import web
import json

urls = (
    '/persona?', 'Persona'
)
app = web.application(urls, globals())

class Persona():
    def __init__(self): 
        pass
    def GET(self):  
        try:
            data = web.input() 
            nombre = data.nombre
            dia = int(data.dia)
            mes = data.mes
            year = int(data.year)
            edad = 2021 - year
            result={}
            result["nombre"] = nombre
            result["dia"] = dia
            result["mes"] = mes
            result["year"] = year
            result["edad"] = edad
            archivo = open("static/datos.txt","a")
            archivo.write(str(result))
            archivo.close()
            return json.dumps(result)
        except:
            data ={}
            data["error"] = "error 404 url no existente corrija"
            return data

if __name__ =="__main__": 
    app.run()