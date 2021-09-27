import requests

from NetworkRequests import Request

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

URL = 'https://gestioacademica.upf.edu/pds/consultaPublica/look[conpub]ActualizarCombosPubHora'
DATA = "entradaPublica=true&idiomaPais=ca.ES&centro=337&estudio=3377&planEstudio=634&curso=3&trimestre=T/1&asignatura1=24303&asignatura2=24304&asignatura3=26003&asignatura4=24306&planDocente=2021"

MyRequest = Request(URL, HEADERS, requests.Session(), requestMethod='POST', postData=DATA)
jSON_File = MyRequest.getJSON(exportFile=True)