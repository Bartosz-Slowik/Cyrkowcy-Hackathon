from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr
from schedule import MyEvent, Scheduler
import datetime
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
            events[event.event_id] = MyEvent(event , event.id, event.description, temp, (event.end-event.start))
mylist = events.values()
scheduler = Scheduler(list(mylist))
scheduler.generateConcurrent()
scheduler.generateSchedule()
results = scheduler.getEvents()


for result in results:
    newEvent = result.baseEvent
    newEvent.summary = "JAJO"

    curgc = calendars[result.baseEvent.creator.email]
    curgc.update_event(newEvent)
    print("LOL")


def cretebeatiful(y,m,d,h,min):
    res = "("
    res+=str(d)+"/"+str(m)+"/"+str(y)+")"
    res+="["+str(h)+":"+str(min)+"]"
    return res
