from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

import datetime
from schedule import MyEvent, Scheduler
from beautiful_date import *
#tommorow date
tommorow = datetime.date.today() + datetime.timedelta(days=1)
#list of employees
employees = ['ritit.server@gmail.com', 'rititek@gmail.com', 'bartosz.slowik2000@gmail.com']

#dicionary of calendars from every employee
calendars={}
i = 0
for employee in employees:
    path = 'googleAPI/.credentials/user'+str(i)+'_token.pickle'
    gc = GoogleCalendar(credentials_path='googleAPI\.credentials\credentials.json',
                    token_path=path)
    calendars[employee]=gc
    i+=1

#list of events

def cretebeatiful(y,m,d,h,min):
    res = "("
    res+=str(d)+"/"+str(m)+"/"+str(y)+")"
    res+="["+str(h)+":"+str(min)+"]"
    return res

events = {}
for gc in calendars.values():
    for event in gc:
        if event.start.date() == tommorow:
            event.start =  "(18/Dec/2022)[20:00]"
            event.end = "(18/Dec/2022)[21:00]"
            gc.update_event(event)
