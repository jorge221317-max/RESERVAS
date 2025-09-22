import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def enviar_email(destinatario, asunto, cuerpo):
    if not EMAIL_USER or not EMAIL_PASS:
        print("EMAIL_USER o EMAIL_PASS no configurados. Email no enviado.")
        return

    msg = EmailMessage()
    msg["Subject"] = asunto
    msg["From"] = EMAIL_USER
    msg["To"] = destinatario
    msg.set_content(cuerpo)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_USER, EMAIL_PASS)
        smtp.send_message(msg)
