from typing import List, Set

class MyEvent:
    def __init__(self, name, desc, attendees: Set[str], length):
        self.name = name
        self.desc = desc
        self.attendees = attendees
        self.length = length
    def __str__(self) -> str:
        s = self.name + " (" + str(self.length) + ")\n"
        for attendee in self.attendees:
            s += "  " + attendee + "\n"
        return s

class TimeFrame:
    def __init__(self) -> None:
        self.events = []
    
    def __str__(self) -> str:
        s = "Time frame: \n"
        for event in self.events:
            s += event.__str__()
        return s

def attendeesOverlaps(event1: MyEvent, event2: MyEvent) -> bool:
    return bool(set(event1.attendees) & set(event2.attendees))

def fitEvent(time: TimeFrame, event: MyEvent) -> bool:
    for ev in time.events:
        if attendeesOverlaps(ev, event):
            return False
    time.events.append(event)
    return True

def scheduleEvents(list: List[MyEvent]):
    hours = []
    for event in list:
        fit=False
        for hour in hours:
            if fitEvent(hour, event):
                fit=True
                break
        if fit==False:
            h = TimeFrame()
            h.events.append(event)
            hours.append(h)
    return hours


def printList(a):
    for e in a:
        print(e)

if __name__ == "__main__":
    e1 = MyEvent("event 1", "ecvev", ("adr", "bart"), 1)
    e2 = MyEvent("event 2", "ecvev", ("adr", "szym"), 1)
    e3 = MyEvent("event 3", "ecvev", ("hub", "wac", "adr"), 1)
    e4 = MyEvent("event 4", "ecvev", ("edward", "wac"), 1)
    e5 = MyEvent("event 5", "ecvev", ("lukasz", "wac", "hubert"), 1)
    testList = [e1, e2, e3, e4, e5]
    printList(scheduleEvents(testList))