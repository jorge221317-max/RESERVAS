import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_mail(destinatario: str, asunto: str, mensaje: str):
    """
    Función para enviar un mail sencillo.
    Configurá con tu SMTP.
    """
    remitente = "tucorreo@gmail.com"
    password = "tu_password"  # Mejor usar variables de entorno

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        server.send_message(msg)
        server.quit()
        print(f"Mail enviado a {destinatario}")
    except Exception as e:
        print(f"Error enviando mail: {e}")
