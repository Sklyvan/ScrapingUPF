# # # Python Required Libraries & Modules # # #
from NetworkRequests import Request, HTML_LocalFile
from bs4 import BeautifulSoup as BS
from tzlocal import get_localzone
import requests, json, sys
from ScheduleBlocks import *
from Configuration import *
from GoogleCalendar import Calendar

# # # Python Required Constants # # #
CONFIG_FILE = "../UserPreferences.ini"
URL = 'https://gestioacademica.upf.edu/pds/consultaPublica/look%5Bconpub%5DInicioPubHora?entradaPublica=true' # URL principal para establecer una conexión y obtener una sesión.
URL_RND = 'https://gestioacademica.upf.edu/pds/consultaPublica/look[conpub]MostrarPubHora' # Con esta URL obtenemos un número "aleatorio" que nos permite simular la conexión de un usuario consultando el horario.
URL_JSON = 'https://gestioacademica.upf.edu/pds/consultaPublica/[Ajax]selecionarRangoHorarios' # Con esta URL obtenermos el archivo JSON que contiene el horario.
TIMEZONE = get_localzone().key

GOOGLE_CALENDAR_API_MAX_COLORS = 11
DECODE_HTML_FILE = 'latin-1'
PYTHON_VERSION = {'Major': 3, 'Minor': 8}
REPOSITORY_URL = "https://github.com/Sklyvan/ScrapingUPF"
README_URL = "https://github.com/Sklyvan/ScrapingUPF/blob/main/README.md"