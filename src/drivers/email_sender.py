import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "mndrt2nf6kydiijl@ethereal.email"
    login = "mndrt2nf6kydiijl@ethereal.email"
    password = "uj9RZM1pRHJD8uhKFy"

    msg = MIMEMultipart()
    msg["From"] = "rosatur_viagens_teste@email.com"
    msg["to"] = ', '.join(to_addrs)  

    msg["Subject"] = "Confirmação da viagem"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()