from datetime import datetime
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import urllib.request 

url = "https://rupalibank.com.bd/admin_web/files/currency/CurrencyDetail.pdf"
urllib.request.urlretrieve(url, "CurrencyDetail.pdf")

'''
port = 465
smtp_server = "smtp.yandex.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
RECEIPIENT = os.environ.get('USER_RECEIPIENT')
message = """\
Subject: GitHub Email Report

This is your daily email report.
"""

email_user = USERNAME
email_password = PASSWORD
email_rcver = RECEIPIENT

subject = "currency details as on ", datetime.now().strftime("%m/%d/%Y")

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_rcver
msg['Subject'] = subject

body = """\
Subject: GitHub Email Report

This is your daily email report.
"""
msg.attach(MIMEText(body, 'plain'))

filename = "CurrencyDetail.pdf"
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header('content-disposition', "attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()

server = smtplib.SMTP(smtp_server, port)
server.starttls()
server.login(email_user, email_password)

server.sendmail(email_user, email_rcver, text)
server.quit()

print("Sent!")
'''





'''
import smtplib, ssl
import os


port = 465
smtp_server = "smtp.yandex.com"
USERNAME = os.environ.get('USER_EMAIL')
PASSWORD = os.environ.get('USER_PASSWORD')
RECEIPIENT = os.environ.get('USER_RECEIPIENT')
message = """\
Subject: GitHub Email Report

This is your daily email report.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(USERNAME,PASSWORD)
    server.sendmail(USERNAME,RECEIPIENT,message)
'''
