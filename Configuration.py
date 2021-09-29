import configparser
FILEPATH = "UserPreferences.ini"

UserPreferences = configparser.ConfigParser()
UserPreferences.read(FILEPATH)
BasicInformation = UserPreferences[UserPreferences.sections()[1]]
Subjects, SubjectsGroups = UserPreferences[UserPreferences.sections()[2]]['Asignaturas'], UserPreferences[UserPreferences.sections()[2]]['GruposAsignaturas']
Subjects, SubjectsGroups = Subjects.split(','), SubjectsGroups.split(',')
Groups = list(set(SubjectsGroups))

print(Subjects, SubjectsGroups, Groups)

DATA = f"planEstudio={BasicInformation['PlanEstudio']}" \
       f"&idiomaPais={BasicInformation['IdiomaPais']}" \
       f"&trimestre=T/{BasicInformation['Trimestre']}" \
       f"&planDocente={BasicInformation['PlanDocente']}" \
       f"&centro={BasicInformation['CodigoCentro']}" \
       f"&estudio={BasicInformation['CodigoEstudio']}" \
       f"&curso={BasicInformation['Curso']}" \
       f"&grupo1=1" \
       f"&grupo2=2" \
       "&asignatura24303=24303" \
       "&asignatura24304=24304" \
       "&asignatura24306=24306" \
       "&asignatura26003=26003"
