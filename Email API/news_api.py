import smtplib
import ssl
import os
import requests

host = "smtp.gmail.com"
port = 465

username = "peterchay112@gmail.com"
password = os.getenv("PASSWORD")

receiver = "peterchay112@gmail.com"
context = ssl.create_default_context()

message = "This is a test"

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)