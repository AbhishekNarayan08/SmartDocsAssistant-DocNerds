# email_reader.py

import imaplib
import email
from email.header import decode_header
import os
from document_classifier import model, processor, predict_document_image
from pathlib import Path
import warnings
from pdf2image import convert_from_path

# Suppress specific FutureWarnings
warnings.simplefilter("ignore", category=FutureWarning)

EMAIL_FOLDER = "Hackathon"

def convert_pdf_to_image(pdf_path: Path) -> Path:
    """Converts a PDF to an image and saves it."""
    images = convert_from_path(str(pdf_path))
    image_path = pdf_path.with_suffix(".jpg")  # Save as .jpg
    images[0].save(image_path, "JPEG")  # Saving the first page as an image
    return image_path

# Download email attachments
def download_attachments(mail, folder):
    mail.select(EMAIL_FOLDER)
    status, messages = mail.search(None, 'UNSEEN')

    for mail_id in messages[0].split():
        _, msg_data = mail.fetch(mail_id, "(RFC822)")

        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                    print(f"Processing email: {subject}")

                if msg.is_multipart():
                    for part in msg.walk():
                        valid_content_types = ["application/pdf", "image/jpeg", "application/png"]
                        if part.get_content_type() in valid_content_types:
                            filename = part.get_filename()
                            if filename:
                                filepath = os.path.join(folder, filename)
                                with open(filepath, "wb") as f:
                                    f.write(part.get_payload(decode=True))
                                print(f"Downloaded: {filename}")

                                filepath = Path(filepath)
                                if filepath.suffix.lower() == ".pdf":
                                    filepath = convert_pdf_to_image(filepath)
                                    print(f"Converted PDF to image: {filepath}")


                                return filepath





def process_new_email(mail, email_id):
    # Fetch the email by id
    status, msg_data = mail.fetch(email_id, "(RFC822)")

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding if encoding else "utf-8")


            mail.store(email_id, '-FLAGS', '\\Seen')
            # Process attachments
            filepath = download_attachments(mail, "documents")
            print("Email Processed")
            mail.store(email_id, '+FLAGS', '\\Seen')  # Mark the email as read

            # Extract sender email
            sender_email = msg["From"]
            # You can extract the email part using regular expressions if needed
            sender_email = sender_email.split('<')[-1].split('>')[0]  # This removes extra details

            return filepath, sender_email
