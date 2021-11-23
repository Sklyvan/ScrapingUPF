from Imports import *

def extractRND(fromSoup):
       """
       Extracts the RND number from the soup.
       Whats the RND number?
       The RND number is a random number generated by the UPF server,
       you need it download any content from the server, so first of
       all we go to URL_RND and then to URL_JSON to get the jSON file.
       :param fromSoup: BeautifulSoup object, contains the page with the RND number.
       :return: The RND value.
       """
       javaScriptCode = str(fromSoup.findAll('script', type='text/javascript')[4]) # The number is inside a javascript function.
       initialPosition = javaScriptCode.find('selecionarRangoHorarios?rnd=') + len('selecionarRangoHorarios?rnd=')  # Obtaining the first position of the RND number.
       RND = javaScriptCode[initialPosition:initialPosition + 6].replace("'", "").replace(" ", "")
       try:
              float(RND) # I do this to check if the RND is a number.
       except ValueError:
              if not logOutput: sys.exit("Something went pretty wrong while searching the RND value. "
                                         "This is probably caused by wrong UserPreferences.ini data.")
              else: logOutput.addLogInformation("ERROR:Something went pretty wrong while searching the RND value. "
                                              "This is probably caused by wrong UserPreferences.ini data.")
              return False
       else: return RND

def downloadContent(fromData, fromDate, toDate, fromHeaders=''):
       """
       Downloads the content from the server.
       :param fromData: UserPreferences data
       :param fromDate: Initial date.
       :param toDate: Final date.
       :param fromHeaders: User headers, better to leave it empty.
       :return: The extracted JSON file.
       """
       jsonFile = False

       try:
              if not logOutput: print("Establishing session.")
              else: logOutput.addLogInformation("Establishing session.")
              SESSION = Request(URL, fromHeaders, requests.Session(), requestMethod='GET').SESSION
       except Exception as ErrorCode:
              if not logOutput: sys.exit(f"Something went wrong while generating session. {ErrorCode}")
              else: logOutput.addLogInformation(f"ERROR: Something went wrong while generating session. {ErrorCode}")
              return False
       if not logOutput: print("Session successfully established.")
       else: logOutput.addLogInformation("Session successfully established.")

       try:
              if not logOutput: print("Searching for RND number.")
              else: logOutput.addLogInformation("Searching for RND number.")
              soupRND = Request(URL_RND, fromHeaders, SESSION, requestMethod='POST', postData=fromData).Soup
       except Exception as ErrorCode:
              if not logOutput: sys.exit(f"Something went wrong while connecting to search RND number. {ErrorCode}")
              else: logOutput.addLogInformation(f"ERROR: Something went wrong while connecting to search RND number. {ErrorCode}")
              return False
       RND = extractRND(soupRND)
       timeRND = f'rnd={RND}&start={fromDate}&end={toDate}'
       if not logOutput: print("RND Number found.")
       else: logOutput.addLogInformation("RND Number found.")

       try:
              if not logOutput: print("Downloading the content.")
              else: logOutput.addLogInformation("Downloading the content.")
              contentRequest = Request(URL_JSON, fromHeaders, SESSION, requestMethod='POST', postData=timeRND)
       except Exception as ErrorCode:
              if not logOutput: sys.exit(f"Something went wrong while obtaining the request content. {ErrorCode}")
              else: logOutput.addLogInformation(f"ERROR: Something went wrong while obtaining the request content. {ErrorCode}")
              return False
       jsonFile = contentRequest.getJSON(exportFile=True)
       if not logOutput: print("Content downloaded, JSON file saved.")
       else: logOutput.addLogInformation("Content downloaded, JSON file saved.")

       return jsonFile

