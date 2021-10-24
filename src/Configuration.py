import configparser, os

def getUserHeaders(FILEPATH):
       UserPreferences = configparser.ConfigParser()
       UserPreferences.read(FILEPATH)
       return {"User-Agent": UserPreferences[UserPreferences.sections()[0]]['Headers']}

def getUserPreferences(FILEPATH):
       UserPreferences = configparser.ConfigParser()
       UserPreferences.read(FILEPATH)
       return UserPreferences

def insertUserPreferences(CONFIG_FILEPATH, planEstudio, idiomaPais, trimestre, planDocente, codigoCentro, codigoEstudio, curso):
       UserPreferences = getUserPreferences(CONFIG_FILEPATH)
       BasicInformation = UserPreferences[UserPreferences.sections()[1]]
       BasicInformation['PlanEstudio'] = planEstudio
       BasicInformation['IdiomaPais'] = idiomaPais
       BasicInformation['Trimestre'] = trimestre
       BasicInformation['PlanDocente'] = planDocente
       BasicInformation['CodigoCentro'] = codigoCentro
       BasicInformation['CodigoEstudio'] = codigoEstudio
       BasicInformation['Curso'] = curso

       with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)

def insertFilePath(CONFIG_FILEPATH, filePath):
       UserPreferences = getUserPreferences(CONFIG_FILEPATH)
       Subjects = UserPreferences[UserPreferences.sections()[2]]
       Subjects['EspaiAulaFilePath'] = filePath

       with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)

def insertSubjectPreferences(CONFIG_FILEPATH, toInsert):
       """
       Adds a subject to the .init file, it checks if is the first subject.
       :param CONFIG_FILEPATH: .init file path.
       :param toInsert: Dictionary that contains subject['Code'] as the subject ID, subject['T'] for the theory group,
       subject['S'] and subject['P'] for the seminars and practice groups.
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

       with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)

def clearSubjectsPreferences(CONFIG_FILEPATH):
       UserPreferences = getUserPreferences(CONFIG_FILEPATH)
       SubjectsInformation = UserPreferences[UserPreferences.sections()[2]]

       SubjectsInformation['Asignaturas'] = 'False'
       SubjectsInformation['GruposAsignaturas'] = 'False'
       SubjectsInformation['GruposPracticas'] = 'False'
       SubjectsInformation['GruposSeminarios'] = 'False'

       with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)

def insertTimeRange(CONFIG_FILEPATH, fromDate, toDate):
       UserPreferences = getUserPreferences(CONFIG_FILEPATH)
       Dates = UserPreferences[UserPreferences.sections()[3]]
       Dates['Inicio'], Dates['Final'] = fromDate, toDate

       with open(CONFIG_FILEPATH, 'w') as configurationFile: UserPreferences.write(configurationFile)

def isUsingEspaiAulaFilePath(UserPreferences): return UserPreferences[UserPreferences.sections()[2]]['EspaiAulaFilePath'] != 'False'

def extractSubjectsPreferences(UserPreferences):
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

def getEspaiAulaFilePath(UserPreferences): return UserPreferences[UserPreferences.sections()[2]]['EspaiAulaFilePath']

def getCalendarID(UserPreferences): return UserPreferences[UserPreferences.sections()[4]]['CalendarID']

def extractSubjectsPreferencesFromFile(searchOn):
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
