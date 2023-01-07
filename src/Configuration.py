import configparser, os
from Constants import DECODE_HTML_FILE
from NetworkRequests import HTML_LocalFile

# This file contains the functions to read and write the configuration file.

def getUserHeaders(FILEPATH):
       """
       Returns the headers used to generate the POST/GET requests.
       :param FILEPATH: UserPreferences file path where the headers are stored.
       :return: The dictionary with the headers.
       """
       UserPreferences = configparser.ConfigParser()
       UserPreferences.read(FILEPATH, encoding=DECODE_HTML_FILE)
       return {"User-Agent": UserPreferences[UserPreferences.sections()[0]]['Headers']}

def getUserPreferences(FILEPATH):
       """
       Returns a ConfigParser object with the user preferences.
       :param FILEPATH: UserPreferences file path.
       :return: ConfigParser object with the user preferences.
       """
       UserPreferences = configparser.ConfigParser()
       UserPreferences.read(FILEPATH, encoding=DECODE_HTML_FILE)
       return UserPreferences

def insertUserPreferences(CONFIG_FILEPATH, planEstudio, idiomaPais, trimestre, planDocente, codigoCentro, codigoEstudio, curso):
       """
       Inserts the user preferences into the UserPreferences.ini file.
       :param CONFIG_FILEPATH: File path of the UserPreferences.ini file.
       :param planEstudio: Identifier of the plan of study. (Integer)
       :param idiomaPais: The subjects are going to be added in the selected language. (en.GB, es.ES, ca.ES)
       :param trimestre: Number of the trimestre. (1, 2, 3)
       :param planDocente: Year of the plan of study. (Integer)
       :param codigoCentro: Identifier of the center. (Integer)
       :param codigoEstudio: Identifier of the study. (Integer)
       :param curso: Main subjects course number. (1, 2, 3, 4)
       :return: True if the preferences were inserted, False otherwise.
       """
       UserPreferences = getUserPreferences(CONFIG_FILEPATH)
       BasicInformation = UserPreferences[UserPreferences.sections()[1]]
       BasicInformation['PlanEstudio'] = planEstudio
       BasicInformation['IdiomaPais'] = idiomaPais
       BasicInformation['Trimestre'] = trimestre
       BasicInformation['PlanDocente'] = planDocente
       BasicInformation['CodigoCentro'] = codigoCentro
       BasicInformation['CodigoEstudio'] = codigoEstudio
       BasicInformation['Curso'] = curso

       try:
              with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)
       except Exception as ErrorCode:
              print(f"Something went wrong while inserting user preferences into the file. {ErrorCode}")
              return False
       else:
              return True

def insertFilePath(CONFIG_FILEPATH, filePath):
       """
       Inserts the file path of the Groups.html file into the UserPreferences.ini file.
       :param CONFIG_FILEPATH: Path of the UserPreferences.ini file.
       :param filePath: HTML file path.
       :return: True if the file path was inserted, False otherwise.
       """
       UserPreferences = getUserPreferences(CONFIG_FILEPATH)
       Subjects = UserPreferences[UserPreferences.sections()[2]]
       Subjects['EspaiAulaFilePath'] = filePath

       try:
              with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)
       except Exception as ErrorCode:
              print(f"Someting went wrong while inserting the HTML file path intro the UserPreferences.ini file. {ErrorCode}")
              return False
       else:
              return True

