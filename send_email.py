from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'nitcevents12@gmail.com'
email_password = 'oxigjruoqjeevenu'
email_receiver = 'jatingoyal7340@gmail.com'

subject = 'FINALLY'

body = """
Aa gya kya!!!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())