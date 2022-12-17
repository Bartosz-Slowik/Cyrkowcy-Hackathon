from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr
from schedule import MyEvent, Scheduler
import datetime
#tommorow date
tommorow = datetime.date.today() + datetime.timedelta(days=1)
#list of employees
employees = ['rititek@gmail.com','ritit.server@gmail.com', 'bartosz.slowik2000@gmail.com']

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
events = {}
for gc in calendars.values():
    for event in gc:
        if event.start.date() == tommorow:
            temp=[]
            if event.attendees==[]:
                temp.append(event.creator.email)
            else:
                for attendee in event.attendees:
                    temp.append(attendee.email)
            diff_in_minutes = (event.end-event.start).total_seconds() / 60
            events[event.event_id] = MyEvent(event , event.id, event.description, temp, diff_in_minutes)
mylist = events.values()
scheduler = Scheduler(list(mylist))
scheduler.generateConcurrent()
results = scheduler.generateSchedule()



for result in results:
    print(result.timeStart)
    newEvent = result.baseEvent
    newEvent.summary = "ZMIENIONE"
    newEvent.start = result.timeStart
    newEvent.end = result.timeEnd
    curgc = calendars[result.baseEvent.creator.email]
    curgc.update_event(newEvent)
    print("LOL")


def cretebeatiful(y,m,d,h,min):
    res = "("
    res+=str(d)+"/"+str(m)+"/"+str(y)+")"
    res+="["+str(h)+":"+str(min)+"]"
    return res
