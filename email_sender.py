import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# Email account credentials
EMAIL_USER = "abhisheknarayan354@gmail.com"
EMAIL_PASSWORD = ""  # Use App password here

def send_classified_email(classification, file_path, sender_email):
    subject = f"Document Classification: {classification}"
    body = f"The document recieved has been classified as: {classification}\n\nSender's email: {sender_email}"

    # Set the sender and recipient
    sender_email_address = EMAIL_USER

    document_type_mapping = {
    "income_statements": "abhisheknarayan354@gmail.com",
    "balance_sheets": "abhisheknarayan354@gmail.com",
    "cash_flows": "abhisheknarayan354@gmail.com",
    "notes": "abhisheknarayan354@gmail.com",
    "others": "abhisheknarayan354@gmail.com"
    }

    receiver_email = document_type_mapping.get(classification, "abhisheknarayan354@gmail.com")

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender_email_address
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Attach the file to the email
    try:
        # Open the file to be sent
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode the file in base64
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition", f"attachment; filename={os.path.basename(file_path)}"
        )

        # Attach the file to the email
        msg.attach(part)

        # Send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(sender_email_address, receiver_email, msg.as_string())
            print(f"Email sent successfully for classification: {classification}")

    except Exception as e:
        print(f"Error sending email with attachment: {e}")
