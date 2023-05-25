import requests

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=df45f55e19b54b649ff36bf2178e407f"
api_key = "df45f55e19b54b649ff36bf2178e407f"

# Make a request
r = requests.get(url)

# get a dictionary with data
content = r.json()
for articles in content["articles"]:
    print(articles["author"])