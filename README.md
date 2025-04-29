# 📝 SmartDocsAssistant-DocNerds

**SmartDocsAssistant-DocNerds** is a Python-based document automation pipeline that reads incoming emails, classifies their content, generates documents using machine learning models and templates, and forwards them appropriately. 

---

## 📁 Repository Structure

```
SmartDocsAssistant-DocNerds/
├── data/                       # Training data, e.g., labeled emails, features for model
├── documents/                  # Generated documents or templates (e.g., DOCX, JSON)
├── model/                      # Model artifacts and notebooks
│   └── model.ipynb             # Notebook for training and evaluating document classification model
├── document_classifier.py      # Loads trained model to classify email content
├── email_reader.py             # Connects to email server and fetches new messages
├── email_sender.py             # Sends generated documents via SMTP
├── main.py                     # Orchestrates the end-to-end workflow
├── .gitignore                  # Files and folders to ignore in Git
└── .gitattributes              # Git attributes configuration
```

---

## 🔄 End-to-End Workflow

1. **Read Emails**  
   - `email_reader.py` connects to the IMAP server, polls the inbox, and downloads new messages.  
   - Extracts sender, subject, and body text for each email.

2. **Classify Content**  
   - `document_classifier.py` loads the pre-trained classification model (from `model/`) to assign a document type label (e.g., invoice, report, notice) based on email text.

3. **Generate Document**  
   - Based on the classification, selects an appropriate template in `documents/`.  
   - Optionally, uses placeholders in templates to fill in extracted entities from the email.

4. **Forward or Store**  
   - `email_sender.py` attaches the generated document and emails it to the intended recipient via SMTP.  
   - Logs the transaction and stores a copy in `documents/`.

5. **Orchestration**  
   - `main.py` ties together reading, classifying, generating, and sending in a single script for scheduled or on-demand execution.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+  
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Configuration

- Create a `config.py` or `.env` file (example in `email_reader.py`) with your IMAP/SMTP credentials:
  ```python
  IMAP_HOST = "imap.example.com"
  IMAP_USER = "you@example.com"
  IMAP_PASS = "yourpassword"
  
  SMTP_HOST = "smtp.example.com"
  SMTP_PORT = 587
  SMTP_USER = "you@example.com"
  SMTP_PASS = "yourpassword"
  ```

### Running the Pipeline

```bash
python main.py
```

- This will process all new emails, classify them, generate documents, and forward them accordingly.

---

## 🔧 Scripts Overview

- **`email_reader.py`**: IMAP email fetcher  
- **`document_classifier.py`**: Text classifier for document type  
- **`main.py`**: Workflow orchestrator  
- **`email_sender.py`**: SMTP email sender  

---

## 👤 Author

**Abhishek Narayan**  
IIT Delhi  
