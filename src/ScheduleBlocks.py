import time, datetime, html, hashlib

class SubjectBlock:
    def __init__(self, name, classroom, type, group, code, start, end, colorID='1', extraInfo=None):
        """
        This class is used to store the information of a subject block.
        A subject block is a element of the schedule.
        :param name: Name of the subject.
        :param classroom: Classroom where the subject is going to be held.
        :param type: Type of the subject. It can be Seminar, Practice or Theory.
        :param group: Group of the subject class.
        :param code: Subject code.
        :param start: Start time of the subject block.
        :param end: End time of the subject block.
        :param colorID: Color of the block into the calendar.
        :param extraInfo: Extra information about the subject block, sometimes here we have the classroom.
        """
        self.name, self.classroom, self.type = name, classroom, type
        self.group, self.code = group, code
        self.start, self.end = start, end
        # Start time & end time as UNIX Timedate format.
        self.startUnix = time.mktime(datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S").timetuple())
        self.endUnix = time.mktime(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S").timetuple())
        self.start, self.end = self.start.replace(" ", "T"), self.end.replace(" ", "T") # Converting to the Google Calendar API format.
        self.colorID = colorID
        self.extraInfo = extraInfo

        # Subject ID is the Hash of:
        #   Code: Subject code.
        #   Type: Type of the subject, can be a Seminar, Practice or Theory.
        #   Start/End: Start and end time of the subject block.
        self.subjectID = f"{self.code}{self.type}{self.start}{self.end}"
        self.subjectID = html.escape(self.subjectID)
        self.subjectID = hashlib.md5(self.subjectID.encode('utf-8')).hexdigest()

    def getDescription(self): # This description goes to the event description.
        if self.extraInfo is None:
            if self.classroom == 'Online': # In case the class is online, we don't need to show the classroom.
                return f"{self.type}: {self.name} ({self.code}) is {self.classroom} ({self.type[0]}{self.group})"
            else:
                return f"{self.type}: {self.name} ({self.code}) at {self.classroom} ({self.type[0]}{self.group})"
        else:
            if self.classroom == 'Online':
                return f"{self.type}: {self.name} ({self.code}) is {self.classroom} ({self.type[0]}{self.group}) | {self.extraInfo}"
            else:
                return f"{self.type}: {self.name} ({self.code}) at {self.classroom} ({self.type[0]}{self.group}) | {self.extraInfo}"

    def __len__(self): return float((self.endUnix - self.startUnix)/(60*60)) # Returning the duration of the class in hours.

    def __str__(self): # Just for debugging purposes.
        if self.classroom == 'Online':
            return f"{self.type} {self.name} is {self.classroom} | Group: {self.group} | Code: {self.code} | {self.start} - {self.end}"
        else:
            return f"{self.type} {self.name} at {self.classroom} | Group: {self.group} | Code: {self.code} | {self.start} - {self.end}"

def generateBlocks(jsonFile, subjectsGroups, subjectsColors, toRead=False):
    """
    Given a json file and a list of groups, this function
    will generate the blocks of the schedule.
    :param jsonFile: This file contains the subjects information.
    :param subjectsGroups: This list contains the groups of the subjects.
    :param subjectsColors: Dictionary with subjectsColors[subjectCode] = colorID
    :param toRead: I don't understand this parameter and I don't remember why I'm using it :)
    :return: List of SubjectBlocks.
    """
    blocks = []
    if not toRead: toRead = len(jsonFile)
    for subject in jsonFile[:toRead]:
        try:
            mainGroup, pGroup, sGroup = subjectsGroups[str(subject['codAsignatura'])]
            observation = None if subject['observacion'] == ' ' else subject['observacion']
        except KeyError:
            None
        else:
            addBlock = False # This variable is used to know if we need to add the block to the list based on the groups.
            if subject['tipologia'][0] == 'T' and mainGroup == subject['grup']: # Si es una teoria, y el grupo de teorías es el que ha seleccionado el usuario.
                newBlock = SubjectBlock(html.unescape(subject['title']), 'Online' if subject['aula'] == ' ' else subject['aula'],
                                        html.unescape(subject['tipologia']), subject['grup'], subject['codAsignatura'], subject['start'], subject['end'],
                                        extraInfo=observation)
                addBlock = True
            elif subject['tipologia'][0] == 'P' and pGroup == subject['grup']: # Si es una práctica, y el grupo de prácticas es el que ha seleccionado el usuario.
                newBlock = SubjectBlock(html.unescape(subject['title']), 'Online' if subject['aula'] == ' ' else subject['aula'],
                                        html.unescape(subject['tipologia']), subject['grup'], subject['codAsignatura'], subject['start'], subject['end'],
                                        extraInfo=observation)
                addBlock = True
            elif subject['tipologia'][0] == 'S' and sGroup == subject['grup']: # Si es un seminario, y el grupo de seminarios es el que ha seleccionado el usuario.
                newBlock = SubjectBlock(html.unescape(subject['title']), 'Online' if subject['aula'] == ' ' else subject['aula'],
                                        html.unescape(subject['tipologia']), subject['grup'], subject['codAsignatura'], subject['start'], subject['end'],
                                        extraInfo=observation)
                addBlock = True

            if addBlock:
                newBlock.colorID = subjectsColors[newBlock.code]
                blocks.append(newBlock)

    return blocks
