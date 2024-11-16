import easyocr
from transformers import LayoutLMv3Processor, LayoutLMv3ForSequenceClassification
from pathlib import Path
from PIL import Image
import torch
import warnings

# Suppress specific FutureWarnings
warnings.simplefilter("ignore", category=FutureWarning)

# Define DEVICE
DEVICE = "cpu"

# Load model and processor
processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=False)
model = LayoutLMv3ForSequenceClassification.from_pretrained(Path("model"))

def scale_bounding_box(box, width_scale, height_scale):
    """Scales a bounding box using given width and height scales."""
    return [
        int(box[0][0] * width_scale),
        int(box[0][1] * height_scale),
        int(box[2][0] * width_scale),
        int(box[2][1] * height_scale),
    ]

def get_ocr_result(image_path: Path) -> list:
    """Extracts OCR data from an image using easyocr."""
    reader = easyocr.Reader(['en'])
    result = reader.readtext(str(image_path))

    ocr_result = []
    for (bbox, text, prob) in result:
        ocr_result.append({
            "bounding_box": bbox,
            "word": text,
            "confidence": prob
        })
    return ocr_result

def predict_document_image(image_path: Path):
    """Predicts the class of a document image using LayoutLMv3."""

    # Get OCR results
    ocr_result = get_ocr_result(image_path)

    with Image.open(image_path).convert("RGB") as image:
        width, height = image.size
        width_scale = 1000 / width
        height_scale = 1000 / height

        words = []
        boxes = []
        for row in ocr_result:
            boxes.append(scale_bounding_box(row["bounding_box"], width_scale, height_scale))
            words.append(row["word"])

        encoding = processor(
            image,
            words,
            boxes=boxes,
            max_length=512,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )

    with torch.inference_mode():
        output = model(
            input_ids=encoding["input_ids"].to(DEVICE),
            attention_mask=encoding["attention_mask"].to(DEVICE),
            bbox=encoding["bbox"].to(DEVICE),
            pixel_values=encoding["pixel_values"].to(DEVICE)
        )

    predicted_class = output.logits.argmax()
    return model.config.id2label[predicted_class.item()]
