from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, SU, SA

from beautiful_date import Jan, Apr
gc = GoogleCalendar(credentials_path='googleAPI\.credentials\credentials.json')

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

for event in gc:
    print(event.start)
    print(event.end)
    print(event.summary)
    #print(event.description)
    #print(event.location)
    print(event.attendees)
    #print(event.minutes_before_email_reminder)