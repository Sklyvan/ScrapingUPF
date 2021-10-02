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

       PGroups, SGroups = PGroups.split(','), SGroups.split(',')
       Groups = list(set(SubjectsGroups))

       return Groups, SubjectsGroups, PGroups, SGroups

def extractRequestInformation(UserPreferences):
       basicInformation = UserPreferences[UserPreferences.sections()[1]] # Information to generate the DATA request.
       subjectsList = UserPreferences[UserPreferences.sections()[2]]['Asignaturas'].split(',')
       timeRange = tuple(UserPreferences[UserPreferences.sections()[3]].values()) # Tuple which contains fromDate and toDate.
       return basicInformation, subjectsList, timeRange

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
