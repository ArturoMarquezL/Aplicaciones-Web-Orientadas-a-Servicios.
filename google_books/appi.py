import requests
import json

resultado = requests.get("https://www.googleapis.com/books/v1/volumes?q=quilting")
print(resultado.status_code)
print(resultado.headers["Content-Type"])

books = resultado.json()
print(books["totalItems"])
items = books["items"]
print(items[1].keys())

encode = json.dumps(items)
decode = json.loads(encode)
print(decode[1]["volumeInfo"]["title"])
