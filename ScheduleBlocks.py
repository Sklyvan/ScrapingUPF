import time, datetime

class SubjectBlock:
    def __init__(self, name, classroom, type, group, code, start, end):
        self.name, self.classroom, self.type = name, classroom, type
        self.group, self.code = group, code
        self.start, self.end = start, end
        # Start time & end time as UNIX Timedate format.
        self.startUnix = time.mktime(datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S").timetuple())
        self.endUnix = time.mktime(datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S").timetuple())

    def __len__(self): return int((self.endUnix - self.startUnix)/(60*60)) # Returning the duration of the class in hours.

    def __str__(self): return "Hay que implementar esto para la gente que quiera programar sobre mi código :)"