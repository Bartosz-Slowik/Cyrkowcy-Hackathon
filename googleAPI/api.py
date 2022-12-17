from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr
from schedule import MyEvent, TimeFrame, attendeesOverlaps, fitEvent, scheduleEvents

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
        temp=[]
        if event.attendees==[]:
            temp.append(event.creator.email)
        else:
            for attendee in event.attendees:
                temp.append(attendee.email)
        events[event.event_id] = MyEvent(event , event.summary, event.description, temp, event.end-event.start)
mylist = events.values()
results = scheduleEvents(mylist)
for result in results:
    result.event.start = result.timeStart
    result.event.end = result.timeStart + result.length
    calendars[result.event.creator.email].modify_event(result.event)




