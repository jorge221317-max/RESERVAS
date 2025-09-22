import smtplib
from email.message import EmailMessage

def enviar_email(destinatario, asunto, cuerpo):
    msg = EmailMessage()
    msg['Subject'] = asunto
    msg['From'] = "jorge221317@gmail.com"       # Cambiá por tu email
    msg['To'] = destinatario
    msg.set_content(cuerpo)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("tu_email@gmail.com", "tu_password")
        smtp.send_message(msg)
