# # # Python Required Libraries & Modules # # #
from NetworkRequests import Request, HTML_LocalFile
from bs4 import BeautifulSoup as BS
import requests, json, sys, os
from ScheduleBlocks import *
from Configuration import *
from GoogleCalendar import Calendar
from Constants import *
import pretty_errors