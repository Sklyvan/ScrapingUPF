from Imports import *

def extractRND(fromSoup):
       javaScriptCode = str(fromSoup.findAll('script', type='text/javascript')[4])
       initialPosition = javaScriptCode.find('selecionarRangoHorarios?rnd=') + len('selecionarRangoHorarios?rnd=')  # Obteniendo la primera posición del primer dígito de RND.
       RND = javaScriptCode[initialPosition:initialPosition + 6].replace("'", "").replace(" ", "")
       return RND

def downloadContent(fromData, fromHeaders=''):
       jsonFile = False

       try:
              print("Establishing session.")
              SESSION = Request(URL, fromHeaders, requests.Session(), requestMethod='GET').SESSION
       except Exception as ErrorCode:
              print(f"Something went wrong while generating session. {ErrorCode}")
              return False
       print("Session successfully established.")

       try:
              print("Searching for RND number.")
              soupRND = Request(URL_RND, fromHeaders, SESSION, requestMethod='POST', postData=fromData).Soup
       except Exception as ErrorCode:
              print(f"Something went wrong while connecting to search RND number. {ErrorCode}")
              return False
       RND = extractRND(soupRND)
       timeRND = f'rnd={RND}&start={fromDate}&end={toDate}'
       print("RND Number found.")

       try:
              print("Downloading the content.")
              contentRequest = Request(URL_JSON, fromHeaders, SESSION, requestMethod='POST', postData=timeRND)
       except Exception as ErrorCode:
              print(f"Something went wrong while obtaining the request content. {ErrorCode}")
              return False
       jsonFile = contentRequest.getJSON(exportFile=True)
       print("Content downloaded, JSON file saved.")

       return jsonFile

if __name__ == '__main__':
       fromSubjects, userSubjectsGroups, fromGroups, basicInformation, timeRange = extractConfig(CONFIG_FILE)
       DATA = generateData(fromSubjects, fromGroups, basicInformation)
       fromDate, toDate = int(time.mktime(datetime.datetime.strptime(timeRange[0], "%d/%m/%Y").timetuple())), int(time.mktime(datetime.datetime.strptime(timeRange[1], "%d/%m/%Y").timetuple()))

       if (jsonFile := downloadContent(DATA, fromHeaders=getUserHeaders(CONFIG_FILE))):
              print(f"Downloaded {len(jsonFile)-1} subjects blocks.")
              generateBlocks(jsonFile, len(jsonFile)-1)
       else:
              print(f"Something went wrong, request failed.")
