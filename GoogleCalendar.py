from __future__ import print_function
import datetime
import os.path
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Calendar:
    def __init__(self):
        self.Service = None
        SCOPES = ['https://www.googleapis.com/auth/calendar']
        CREDS = None # Google API Function, generating the current Auth without opening the browser, so cool :).
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                CREDS = pickle.load(token)
        if not CREDS or not CREDS.valid:
            if CREDS and CREDS.expired and CREDS.refresh_token:
                CREDS.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                CREDS = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(CREDS, token)

        service = build('calendar', 'v3', credentials=CREDS)

        self.Service = service

    def addEvent(self, eventName="", eventLocation="", eventDescription="", start="", end="", timeZone="Europe/Madrid", calendarID='primary'):
        """
        :param eventName: Event name, that name is going to appear at Google Calendar GUI.
        :param eventLocation: Event location, Google Maps can use it.
        :param eventDescription: Just text about the event.
        :param start: YYYY-MM-DDTHours:Minutes:Seconds
        :param end: YYYY-MM-DDTHours:Minutes:Seconds
        :param timeZone: TimeZone of the event inside the calendar.
        :param calendarID: ID to detect the subcalendar where you want to add it.
        :return: The event object.
        """

        newEvent = \
        {
            'summary': eventName, 'location': eventLocation, 'description': eventDescription,

            'start':
            {
                'dateTime': start,
                'timeZone': timeZone,
            },
            'end':
            {
                'dateTime': end,
                'timeZone': timeZone,
            },
            "reminders":
            {
                "useDefault": False,
            }

        }

        newEvent = self.Service.events().insert(calendarId=calendarID, body=newEvent).execute()
        return newEvent
