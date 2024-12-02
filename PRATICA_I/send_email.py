                                  
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Tem que desabilitar acesso por apps menos seguros nas configurações do e-mail utilizado.
def sendEmail():
    # Configurações do servidor de e-mail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'email@gmail.com'
    smtp_password = 'senhadoemail'

    # Informações do e-mail
    from_email = 'email_de_origem'
    to_email = ['email1@gmail.com','email2@gmail.com']

    subject = 'INFORME CAIXA DÁGUA'
    body = 'Informamos que a caixa dágua se encontra com nível baixo. Favor verificar app. link: link_da_vercel'

    # Cria a mensagem do e-mail
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_email)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conecta ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Usa TLS (Transport Layer Security)
        server.login(smtp_user, smtp_password)

        # Envia o e-mail
        server.sendmail(from_email, to_email, msg.as_string())
        print('E-mail enviado com sucesso!')

    except Exception as e:
        print(f'Erro ao enviar o e-mail: {e}')

    finally:
        server.quit()