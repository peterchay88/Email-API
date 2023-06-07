import smtplib
import ssl
import os
import requests

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=df45f55e19b54b649ff36bf2178e407f"
api_key = os.getenv("news_api")

r = requests.get(url)
content = r.json()

author = []
title = []
description = []
for articles in content["articles"]:
    author.append(articles["author"])
    title.append(articles["title"])
    description.append(articles["description"])

message = ""
for authors, titles, descriptions in zip(author, title, description):
    message += f"{authors}\n{titles}\n{descriptions}\n\n"
message = message.encode("utf-8")

host = "smtp.gmail.com"
port = 465

username = "peterchay112@gmail.com"
password = os.getenv("PASSWORD")

receiver = "peterchay112@gmail.com"
context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)