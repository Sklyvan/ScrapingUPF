from tzlocal import get_localzone # With this, I extract the user timezone and use it to add the events to the calendar with this timezone.

# Main program constants.
CONFIG_FILE = "../UserPreferences.ini"
URL = 'https://gestioacademica.upf.edu/pds/consultaPublica/look%5Bconpub%5DInicioPubHora?entradaPublica=true' # URL principal para establecer una conexión y obtener una sesión.
URL_RND = 'https://gestioacademica.upf.edu/pds/consultaPublica/look[conpub]MostrarPubHora' # Con esta URL obtenemos un número "aleatorio" que nos permite simular la conexión de un usuario consultando el horario.
URL_JSON = 'https://gestioacademica.upf.edu/pds/consultaPublica/[Ajax]selecionarRangoHorarios' # Con esta URL obtenermos el archivo JSON que contiene el horario.
TIMEZONE = get_localzone().key
GOOGLE_CALENDAR_API_MAX_COLORS = 11 # Maximum number of colors allowed by Google Calendar API.
DECODE_HTML_FILE = 'latin-1' # This is the encoding of the HTML file.
PYTHON_VERSION = {'Major': 3, 'Minor': 8} # This is the required Python version used to run the program.

# Graphic User Interface variables.
REPOSITORY_URL = "https://github.com/Sklyvan/ScrapingUPF"
README_URL = "https://github.com/Sklyvan/ScrapingUPF/blob/main/README.md"
APP_LOGO = "../res/GUI/AppLogo.png"