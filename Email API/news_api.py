import smtplib
import ssl
import os
import requests

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=df45f55e19b54b649ff36bf2178e407f&language=en"
api_key = os.getenv("news_api")

r = requests.get(url)
content = r.json()

author = []
title = []
description = []
url = []
for articles in content["articles"]:
    author.append(articles["author"])
    title.append(articles["title"])
    description.append(articles["description"])
    url.append(articles["url"])

message = ""
for authors, titles, descriptions, urls in zip(author, title, description, url):
    message += f"{authors}\n{titles}\n{descriptions}\n{urls}\n\n"
message = f"Subject: Today's News\n{message}"
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