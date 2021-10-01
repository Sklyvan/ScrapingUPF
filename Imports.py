# # # Python Required Libraries & Modules # # #
from NetworkRequests import Request
from bs4 import BeautifulSoup as BS
import requests, json, sys
from ScheduleBlocks import *
from Configuration import *
from GoogleCalendar import Calendar

# # # Python Required Constants # # #
CONFIG_FILE = "UserPreferences.ini"
URL = 'https://gestioacademica.upf.edu/pds/consultaPublica/look%5Bconpub%5DInicioPubHora?entradaPublica=true' # URL principal para establecer una conexión y obtener una sesión.
URL_RND = 'https://gestioacademica.upf.edu/pds/consultaPublica/look[conpub]MostrarPubHora' # Con esta URL obtenemos un número "aleatorio" que nos permite simular la conexión de un usuario consultando el horario.
URL_JSON = 'https://gestioacademica.upf.edu/pds/consultaPublica/[Ajax]selecionarRangoHorarios' # Con esta URL obtenermos el archivo JSON que contiene el horario.