def deleteGeneratedEvents(MyCalendar, subjectsBlocks, calendarID, logMessages=None):
       """
       Witth this function we delete all the events that were generated by the program.
       :param MyCalendar: Google Calendar object from which we delete the events.
       :param subjectsBlocks: List of subjects to be removed.
       :param calendarID: Calendar ID from which we delete the events.
       :param logMessages: File where we're going to save the log messages, if it's None, the output goes to stdout.
       :return: True if everything went well, False otherwise.
       """
       try:
              descriptions = list(map(lambda x: x.getDescription(), subjectsBlocks))
              events = MyCalendar.getEvents()
       except Exception as ErrorCode:
              if not logOuput:
                     print(f"Something went wrong while extrating the current calendar events, "
                           f"that's possible caused by a Google Calendar API error. "
                           f"{ErrorCode}")
                     return False
              else:
                     logOutput.addLogInformation(f"Something went wrong while extrating the current calendar events, "
                                               f"that's possible caused by a Google Calendar API error. "
                                               f"{ErrorCode}")
                     return False

       for event in events:
              eventDescription, eventID = event[0], event[1]
              if eventDescription in descriptions:
                     if not logOutput:
                            print(f"Deleting EventID: {eventID} | {eventDescription}")
                     else:
                            logOutput.addLogInformation(f"Deleting EventID: {eventID} | {eventDescription}")

                     try:
                            MyCalendar.deleteEvent(eventID, calendarID=calendarID)
                     except Exception as ErrorCode:
                            print(f"Something went wrong while deleting an event, that can be caused by some problems with Google Calendar API. "
                                  f"{ErrorCode}")
                            return False
              else:
                     if not logOutput:
                            print(f"Skipped EventID: {eventID} | {eventDescription}")
                     else:
                            logOutput.addLogInformation(f"Skipped EventID: {eventID} | {eventDescription}")

       if not logOutput: print("Events Removed!")
       else: logOutput.addLogInformation("Events Removed!")
       return True

def addGeneratedEvents(MyCalendar, subjectsBlocks, calendarID, subjectsColors, logMessages=None):
       """
       With this function we're going to add the generated events to the Google Calendar.
       :param MyCalendar: That's the Google Calendar object were we're adding the events.
       :param subjectsBlocks: List of subjects that we are going to add to the Google Calendar.
       :param calendarID: The ID of the Google Calendar where we're going to add the events.
       :param subjectsColors: Dictionary with the subjects and their colors.
       :param logMessages: File where we're going to save the log messages, if it's None, the output goes to stdout.
       :return: True in case of success, False in case of error.
       """
       for subject in subjectsBlocks:
              if not logOutput:
                     print(f"Adding {subject.name} to the calendar.")
              else:
                     logOutput.addLogInformation(f"Adding {subject.name} to the calendar.")
              try:
                     MyCalendar.addEvent(f"{subject.name} ({subject.type[0]})", subject.classroom, subject.getDescription(),
                                         subject.start, subject.end, TIMEZONE, colorID=subjectsColors[str(subject.code)],
                                         calendarID=calendarID)
              except Exception as ErrorCode:
                     if not logOutput:
                            print(f"Something went wrong while adding subject {subject.getDescription()} to calendar, that can be caused by a wrong CalendarID "
                                  f"or a Google Calendar API problem. {ErrorCode}")
                            return False
                     else:
                            logOutput.addLogInformation(f"Something went wrong while adding subject {subject.getDescription()} to calendar, "
                                                      f"that can be caused by a wrong CalendarID or a Google Calendar API problem. {ErrorCode}")
                            return False
              else:
                     if not logOutput:
                            print(f"{subject.name} added to the calendar.")
                     else:
                            logOutput.addLogInformation(f"{subject.name} added to the calendar.")
       if not logOutput: print("Done!")
       else: logOutput.addLogInformation("Done!")
       return True

