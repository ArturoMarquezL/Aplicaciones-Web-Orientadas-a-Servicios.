import web
import requests
import json

render = web.template.render("conte/")
class Index():
  def GET(self):
    anime=None
    return render.index(anime)

  def POST(self):
    form = web.input() 
    titulo=form["titulo"]
    resultado = requests.get(" https://api.jikan.moe/v3/search/anime?q="+titulo) 
    
    anime = resultado.json()
    results=anime["results"]
    encoded = json.dumps(results)
    decoded = json.loads(encoded)

    anime=[]
    
    for animes in decoded:
        
        url=animes["url"]
        imagenes=animes["image_url"]
        synopsis=animes["synopsis"]
        episodes=animes["episodes"]
        link ="<a href='"+url+"'>"+url+"</a>"
        imagen ="<img src='"+imagenes+"'/>"



        datos={
    
        "titulo":titulo,
        "episodes":episodes,
        "imagen":imagen,
        "url":link,
        "synopsis":synopsis
        }
        anime.append(datos)

    print(anime)   

    return render.index(anime)