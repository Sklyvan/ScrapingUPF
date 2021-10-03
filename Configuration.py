import configparser

def getUserHeaders(FILEPATH):
       UserPreferences = configparser.ConfigParser()
       UserPreferences.read(FILEPATH)
       return {"User-Agent": UserPreferences[UserPreferences.sections()[0]]['Headers']}

def getUserPreferences(FILEPATH):
       UserPreferences = configparser.ConfigParser()
       UserPreferences.read(FILEPATH)
       return UserPreferences

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
