import configparser

def getUserHeaders(FILEPATH):
       UserPreferences = configparser.ConfigParser()
       UserPreferences.read(FILEPATH)
       return {"User-Agent": UserPreferences[UserPreferences.sections()[0]]['Headers']}

def extractConfig(FILEPATH):
       UserPreferences = configparser.ConfigParser()
       UserPreferences.read(FILEPATH)
       BasicInformation = UserPreferences[UserPreferences.sections()[1]]
       Subjects, SubjectsGroups = UserPreferences[UserPreferences.sections()[2]]['Asignaturas'], UserPreferences[UserPreferences.sections()[2]]['GruposAsignaturas']
       Subjects, SubjectsGroups = Subjects.split(','), SubjectsGroups.split(',')
       Groups = list(set(SubjectsGroups))
       timeRange = tuple(UserPreferences[UserPreferences.sections()[3]].values())
       return Subjects, SubjectsGroups, Groups, BasicInformation, timeRange

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