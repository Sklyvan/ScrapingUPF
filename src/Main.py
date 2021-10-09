from Imports import *

def extractRND(fromSoup):
       javaScriptCode = str(fromSoup.findAll('script', type='text/javascript')[4])
       initialPosition = javaScriptCode.find('selecionarRangoHorarios?rnd=') + len('selecionarRangoHorarios?rnd=')  # Obteniendo la primera posición del primer dígito de RND.
       RND = javaScriptCode[initialPosition:initialPosition + 6].replace("'", "").replace(" ", "")
       try:
              float(RND)
       except ValueError:
              sys.exit("Something went pretty wrong while searching the RND value. This is probably a code bug, so contact Sklyvan.")
              return False
       else:
              return RND

def downloadContent(fromData, fromDate, toDate, fromHeaders=''):
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

def RunApplication(deleteMode=False):
       # Python 3.8 or bigger version is needed for Walrus Operator.
       if sys.version_info.major < PYTHON_VERSION['Major'] or (sys.version_info.major >= PYTHON_VERSION['Major'] and sys.version_info.minor < PYTHON_VERSION['Minor']):
              sys.exit(f"You're using Python {sys.version_info.major}.{sys.version_info.minor}, required version is 3.8 or bigger.")
       userPreferences = getUserPreferences(CONFIG_FILE)

       if isUsingEspaiAulaFilePath(userPreferences):
              espaiAulaFile = HTML_LocalFile(getEspaiAulaFilePath(userPreferences), DECODE_HTML_FILE)
              fromGroups, fromSubjects, userSubjectsGroups, pGroups, sGroups = extractSubjectsPreferencesFromFile(espaiAulaFile)
       else:
              fromGroups, fromSubjects, userSubjectsGroups, pGroups, sGroups = extractSubjectsPreferences(userPreferences)

       subjectsColors = dict(zip(fromSubjects, [str(x%GOOGLE_CALENDAR_API_MAX_COLORS+1) for x in range(len(fromSubjects))]))

       basicInformation, timeRange = extractRequestInformation(userPreferences)
       DATA = generateData(fromSubjects, fromGroups, basicInformation)
       fromDate, toDate = int(time.mktime(datetime.datetime.strptime(timeRange[0], "%d/%m/%Y").timetuple())), int(time.mktime(datetime.datetime.strptime(timeRange[1], "%d/%m/%Y").timetuple()))

       if (jsonFile := downloadContent(DATA, fromDate, toDate, fromHeaders=getUserHeaders(CONFIG_FILE))):
              if (n_downloadedSubjects := len(jsonFile)-1) > 0:
                     print(f"Downloaded {n_downloadedSubjects} subjects blocks.")
                     subjectsBlocks = generateBlocks(jsonFile, dict(zip(fromSubjects, zip(userSubjectsGroups, pGroups, sGroups))), n_downloadedSubjects)
                     print(f"Using {len(subjectsBlocks)} subjects blocks.")
              else:
                     sys.exit("No subjects blocks have been downloaded, closing program.")
       else:
              sys.exit(f"Something went wrong generating blocks, closing program.")

       MyCalendar = Calendar()

       if deleteMode:
              descriptions = list(map(lambda x: x.getDescription(),subjectsBlocks))
              events = MyCalendar.getEvents()
              for event in events:
                     eventDescription, eventID = event[0], event[1]
                     if eventDescription in descriptions:
                            print(f"Deleting EventID: {eventID} | {eventDescription}")
                            MyCalendar.deleteEvent(eventID)
                     else:
                            print(f"Skipped EventID: {eventID} | {eventDescription}")
              print("Events Deleted!")
       else:
              for subject in subjectsBlocks:
                     print(f"Adding {subject.name} to the calendar.")
                     MyCalendar.addEvent(f"{subject.name} ({subject.type[0]})", subject.classroom, subject.getDescription(), subject.start, subject.end, TIMEZONE, colorID=subjectsColors[str(subject.code)])
                     print(f"{subject.name} added to the calendar.")
              print("Done!")
