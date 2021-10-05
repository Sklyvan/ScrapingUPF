import time, datetime, html

class SubjectBlock:
    def __init__(self, name, classroom, type, group, code, start, end, colorID='1'):
        self.name, self.classroom, self.type = name, classroom, type
        self.group, self.code = group, code
        self.start, self.end = start, end
        # Start time & end time as UNIX Timedate format.
        self.startUnix = time.mktime(datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S").timetuple())
        self.endUnix = time.mktime(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S").timetuple())
        self.start, self.end = self.start.replace(" ", "T"), self.end.replace(" ", "T") # Converting to the Google Calendar API format.
        self.colorID = colorID

    def getDescription(self): return f"{self.type}: {self.name} ({self.code}) at {self.classroom} ({self.type[0]}{self.group})"

    def __len__(self): return int((self.endUnix - self.startUnix)/(60*60)) # Returning the duration of the class in hours.

    def __str__(self): return f"{self.type} {self.name} at {self.classroom} | Group: {self.group} | Code: {self.code} | {self.start} - {self.end}"

def generateBlocks(jsonFile, subjectsGroups, toRead=False):
    blocks = []
    if not toRead: toRead = len(jsonFile)
    for subject in jsonFile[:toRead]:
        try:
            mainGroup, pGroup, sGroup = subjectsGroups[str(subject['codAsignatura'])]
        except KeyError:
            print("Ignored Block")
        else:
            addBlock = False
            if subject['tipologia'][0] == 'T' and mainGroup == subject['grup']: # Si es una teoria, y el grupo de teorías es el que ha seleccionado el usuario.
                newBlock = SubjectBlock(html.unescape(subject['title']), subject['aula'], html.unescape(subject['tipologia']), subject['grup'], subject['codAsignatura'], subject['start'], subject['end'])
                addBlock = True
            elif subject['tipologia'][0] == 'P' and pGroup == subject['grup']: # Si es una práctica, y el grupo de prácticas es el que ha seleccionado el usuario.
                newBlock = SubjectBlock(html.unescape(subject['title']), subject['aula'], html.unescape(subject['tipologia']), subject['grup'], subject['codAsignatura'], subject['start'], subject['end'])
                addBlock = True
            elif subject['tipologia'][0] == 'S' and sGroup == subject['grup']: # Si es un seminario, y el grupo de seminarios es el que ha seleccionado el usuario.
                newBlock = SubjectBlock(html.unescape(subject['title']), subject['aula'], html.unescape(subject['tipologia']), subject['grup'], subject['codAsignatura'], subject['start'], subject['end'])
                addBlock = True

            if addBlock: blocks.append(newBlock)

    return blocks