def insertSubjectPreferences(CONFIG_FILEPATH, toInsert):
       """
       Adds a subject to the .init file, it checks if is the first subject.
       :param CONFIG_FILEPATH: .init file path.
       :param toInsert: Dictionary that contains subject['Code'] as the subject ID, subject['T']
       for the theory group, subject['S'] and subject['P'] for the seminars and practice groups.
       :return: True if the subject information was inserted, False otherwise.
       """
       UserPreferences = getUserPreferences(CONFIG_FILEPATH)
       SubjectsInformation = UserPreferences[UserPreferences.sections()[2]]

       if SubjectsInformation['Asignaturas'].lower() != 'false':
              SubjectsInformation['Asignaturas'] = SubjectsInformation['Asignaturas'] + ',' + toInsert['Code']
              SubjectsInformation['GruposAsignaturas'] = SubjectsInformation['GruposAsignaturas'] + ',' + toInsert['T']
              SubjectsInformation['GruposPracticas'] = SubjectsInformation['GruposPracticas'] + ',' + toInsert['P']
              SubjectsInformation['GruposSeminarios'] = SubjectsInformation['GruposSeminarios'] + ',' + toInsert['S']
       else:
              SubjectsInformation['Asignaturas'] = toInsert['Code']
              SubjectsInformation['GruposAsignaturas'] = toInsert['T']
              SubjectsInformation['GruposPracticas'] = toInsert['P']
              SubjectsInformation['GruposSeminarios'] = toInsert['S']

       try:
              with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)
       except Exception as ErrorCode:
              print(f"Something went wrong while inserting the subject information into the file. {ErrorCode}")
              return False
       else:
              return True

def clearSubjectsPreferences(CONFIG_FILEPATH):
       """
       Removes all the subjects information from the .ini file.
       :param CONFIG_FILEPATH: File path of the UserPreferences.ini file.
       :return: True if the subjects information was removed, False otherwise.
       """
       UserPreferences = getUserPreferences(CONFIG_FILEPATH)
       SubjectsInformation = UserPreferences[UserPreferences.sections()[2]]

       SubjectsInformation['Asignaturas'] = 'False'
       SubjectsInformation['GruposAsignaturas'] = 'False'
       SubjectsInformation['GruposPracticas'] = 'False'
       SubjectsInformation['GruposSeminarios'] = 'False'

       try:
              with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)
       except Exception as ErrorCode:
              print(f"Something went wrong while removing the subjects information from the file. {ErrorCode}")
              return False
       else:
              return True

def insertTimeRange(CONFIG_FILEPATH, fromDate, toDate):
       """
       Inserting the initial and final date of the subjects.
       :param CONFIG_FILEPATH: File path of the UserPreferences.ini file.
       :param fromDate: Initial date of the subjects.
       :param toDate: Final date of the subjects.
       :return: True if the date were inserted, False otherwise.
       """
       UserPreferences = getUserPreferences(CONFIG_FILEPATH)
       Dates = UserPreferences[UserPreferences.sections()[3]]
       Dates['Inicio'], Dates['Final'] = fromDate, toDate

       try:
              with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)
       except Exception as ErrorCode:
              print(f"Something went wrong while inserting the date information into the file. {ErrorCode}")
              return False
       else:
              return True

def isUsingEspaiAulaFilePath(UserPreferences):
       # Function to check if the user is using the automatic mode.
       return UserPreferences[UserPreferences.sections()[2]]['EspaiAulaFilePath'] != 'False'

def extractSubjectsPreferences(UserPreferences): # Reads the subjects information from the .ini file.
       SubjectsGroups = UserPreferences[UserPreferences.sections()[2]]['GruposAsignaturas'].split(',')
       PGroups, SGroups = UserPreferences[UserPreferences.sections()[2]]['GruposPracticas'], UserPreferences[UserPreferences.sections()[2]]['GruposSeminarios']
       subjectsList = UserPreferences[UserPreferences.sections()[2]]['Asignaturas'].split(',')
       PGroups, SGroups = PGroups.split(','), SGroups.split(',')
       Groups = list(set(SubjectsGroups))

       return Groups, subjectsList, SubjectsGroups, PGroups, SGroups

def extractRequestInformation(UserPreferences):
       basicInformation = UserPreferences[UserPreferences.sections()[1]] # Information to generate the DATA request.
       timeRange = tuple(UserPreferences[UserPreferences.sections()[3]].values()) # Tuple which contains fromDate and toDate.
       return basicInformation, timeRange

def getEspaiAulaFilePath(UserPreferences):
       espaiAulaFilePath = UserPreferences[UserPreferences.sections()[2]]['EspaiAulaFilePath']
       if not os.path.isfile(espaiAulaFilePath): print(f"WARNING! It looks like the HTML file with subjects information does not exist at {espaiAulaFilePath}")
       return espaiAulaFilePath

