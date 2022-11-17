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
