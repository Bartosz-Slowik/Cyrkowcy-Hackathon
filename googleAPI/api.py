from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr

calendars=[]
for i in range(0,3):
    path = 'googleAPI/.credentials/user'+str(i)+'_token.pickle'
    gc = GoogleCalendar(credentials_path='googleAPI\.credentials\credentials.json',
                    token_path=path)
    calendars.append(gc)
#calendar = GoogleCalendar('ritit.server@gmail.com')

class MyEvent:
    def __init__(self, name, desc, attendees, length):
        self.name = name
        self.desc = desc
        self.attendees = attendees
        self.length = length
    

event = Event(
    'Breakfast',
    start=(1 / Jan / 2022)[9:00],
    recurrence=[
        Recurrence.rule(freq=DAILY),
        Recurrence.exclude_rule(by_week_day=[SU, SA]),
        Recurrence.exclude_times([
            (19 / Apr / 2023)[9:00],
            (22 / Apr / 2023)[9:00]
        ])
    ],
    minutes_before_email_reminder=50
)

#calendar.add_event(event)

class MyEvent:
    def __init__(self, name, desc, attendees, length):
        self.name = name
        self.desc = desc
        self.attendees = attendees
        self.length = length

events = {}
for gc in calendars:
    for event in gc:
        temp=[]
        if event.attendees==[]:
            temp.append(event.creator.email)
        else:
            for attendee in event.attendees:
                temp.append(attendee.email)
        events[event.event_id] = MyEvent(event.summary, event.description, temp, event.end-event.start)


print(events)
'''
for gc in calendars:
    for event in gc:
        print(event.attendees)
        print(event.creator.email)
        print(event.event_id)
        print(event.start)
        print(event.end)

'''