def RunApplication(deleteMode=False, logMessages=None, replaceMode=True):
       """
       This function is the main function of the application,
       it's going to read the configuration file, then it's going to generate the events.
       After generating the events, it's going to add them to the Google Calendar.
       :param deleteMode: If this is true, the function will delete the events from the Google Calendar.
       :param logMessages: File where we're going to save the log messages, if it's None, the output goes to stdout.
       :param replaceMode: If this is true, the function will replace the events in the Google Calendar.
       :return: None
       """
       global logOutput # That's necessary to make the GUI able to use the log messages.
       logOutput = logMessages

       # Checking the Python version, in this case we're going to use Python 3.8 or higher, since I'm using the Walrus Operator.
       if sys.version_info.major < PYTHON_VERSION['Major'] or (sys.version_info.major >= PYTHON_VERSION['Major'] and sys.version_info.minor < PYTHON_VERSION['Minor']):
              sys.exit(f"You're using Python {sys.version_info.major}.{sys.version_info.minor}, required version is 3.8 or bigger.")

       # Checking if the configuration file exists, if it exists, we're going to read it.
       if os.path.isfile(CONFIG_FILE): userPreferences = getUserPreferences(CONFIG_FILE)
       else: sys.exit(f"UserPreferences.ini not found at {CONFIG_FILE}.")


       if isUsingEspaiAulaFilePath(userPreferences): # If the user is using the automatic mode, we're going to read the HTML file with user data.
              espaiAulaFile = HTML_LocalFile(getEspaiAulaFilePath(userPreferences), DECODE_HTML_FILE)
              fromGroups, fromSubjects, userSubjectsGroups, pGroups, sGroups = extractSubjectsPreferencesFromFile(espaiAulaFile)
       else: # If the user is using the manual mode, we're going to read the user groups and subjects from the user preferences file.
              fromGroups, fromSubjects, userSubjectsGroups, pGroups, sGroups = extractSubjectsPreferences(userPreferences)

       subjectsColors = dict(zip(fromSubjects, [str(x%GOOGLE_CALENDAR_API_MAX_COLORS+1) for x in range(len(fromSubjects))])) # Generating a dictionary[subjectCode] = assignedColor

       # Extracting the time information.
       basicInformation, timeRange = extractRequestInformation(userPreferences)
       DATA = generateData(fromSubjects, fromGroups, basicInformation)
       fromDate = int(time.mktime(datetime.datetime.strptime(timeRange[0], "%d/%m/%Y").timetuple()))
       toDate = int(time.mktime(datetime.datetime.strptime(timeRange[1], "%d/%m/%Y").timetuple()))

       """
       At this point, we have all the user data and we checked if it's correct.
       Now, we're going to access the UPF website to extract the schedule information.
       """
       if (jsonFile := downloadContent(DATA, fromDate, toDate, fromHeaders=getUserHeaders(CONFIG_FILE))):
              if (n_downloadedSubjects := len(jsonFile)-1) > 0: # If we have downloaded at least one subject, we're going to process them.
                     if not logOutput: print(f"Downloaded {n_downloadedSubjects} subjects blocks.")
                     else: logOutput.addLogInformation(f"Downloaded {n_downloadedSubjects} subjects blocks.")
                     subjectsBlocks = generateBlocks(jsonFile, dict(zip(fromSubjects, zip(userSubjectsGroups, pGroups, sGroups))), n_downloadedSubjects)
                     if not logOutput: print(f"Using {len(subjectsBlocks)} subjects blocks.")
                     else: logOutput.addLogInformation(f"Using {len(subjectsBlocks)} subjects blocks.")
              else:
                     if not logOutput: sys.exit("No subjects blocks have been downloaded, closing program.")
                     else: logOutput.addLogInformation(f"WARNING: No subjects blocks have been downloaded, closing program.")
       else:
              if not logOutput: sys.exit(f"Something went wrong generating blocks, closing program.")
              else: logOutput.addLogInformation(f"ERROR: Something went wrong generating blocks, closing program.")

       MyCalendar = Calendar()
       calendarID = getCalendarID(userPreferences)

       # Now, with all the information downloaded, we're going to work with Google Calendar API.
       if replaceMode: # In this case, we're deleting all the events in the calendar and then adding the new ones.
              deleteGeneratedEvents(MyCalendar, subjectsBlocks, calendarID)
              addGeneratedEvents(MyCalendar, subjectsBlocks, calendarID, subjectsColors)
       else:
              if deleteMode: # Just deleting events.
                     deleteGeneratedEvents(MyCalendar, subjectsBlocks, calendarID)
              else: # Just adding events.
                     addGeneratedEvents(MyCalendar, subjectsBlocks, calendarID, subjectsColors)
