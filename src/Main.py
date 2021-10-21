import os.path

from Imports import *

def extractRND(fromSoup):
       javaScriptCode = str(fromSoup.findAll('script', type='text/javascript')[4])
       initialPosition = javaScriptCode.find('selecionarRangoHorarios?rnd=') + len('selecionarRangoHorarios?rnd=')  # Obteniendo la primera posición del primer dígito de RND.
       RND = javaScriptCode[initialPosition:initialPosition + 6].replace("'", "").replace(" ", "")
       try:
              float(RND)
       except ValueError:
              if not logOutput: sys.exit("Something went pretty wrong while searching the RND value. This is probably caused by wrong UserPreferences.ini data.")
              else: logOutput.appendPlainText("ERROR:Something went pretty wrong while searching the RND value. This is probably caused by wrong UserPreferences.ini data.")
              return False
       else:
              return RND

def downloadContent(fromData, fromDate, toDate, fromHeaders=''):
       jsonFile = False

       try:
              if not logOutput: print("Establishing session.")
              else: logOutput.appendPlainText("Establishing session.")
              SESSION = Request(URL, fromHeaders, requests.Session(), requestMethod='GET').SESSION
       except Exception as ErrorCode:
              if not logOutput: sys.exit(f"Something went wrong while generating session. {ErrorCode}")
              else: logOutput.appendPlainText(f"ERROR: Something went wrong while generating session. {ErrorCode}")
              return False
       if not logOutput: print("Session successfully established.")
       else: logOutput.appendPlainText("Session successfully established.")

       try:
              if not logOutput: print("Searching for RND number.")
              else: logOutput.appendPlainText("Searching for RND number.")
              soupRND = Request(URL_RND, fromHeaders, SESSION, requestMethod='POST', postData=fromData).Soup
       except Exception as ErrorCode:
              if not logOutput: sys.exit(f"Something went wrong while connecting to search RND number. {ErrorCode}")
              else: logOutput.appendPlainText(f"ERROR: Something went wrong while connecting to search RND number. {ErrorCode}")
              return False
       RND = extractRND(soupRND)
       timeRND = f'rnd={RND}&start={fromDate}&end={toDate}'
       if not logOutput: print("RND Number found.")
       else: logOutput.appendPlainText("RND Number found.")

       try:
              if not logOutput: print("Downloading the content.")
              else: logOutput.appendPlainText("Downloading the content.")
              contentRequest = Request(URL_JSON, fromHeaders, SESSION, requestMethod='POST', postData=timeRND)
       except Exception as ErrorCode:
              if not logOutput: sys.exit(f"Something went wrong while obtaining the request content. {ErrorCode}")
              else: logOutput.appendPlainText(f"ERROR: Something went wrong while obtaining the request content. {ErrorCode}")
              return False
       jsonFile = contentRequest.getJSON(exportFile=True)
       if not logOutput: print("Content downloaded, JSON file saved.")
       else: logOutput.appendPlainText("Content downloaded, JSON file saved.")

       return jsonFile

def RunApplication(deleteMode=False, logMessages=None):
       global logOutput # Esto es cutre, pero me da pereza modificar la estructura entera del proyecto por culpa de una puta GUI.
       logOutput = logMessages
       # Python 3.8 or bigger version is needed for Walrus Operator.
       if sys.version_info.major < PYTHON_VERSION['Major'] or (sys.version_info.major >= PYTHON_VERSION['Major'] and sys.version_info.minor < PYTHON_VERSION['Minor']):
              sys.exit(f"You're using Python {sys.version_info.major}.{sys.version_info.minor}, required version is 3.8 or bigger.")

       if os.path.isfile(CONFIG_FILE): userPreferences = getUserPreferences(CONFIG_FILE)
       else: sys.exit(f"UserPreferences.ini not found at {CONFIG_FILE}.")

       if isUsingEspaiAulaFilePath(userPreferences):
              espaiAulaFile = HTML_LocalFile(getEspaiAulaFilePath(userPreferences), DECODE_HTML_FILE)
              fromGroups, fromSubjects, userSubjectsGroups, pGroups, sGroups = extractSubjectsPreferencesFromFile(espaiAulaFile)
       else:
              fromGroups, fromSubjects, userSubjectsGroups, pGroups, sGroups = extractSubjectsPreferences(userPreferences)

       subjectsColors = dict(zip(fromSubjects, [str(x%GOOGLE_CALENDAR_API_MAX_COLORS+1) for x in range(len(fromSubjects))])) # Generating a dictionary[subjectCode] = assignedColor

       basicInformation, timeRange = extractRequestInformation(userPreferences)
       DATA = generateData(fromSubjects, fromGroups, basicInformation)
       fromDate, toDate = int(time.mktime(datetime.datetime.strptime(timeRange[0], "%d/%m/%Y").timetuple())), int(time.mktime(datetime.datetime.strptime(timeRange[1], "%d/%m/%Y").timetuple()))

       if (jsonFile := downloadContent(DATA, fromDate, toDate, fromHeaders=getUserHeaders(CONFIG_FILE))):
              if (n_downloadedSubjects := len(jsonFile)-1) > 0:
                     if not logOutput: print(f"Downloaded {n_downloadedSubjects} subjects blocks.")
                     else: logOutput.appendPlainText(f"Downloaded {n_downloadedSubjects} subjects blocks.")
                     subjectsBlocks = generateBlocks(jsonFile, dict(zip(fromSubjects, zip(userSubjectsGroups, pGroups, sGroups))), n_downloadedSubjects)
                     if not logOutput: print(f"Using {len(subjectsBlocks)} subjects blocks.")
                     else: logOutput.appendPlainText(f"Using {len(subjectsBlocks)} subjects blocks.")
              else:
                     if not logOutput: sys.exit("No subjects blocks have been downloaded, closing program.")
                     else: logOutput.appendPlainText(f"WARNING: No subjects blocks have been downloaded, closing program.")
       else:
              if not logOutput: sys.exit(f"Something went wrong generating blocks, closing program.")
              else: logOutput.appendPlainText(f"ERROR: Something went wrong generating blocks, closing program.")

       MyCalendar = Calendar()

       if deleteMode:
              descriptions = list(map(lambda x: x.getDescription(),subjectsBlocks))
              events = MyCalendar.getEvents()
              for event in events:
                     eventDescription, eventID = event[0], event[1]
                     if eventDescription in descriptions:
                            if not logOutput: print(f"Deleting EventID: {eventID} | {eventDescription}")
                            else: logOutput.appendPlainText(f"Deleting EventID: {eventID} | {eventDescription}")
                            MyCalendar.deleteEvent(eventID)
                     else:
                            if not logOutput: print(f"Skipped EventID: {eventID} | {eventDescription}")
                            else: logOutput.appendPlainText(f"Skipped EventID: {eventID} | {eventDescription}")
              if not logOutput: print("Events Removed!")
              else: logOutput.appendPlainText("Events Removed!")
       else:
              for subject in subjectsBlocks:
                     if not logOutput: print(f"Adding {subject.name} to the calendar.")
                     else: logOutput.appendPlainText(f"Adding {subject.name} to the calendar.")
                     MyCalendar.addEvent(f"{subject.name} ({subject.type[0]})", subject.classroom, subject.getDescription(), subject.start, subject.end, TIMEZONE, colorID=subjectsColors[str(subject.code)])
                     if not logOutput: print(f"{subject.name} added to the calendar.")
                     else: logOutput.appendPlainText(f"{subject.name} added to the calendar.")
              if not logOutput: print("Done!")
              else: logOutput.appendPlainText("Done!")