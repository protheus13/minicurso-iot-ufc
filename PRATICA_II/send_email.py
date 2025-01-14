import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

def sendEmail():
    # Configurações do servidor de e-mail
    smtp_server = 'smtp.gmail.com' 
    smtp_port = 587 
    smtp_user = 'adm@gmail.com' 
    smtp_password = 'senha_email'

    # Informações do e-mail
    from_email = 'adm@gmail.com' 
    to_email = ['email1@gmail.com','email2@gmail.com']
    subject = 'CAIXA DÁGUA COM NÍVEL BAIXO'
    body = 'QAP, cambada. QRA Edvaldobot, QTC: A caixa dágua principal do campus está com nível baixo. Link para verificação: https://waterbox-ifce.vercel.app/. QRT.'
    # Cria a mensagem do e-mail
    msg = MIMEMultipart() 
    msg['From'] = from_email 
    msg['To'] = ", ".join(to_email) 
    msg['Subject'] = subject 
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conecta ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port) 
        server.starttls() # Usa TLS (Transport Layer Security) 
        server.login(smtp_user, smtp_password)

        # Envia o e-mail
        server.sendmail(from_email, to_email, msg.as_string())
        print('E-mail enviado com sucesso!')

    except Exception as e: print(f'Erro ao enviar o e-mail: {e}')

    finally: server.quit()
