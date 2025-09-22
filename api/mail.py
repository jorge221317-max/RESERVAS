import smtplib
from email.message import EmailMessage

def enviar_mail(destinatario: str, asunto: str, mensaje: str):
    email = EmailMessage()
    email["From"] = "tuemail@gmail.com"
    email["To"] = destinatario
    email["Subject"] = asunto
    email.set_content(mensaje)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("tuemail@gmail.com", "tucontraseña")
        smtp.send_message(email)
