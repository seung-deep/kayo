import smtplib
from email.message import EmailMessage

def send_otp(recipient):
    sender_email = "@gmail.com"
    message = EmailMessage()
    message.set_content("Hello")
    message["Subject"] = "OTP for kayo"
    message["From"] = sender_email
    message["To"] = recipient
    
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()  # Enable TLS
        smtp.login(sender_email, "")
        smtp.send_message(message)

send_otp("@gmail.com")