def getCalendarID(UserPreferences): return UserPreferences[UserPreferences.sections()[4]]['CalendarID']

def getColorList(UserPreferences): return UserPreferences[UserPreferences.sections()[4]]['SubjectsColors'].split(',')

def extractSubjectsPreferencesFromFile(searchOn):
       """
       Extracts the subjects information from the .ini file.
       :param searchOn: BeautifulSoup object with the server answer.
       :return: Tuples with the subjects information.
       """
       contentList = searchOn.findAllContent('td', 'lletrab')
       contentList = [x for x in contentList if x != '..'] # Removing some trash data.
       Groups, SubjectsGroups, PGroups, SGroups = set(), [], [], []
       subjectsList = []
       i = 0
       while i < (len(contentList)-1):
              if contentList[i+1][0] == 'P' and contentList[i+2][0] == 'S':
                     subject, practice, seminar = contentList[i], contentList[i+1], contentList[i+2]
                     separatorPosition = subject.find('-')
                     subjectCode, subjectGroup = subject[0:separatorPosition], subject[separatorPosition+1:separatorPosition+2]
                     practiceGroup, seminarGroup = practice[practice.find('-')+1:], seminar[seminar.find('-')+1:]
                     Groups.add(subjectGroup)
                     SubjectsGroups.append(subjectGroup)
                     PGroups.append(practiceGroup)
                     SGroups.append(seminarGroup)
                     subjectsList.append(subjectCode)
                     i += 2
              elif contentList[i+1][0] == 'S':
                     subject, seminar = contentList[i], contentList[i + 1]
                     separatorPosition = subject.find('-')
                     subjectCode, subjectGroup = subject[0:separatorPosition], subject[separatorPosition + 1:separatorPosition + 2]
                     seminarGroup = seminar[seminar.find('-') + 1:]
                     Groups.add(subjectGroup)
                     SubjectsGroups.append(subjectGroup)
                     PGroups.append('-1')
                     SGroups.append(seminarGroup)
                     subjectsList.append(subjectCode)
                     i += 1
              elif contentList[i+1][0] == 'P':
                     subject, practice = contentList[i], contentList[i + 1]
                     separatorPosition = subject.find('-')
                     subjectCode, subjectGroup = subject[0:separatorPosition], subject[separatorPosition + 1:separatorPosition + 2]
                     practiceGroup = practice[practice.find('-') + 1:]
                     Groups.add(subjectGroup)
                     SubjectsGroups.append(subjectGroup)
                     PGroups.append(practiceGroup)
                     SGroups.append('-1')
                     subjectsList.append(subjectCode)
                     i += 1
              i += 1
       return list(Groups), subjectsList, SubjectsGroups, PGroups, SGroups

def generateData(fromSubjects, fromGroups, BasicInformation):
       """
       Generating the request data in POST/GET structure.
       :param fromSubjects: List of subjects codes.
       :param fromGroups: List of theory groups for every subject.
       :param BasicInformation: Main information to generate the request.
       :return: POST/GET request data.
       """
       DATA = f"planEstudio={BasicInformation['PlanEstudio']}" \
              f"&idiomaPais={BasicInformation['IdiomaPais']}" \
              f"&trimestre=T/{BasicInformation['Trimestre']}" \
              f"&planDocente={BasicInformation['PlanDocente']}" \
              f"&centro={BasicInformation['CodigoCentro']}" \
              f"&estudio={BasicInformation['CodigoEstudio']}" \
              f"&curso={BasicInformation['Curso']}" \

       for group in fromGroups: DATA += f"&grupo{group}={group}"
       for subject in fromSubjects: DATA += f"&asignatura{subject}={subject}"

       return DATA

def checkEspaiAulaFileIntegrity(filePath):
       """
       This function recieves the HTML file with the subject information
       from the AulaGlobal website and checks if the file is valid.
       :param filePath: HTML file path.
       :return: The score of the file.
       """
       if os.path.exists(filePath):
              try: espaiAulaFile = HTML_LocalFile(filePath, DECODE_HTML_FILE)
              except: return 50

              try: extractSubjectsPreferencesFromFile(espaiAulaFile)
              except: return 75

              return 100
       return 25
