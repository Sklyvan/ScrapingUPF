from UserInterface import displayNumericMenu
from NetworkRequests import Request
from bs4 import BeautifulSoup as BS
import requests, json, time, datetime

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
URL = 'https://gestioacademica.upf.edu/pds/consultaPublica/look%5Bconpub%5DInicioPubHora?entradaPublica=true' # URL principal para establecer una conexión y obtener una sesión.
URL_RND = 'https://gestioacademica.upf.edu/pds/consultaPublica/look[conpub]MostrarPubHora' # Con esta URL obtenemos un número "aleatorio" que nos permite simular la conexión de un usuario consultando el horario.
URL_JSON ='https://gestioacademica.upf.edu/pds/consultaPublica/[Ajax]selecionarRangoHorarios' # Con esta URL obtenermos el archivo JSON que contiene el horario.

DATA = "planEstudio=634&idiomaPais=es.ES&ultimoPlanDocente=&indExamenRecuperacion=true&trimestre=T/1&planDocente=2021&accesoSecretaria=" \
              "&entradaPublica=true&centro=337&estudio=3377&idPestana=1&curso=3&grupo1=1&grupos=1&asignatura24304=24304&asignatura26003=26003"

fromDate, toDate = "27/09/2021", "03/10/2021" # La fecha de entrada se puede meter en este formato y el programa la pasa a UNIX Time.
fromDate, toDate = int(time.mktime(datetime.datetime.strptime(fromDate, "%d/%m/%Y").timetuple())), int(time.mktime(datetime.datetime.strptime(toDate, "%d/%m/%Y").timetuple()))

try:
       print("Establishing session.")
       SESSION = Request(URL, HEADERS, requests.Session(), requestMethod='GET').SESSION
except Exception as ErrorCode:
       print(f"Something went wrong while generating session. {ErrorCode}")
else:
       print("Session successfully established.")

       try:
              print("Searching for RND number.")
              soupRND = Request(URL_RND, HEADERS, SESSION, requestMethod='POST', postData=DATA).Soup
       except Exception as ErrorCode:
              print(f"Something went wrong while simulating a user connection. {ErrorCode}")
       else:
              javaScriptCode = str(soupRND.findAll('script', type='text/javascript')[4])
              initialPosition = javaScriptCode.find('selecionarRangoHorarios?rnd=') + len('selecionarRangoHorarios?rnd=') # Obteniendo la primera posición del primer dígito de RND.
              RND = javaScriptCode[initialPosition:initialPosition+6].replace("'", "").replace(" ", "")
              timeRND = f'rnd={RND}&start={fromDate}&end={toDate}'
              print("RND Number found.")
              try:
                     print("Downloading the content.")
                     contentRequest = Request(URL_JSON, HEADERS, SESSION, requestMethod='POST', postData=timeRND)
              except Exception as ErrorCode:
                     print(f"Something went wrong while obtaining the request content. {ErrorCode}")
              else:
                     jsonFile = contentRequest.getJSON(exportFile=True)
                     print("Content downloaded, JSON file saved.")
