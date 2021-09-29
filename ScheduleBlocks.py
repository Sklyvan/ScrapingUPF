import time, datetime, html

class SubjectBlock:
    def __init__(self, name, classroom, type, group, code, start, end):
        self.name, self.classroom, self.type = name, classroom, type
        self.group, self.code = group, code
        self.start, self.end = start, end
        # Start time & end time as UNIX Timedate format.
        self.startUnix = time.mktime(datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S").timetuple())
        self.endUnix = time.mktime(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S").timetuple())
        self.start, self.end = self.start.replace(" ", "T"), self.end.replace(" ", "T") # Converting to the Google Calendar API format.

    def __len__(self): return int((self.endUnix - self.startUnix)/(60*60)) # Returning the duration of the class in hours.

    def __str__(self):
        return f"{self.type} {self.name} at {self.classroom} | Group: {self.group} | Code: {self.code} | {self.start} - {self.end}"

def generateBlocks(jsonFile, toRead=False):
    blocks = []
    if not toRead: toRead = len(jsonFile)
    for subject in jsonFile[:toRead]:
        newBlock = SubjectBlock(html.unescape(subject['title']), subject['aula'], html.unescape(subject['tipologia']), subject['grup'], subject['codAsignatura'], subject['start'], subject['end'])
        blocks.append(newBlock)
        print(newBlock)
    return blocks
