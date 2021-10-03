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
              sys.exit(f"Something went wrong while generating session. {ErrorCode}")
              return False
       print("Session successfully established.")

       try:
              print("Searching for RND number.")
              soupRND = Request(URL_RND, fromHeaders, SESSION, requestMethod='POST', postData=fromData).Soup
       except Exception as ErrorCode:
              sys.exit(f"Something went wrong while connecting to search RND number. {ErrorCode}")
              return False
       RND = extractRND(soupRND)
       timeRND = f'rnd={RND}&start={fromDate}&end={toDate}'
       print("RND Number found.")

       try:
              print("Downloading the content.")
              contentRequest = Request(URL_JSON, fromHeaders, SESSION, requestMethod='POST', postData=timeRND)
       except Exception as ErrorCode:
              sys.exit(f"Something went wrong while obtaining the request content. {ErrorCode}")
              return False
       jsonFile = contentRequest.getJSON(exportFile=True)
       print("Content downloaded, JSON file saved.")

       return jsonFile

if __name__ == '__main__':
       if sys.version_info.major < 3 or (sys.version_info.major >= 3 and sys.version_info.minor < 8): # Python 3.8 or bigger version is needed for Walrus Operator.
              sys.exit(f"You're using Python {sys.version_info.major}.{sys.version_info.minor}, required version is 3.8 or bigger.")

       userPreferences = getUserPreferences(CONFIG_FILE)

       if isUsingEspaiAulaFilePath(userPreferences):
              espaiAulaFile = HTML_LocalFile(getEspaiAulaFilePath(userPreferences), 'latin-1')
              fromGroups, fromSubjects, userSubjectsGroups, pGroups, sGroups = extractSubjectsPreferencesFromFile(espaiAulaFile)
       else:
              fromGroups, fromSubjects, userSubjectsGroups, pGroups, sGroups = extractSubjectsPreferences(userPreferences)

       basicInformation, timeRange = extractRequestInformation(userPreferences)
       DATA = generateData(fromSubjects, fromGroups, basicInformation)
       fromDate, toDate = int(time.mktime(datetime.datetime.strptime(timeRange[0], "%d/%m/%Y").timetuple())), int(time.mktime(datetime.datetime.strptime(timeRange[1], "%d/%m/%Y").timetuple()))

       if (jsonFile := downloadContent(DATA, fromHeaders=getUserHeaders(CONFIG_FILE))):
              if (n_downloadedSubjects := len(jsonFile)-1) > 0:
                     print(f"Downloaded {n_downloadedSubjects} subjects blocks.")
                     subjectsBlocks = generateBlocks(jsonFile, dict(zip(fromSubjects, zip(userSubjectsGroups, pGroups, sGroups))), n_downloadedSubjects)
                     print(f"Using {len(subjectsBlocks)} subjects blocks.")
              else:
                     sys.exit("No subjects blocks have been downloaded, closing program.")
       else:
              sys.exit(f"Something went wrong generating blocks, closing program.")

       MyCalendar = Calendar()

       for subject in subjectsBlocks:
              print(f"Adding {subject.name} to the calendar.")
              MyCalendar.addEvent(f"{subject.name} ({subject.type[0]})", subject.classroom, subject.getDescription(), subject.start, subject.end, TIMEZONE)
              print(f"{subject.name} added to the calendar.")
       print("Done!")
