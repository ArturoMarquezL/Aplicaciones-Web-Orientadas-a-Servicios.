import requests
import json

resultado = requests.get(" https://api.jikan.moe/v3/search/anime?q=naruto")
print(resultado.status_code)
print(resultado.headers["Content-Type"])

anime = resultado.json()
print(anime.keys())
print(anime["results"])

results=anime["results"]

print(results[0].keys())

encoded = json.dumps(results)
decoded = json.loads(encoded)
print(decoded[0]["title"]["image_url"]["url"]["synopsis"])