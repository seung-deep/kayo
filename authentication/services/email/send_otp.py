import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), "..", "..", ".env")
load_dotenv(dotenv_path=dotenv_path)

def send_otp(recipient):
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = os.getenv("SMTP_PORT")
    smtp_password = os.getenv("SMTP_PASSWORD")
    sender_email = "@gmail.com"
    message = EmailMessage()
    message.set_content("Hello")
    message["Subject"] = "OTP for kayo"
    message["From"] = sender_email
    message["To"] = recipient
    
    with smtplib.SMTP(smtp_server, int(smtp_port)) as smtp:
        smtp.starttls()  # Enable TLS
        smtp.login(sender_email, smtp_password)
        smtp.send_message(message)

send_otp("@gmail.com")
