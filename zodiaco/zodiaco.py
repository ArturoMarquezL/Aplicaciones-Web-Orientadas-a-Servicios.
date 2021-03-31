import web
import json
import random


carta = {}
urls = (
    '/(.*)',
    'Cartas',
)
app = web.application(urls, globals())

class Cartas():
  def __init__(self):
    pass
    
    
  def GET (self, carta):
    try:
      dia = int(carta[0:2])
      mes = int(carta[3:5])
      print(dia, mes)
      
      
      if dia >= 21 and mes == 1 or mes == 2 and dia <= 19:
        horoscopo = {}
        horoscopo["Nombre"] = "Acuario"
        horoscopo["Fecha"] = "Enero  21 – Febrero 19"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "10,55,33"
        horoscopo["Color"] = "vino tinto"
        horoscopo["Horóscopo del día"] =(random.choice([ "Si tienes que trabajar con más personas, puedes tener problemas para lidiar con quien no pueda ir a tu mismo ritmo. Asegúrate de rodearte de personas que respalden tus esfuerzos laborales, o que compartan tu visión de éxito. Puedes descubrir si los intereses de alguien te están bloqueando el camino."]))
        result= json.dumps(horoscopo)
        return result

      elif dia >= 20  and mes == 2 or mes == 3 and dia <= 20:
        horoscopo = {}
        horoscopo["Nombre"] = "Picis"
        horoscopo["Fecha"] = "Febrero  20 – Marzo 20"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = " 29, 87 y 56"
        horoscopo["Color"] = "Plateado."
        horoscopo["Horóscopo del día"] = (random.choice([ "No es tu imaginación, las personas realmente te están prestando más atención que de costumbre, estás en la mira y esto lo puedes aprovechar para transformar la percepción que tienen de ti. Es uno de esos días en los que te toca preguntarte cómo puedes mejorar tu vida, lo mejor es que te resultará fácil encontrar una respuesta."]))
        result= json.dumps(horoscopo)
        return result

      elif dia >= 21  and mes == 3 or mes == 4 and dia <= 19:
        horoscopo = {}
        horoscopo["Nombre"] = "Aries"
        horoscopo["Fecha"] = "Marzo  21 – Abril 19"
        horoscopo["Elemento"] = "Fuego"
        horoscopo["Numero de la suerte"] = "11, 24 y 60."
        horoscopo["Color"] = "Verde"
        horoscopo["Horóscopo del día"] = (random.choice(["Tú expresión y la forma en la que te comunicas, puede estar reprimida o censurada. Puede haber algún roce con tus familiares cercanos, no busques enemigos donde no los hay, trata de mantenerte alejada de las emociones oscuras que te pueden llevar a mostrarte resentida, vengativa o insatisfecha."]))
        result= json.dumps(horoscopo)
        return result

      elif dia >= 20  and mes == 4 or mes == 5 and dia <= 20:
        horoscopo = {}
        horoscopo["Nombre"] = "Tauro"
        horoscopo["Fecha"] = "Abril  20 – Mayo 20"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = "21, 40 y 33."
        horoscopo["Color"] = "Naranja."
        horoscopo["Horóscopo del día"] = (random.choice(["Estás sintiendo algún tipo de responsabilidad frente a tus amigos o a tu medio social, pero evita cargar con algo que no te corresponde. Si eres demasiado protectora, o te sientes muy necesitada de cariño y afecto, las cosas en tu relación de pareja, se pueden complicar el día de hoy."]))
        result= json.dumps(horoscopo)
        return result

      elif dia >= 21  and mes == 5 or mes == 6 and dia <= 21:
        horoscopo = {}
        horoscopo["Nombre"] = "Géminis"
        horoscopo["Fecha"] = "Mayo  21 – Junio 21"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "19, 33 y 67"
        horoscopo["Color"] = "Azul celeste"
        horoscopo["Horóscopo del día"] = (random.choice(["Si tu trabajo tiene que ver con el medio editorial o de comunicación, el fin de mes puede ser un periodo especialmente productivo. Es también un día para cuestionarte si las cosas realmente están funcionando para ti en ese trabajo, o si te está desgastando más de lo que te está brindando."]))
        result= json.dumps(horoscopo)
        return result

      elif dia >= 20  and mes == 6 or mes == 7 and dia <= 20:
        horoscopo = {}
        horoscopo["Nombre"] = "Cáncer"
        horoscopo["Fecha"] = "Junio  20 – Julio 20"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = "22, 9 y 45."
        horoscopo["Color"] = "Blanco"
        horoscopo["Horóscopo del día"] = (random.choice(["Es posible que te sientas inclinada a asimilar todo lo que ha ocurrido desde el inicio de año, para que puedas integrar el aprendizaje recibido. Es un buen día para salir de casa y pasar algo de tiempo haciendo cosas divertidas, involucrándote en algo que te entusiasme y te alegre el corazón."]))
        result= json.dumps(horoscopo)
        return result

      elif dia >= 22  and mes == 7 or mes == 8 and dia <= 22:
        horoscopo = {}
        horoscopo["Nombre"] = "Leo"
        horoscopo["Fecha"] = "Julio  22 – Agosto 22"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "13, 54 y 09."
        horoscopo["Color"] = "Azul marino."
        horoscopo["Horóscopo del día"] = (random.choice(["La energía astrológica te está regalando la capacidad de ver a través de las apariencias, para analizar tus relaciones personales, y así, descubrir en dónde te encuentras dentro de ellas. Hoy es un día en el que te es más fácil ser cariñosa contigo y también con los demás. Aprovecha para tener un gesto amoroso contigo misma, darte un gusto o un regalo."]))
        result= json.dumps(horoscopo)
        return result

      elif dia >= 23  and mes == 8 or mes == 9 and dia <= 22:
        horoscopo = {}
        horoscopo["Nombre"] = "Virgo"
        horoscopo["Fecha"] = "Agosto  23 – Septiembre 22"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = "13, 33 y 78."
        horoscopo["Color"] = "Dorado."
        horoscopo["Horóscopo del día"] = (random.choice(["Si estás soltera, puedes sentir interés por dos personas diferentes y, en este final de mes, quizá debas empezar a decidirte por una. Vives el día mucho más curiosa que de costumbre, pero ten cuidado y no te involucres en una discusión o un asunto que no te corresponde, enfócate en lo tuyo."]))
        result= json.dumps(horoscopo)
        return result

      elif dia >= 23  and mes == 9 or mes == 10 and dia <= 22:
        horoscopo = {}
        horoscopo["Nombre"] = "Libra"
        horoscopo["Fecha"] = "Septiembre  23 – Octubre 22"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "19, 70 y 21"
        horoscopo["Color"] = "Rojo."
        horoscopo["Horóscopo del día"] = (random.choice(["Los eventos recientes te han llevado a hacer un esfuerzo excesivo, así que procura usar estos dos días para relajarte. Te puede costar mucho trabajo adoptar una perspectiva original o diferente, ya que te rodea cierta energía predecible y básica. Prefieres apegarte a lo tradicional."]))
        result= json.dumps(horoscopo)
        return result


      elif dia >= 23 and mes == 10 or mes == 11 and dia <= 21:
        horoscopo = {}
        horoscopo["Nombre"] = "Escorpio"
        horoscopo["Fecha"] = "Octubre  23 – Noviembre 21"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = "10, 78 y 11."
        horoscopo["Color"] = "Violeta"
        horoscopo["Horóscopo del día"] = (random.choice(["Con la luna en tu signo, es un buen día para expresar tus sentimientos y ser más afectuosa con los demás. Pero evita tener expectativas muy altas o irreales, respecto a la reacción que los otros tengan frente a tu demostración de afecto, porque estás muy emocional, y si alguien no responde como esperas, puede venir una discusión."]))
        result= json.dumps(horoscopo)
        return result

      elif dia >= 22  and mes == 11 or mes == 12 and  dia <= 21:
        horoscopo = {}
        horoscopo["Nombre"] = "Sagitario"
        horoscopo["Fecha"] = "Noviembre  20 – Diciembre 20"
        horoscopo["Elemento"] = "Fuego"
        horoscopo["Numero de la suerte"] = "29, 69 y 18."
        horoscopo["Color"] = "Amarillo."
        horoscopo["Horóscopo del día"] =  (random.choice(["Pon atención a lo que ocurre en la vida de tus papás, porque es probable que recibas noticias o que tengas que solucionar una situación latente con tu familia. Puedes sentirte más espiritual, conectada con el mundo metafísico, es un muy buen día para meditar, ir a una sesión de reiki, encender velas, etc."]))
        result= json.dumps(horoscopo)
        return result
          
      elif dia >= 22 or dia <= 20 and mes == 12 or mes == 1:
        horoscopo = {}
        horoscopo["Nombre"] = "Capricornio"
        horoscopo["Fecha"] = "Diciembre  22 – Enero 20"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = " 19, 67 y 13."
        horoscopo["Color"] = "Rosa."
        horoscopo["Horóscopo del día"] = (random.choice(["En estos días, estás tan inquieta mentalmente, que te puede costar trabajo estudiar o resolver una sola cosa en particular. Así que usa a tu favor esta energía para revisar nuevas ideas y conceptos que quizá antes no te habías atrevido a explorar, o no habías tomado en serio."]))
        result= json.dumps(horoscopo)
        return result
    except:
      
      horoscopo = {}
      horoscopo["Fecha"] = "La fecha  " + str(carta)
      horoscopo["Error"] = "Valor incorrecto"
      horoscopo["Solucion"] = "Escribe la fecha de tu nacimiento en forma DD/MM/AAAA"
      result= json.dumps(horoscopo)
      return result


if __name__ == "__main__":
	app.run()