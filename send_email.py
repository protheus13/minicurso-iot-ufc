                                  
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail():
    # Configurações do servidor de e-mail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'infra.sobral@ifce.edu.br'
    smtp_password = 'ifceSobral2018'

    # Informações do e-mail
    from_email = 'infra.sobral@ifce.edu.br'
    to_email = ['geraldo.martins@ifce.edu.br','infra.sobral@ifce.edu.br','francisco.eliel@ifce.edu.br', 'dap.sobral@ifce.edu.br']

    subject = 'CAIXA DÁGUA COM NÍVEL BAIXO'
    body = 'EdvaldoBot informa que a caixa dágua principal do IFCE-Sobral se encontra com nível baixo. favor verificar app. link: https://waterbox-ifce.vercel.app/'

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