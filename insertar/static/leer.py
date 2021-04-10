import web
import json

urls = (
    '/personas?', 'Personas'
)
app = web.application(urls, globals())

class Personas():

  json_file={}

  def read(self):
    try:
      with open("datos.json") as file:
        self.json_file = json.load(file)
      print(self.json_file)
      return json.dumps(self.json_file)

    except Exception as error:
      print("Error {}".format(error.args[0]))

  def writePersonas(self, nombre, dia, mes, year, edad):
    data={
    "Nombre" : nombre,
    "Dia" : dia,
    "Mes" : mes,
    "Ano de nacimiento" : year,
    "Edad" : edad
    }
   
    with open("datos.json") as file:
        self.json_file = json.load(file)
    self.json_file["personas"].append(data)
    with open("datos.json","w") as file:
      json.dump(self.json_file, file)
    return self.read()


  def GET(self):
    try:
      dato = web.input() 
      action = dato["action"]      

      if action == "get":
        return self.read()
        
      elif action == "put":
        nombre = dato.nombre
        dia = int(dato.dia)
        mes = dato.mes
        year = int(dato.year)
        edad = 2021 - year
        self.writePersonas(nombre, dia, mes, year, edad)

        info = {}
        info["info"]= "Datos guardados"
        return json.dumps(info)

    except:
      data = {}
      data["info"] = "Verifica los datos ingresados"
      return json.dumps(data)
       
if __name__ == "__main__":
  app.run()