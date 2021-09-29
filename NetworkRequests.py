from bs4 import BeautifulSoup as BS
import requests, json, os

def getDataDict(dataString):
    """
    Para una string de forma enlace ---> https://www...../...php?id=1&class=5 nos transforma la parte de la petición, a un dicionario ---> DATA[id]=1, DATA[class]=5.
    :param dataString: String de la URL.
    :return: Diccionario listo para el POST.
    """
    DATA = {}
    for x in dataString.split('&'):
        temp = x.split('=')
        DATA[temp[0]] = temp[1]
    return DATA

class Request:
    def __init__(self, URL, HEADERS, SESSION, requestMethod, postData=None, makeRequest=True):
        """
        Objeto para hacer los POST y los GET de forma más sencilla y que limpia los datos automáticamente.
        :param URL: Enlace al que se hace la petición, en caso de que sea un GET, se incluyen también los datos.
        :param HEADERS: Cabezera para simular que la petición es desde Mozilla Firefox/Google Chrome...
        :param SESSION: Conjunto de cookies para que la sesión se mantenga en las diversas peticiones.
        :param requestMethod: Tipo de petición que queremos hacer, el valor puede ser o POST o GET.
        :param postData: En caso de hacer una petición POST, aquí se pasa el string con los datos a mandar.
        :param makeRequest: Booleano, si este valor es False, al crear el objeto, no se hace ninguna petición. (Se usa por si se quieren ir construyendo los datos pero no se tienen todos)
        """
        self.URL = URL
        self.HEADERS = HEADERS
        self.SESSION = SESSION
        self.jSON, self.jsonDir = None, "Path not defined."
        if requestMethod == 'GET' and makeRequest:
            self.HTML_Page = self.SESSION.get(self.URL, headers=self.HEADERS)
        elif requestMethod == 'POST' and makeRequest:
            self.HTML_Page = self.SESSION.post(self.URL, headers=self.HEADERS, data=getDataDict(postData))
        if makeRequest: self.Soup = BS(self.HTML_Page.content, 'html.parser') # Creando el Arbol de Beautiful Soup (Siempre que se haya hecho una petición POST/GET)

    def addToURL(self, stringToAdd): # Añade campos a nuestra petición.
        self.URL += str(stringToAdd)

    def GET(self): # Hace el GET y se crea el BS.
        self.HTML_Page = self.SESSION.get(self.URL, headers=self.HEADERS)
        self.Soup = BS(self.HTML_Page.content, 'html.parser')

    def POST(self, dataString): # Hace el POST con la nueva string de datos y crea el BS.
        self.HTML_Page = self.SESSION.post(self.URL, headers=self.HEADERS, data=getDataDict(dataString))
        self.Soup = BS(self.HTML_Page.content, 'html.parser')

    def getJSON(self, exportFile=False, nameID=None): # Como al final nos devuelve un horario, lo extraemos en formato JSON ya que es mucho más cómo de trabajar.
        self.jSON = json.loads(self.HTML_Page.text)
        if exportFile:
            if not os.path.isdir('./JSON Files'): os.mkdir('./JSON Files')
            if not nameID:
                open('./JSON Files/Data.json', 'w').write(str(self.jSON))
                self.jsonDir = './JSON Files/Data.json'
            else:
                open(f'./JSON Files/Data{nameID}.json', 'w').write(str(self.jSON))
                self.jsonDir = f'./JSON Files/Data{nameID}.json'
        return self.jSON