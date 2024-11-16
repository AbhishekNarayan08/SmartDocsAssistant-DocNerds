# Main function

import imaplib
import email
from email.header import decode_header
import os
from document_classifier import predict_document_image
import warnings
from email_reader import process_new_email
from email_sender import send_classified_email
import time

# Suppress specific FutureWarnings
warnings.simplefilter("ignore", category=FutureWarning)

# Email account credentials
EMAIL_USER = "abhisheknarayan354@gmail.com"
EMAIL_PASSWORD = ""  # Use App password here
EMAIL_FOLDER = "Hackathon"

# Connect to Gmail and fetch attachments
def connect_to_mail():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL_USER, EMAIL_PASSWORD)
    return mail

def check_for_new_emails(mail):
    mail.select(EMAIL_FOLDER)  # Select the inbox folder
    status, messages = mail.search(None, "UNSEEN")  # Search for unread emails
    if status == "OK" and messages != [b'']:
        return messages[0].split()  # List of email ids
    return []

def monitor_new_emails():
    mail = connect_to_mail()

    while True:
        print("---------------Checking for new emails-----------")
        new_emails = check_for_new_emails(mail)

        if new_emails:
            for email_id in new_emails:
                filepath, sender_email = process_new_email(mail, email_id)

                # Classify the downloaded document
                document_type = predict_document_image(filepath)
                print(f"*****************Classified as: {document_type}")

                send_classified_email(document_type, filepath, sender_email)

        time.sleep(6)  # Check every 60 seconds for new emails


def main():
    monitor_new_emails()


if __name__ == "__main__":
    main()
