from typing import List, Set
import datetime
#tommorow date
tommorow = datetime.date.today() + datetime.timedelta(days=1)
class MyEvent:
    def __init__(self ,event, name, desc, attendees: Set[str], length):
        self.name = name
        self.baseEvent = event
        self.desc = desc
        self.attendees = attendees
        self.timeStart = 0
        self.timeEnd = 0
        self.length = length
    def __str__(self) -> str:
        s = self.name + " (" + str(self.length) + ")\n"
        for attendee in self.attendees:
            s += "  " + attendee + " "
        return s
    def __lt__(self, other):
         return self.timeStart < other.timeStart


class Concurrent:
    def __init__(self) -> None:
        self.events = []
    
    def __init__(self, events: List[MyEvent]) -> None:
        self.events = events

    def _attendeesOverlaps(self, event1: MyEvent, event2: MyEvent) -> bool:
        return bool(set(event1.attendees) & set(event2.attendees))

    def fitEvent(self, event: MyEvent) -> bool:
        for ev in self.events:
            if self._attendeesOverlaps(ev, event):
                return False
        self.events.append(event)
        return True

    def __hash__(self) -> int:
        return hash(frozenset(self.events))
    
    def __eq__(self, other: object) -> bool:
        return self.__hash__() == other.__hash__()

    def __lt__(self, other):
         return self.getPeopleCount() < other.getPeopleCount()

    def getPeopleCount(self):
        count = 0
        for event in self.events:
            count += len(event.attendees)
        return count

    def haveEvents(self, events):
        for event in events:
            if not event in self.events:
                return False
        return True

    def notHaveEvents(self, events):
        for event in events:
            if event in self.events:
                return False
        return True
        

    
class Schedule:
    def __init__(self, concurrents: List[Concurrent], eventsCount) -> None:
        self.remaining = list(concurrents)
        self.remaining.sort(reverse=True)
        self.concurrents = []
        self.events = set()
        self.eventsCount = eventsCount

    def addConcurent(self, concurrent, time):
        for event in concurrent.events:
            event.timeStart = time
            event.timeEnd = event.timeStart + datetime.timedelta(minutes=event.length)
            self.events.add(event)
        self.concurrents.append(concurrent)
        self.remaining.remove(concurrent)
        
    def getEventsNow(self, timeNow):
        events = []
        for event in self.events:
            if event.timeStart.time() < timeNow.time() and timeNow.time() < event.timeEnd.time():
                events.append(event)
        return events

    def getEventsEnded(self, timeNow):
        events = []
        for event in self.events:
            if timeNow.time() >= event.timeEnd.time():
                events.append(event)
        return events

    def fitNow(self, timeNow):
        events = self.getEventsNow(timeNow)
        ended = self.getEventsEnded(timeNow)
        canFit = []
        for concurrent in self.remaining:
            if concurrent.haveEvents(events) and concurrent.notHaveEvents(ended) and concurrent not in self.concurrents:
                canFit.append(concurrent)
                break
        if len(canFit) > 0:
            self.addConcurent(canFit[0], timeNow)

    def isFull(self):
        return len(self.events) >= self.eventsCount

    def print(self):
        for event in events:
            print(event.startTime)
            
        
    

class Scheduler:
    def __init__(self, events: List[MyEvent]) -> None:
        self.events = events
        self.allConcurrences = set()
        self.eventCount = len(events)

    def _recursiveFindConcurrent(self, previous: List[MyEvent], remaning: List[MyEvent]):
        for event in remaning:
            con = Concurrent(previous.copy())
            if not con.fitEvent(event):
                continue
            self.allConcurrences.add(con)
            rem = remaning.copy()
            rem.remove(event)
            self._recursiveFindConcurrent(con.events, rem)

    def generateConcurrent(self):
        self._recursiveFindConcurrent([], self.events)
        print(len(self.allConcurrences))

    def generateSchedule(self):
        schedule = Schedule(self.allConcurrences, self.eventCount)        
        hour = 7
        minute = 0
        while(True):
            schedule.fitNow(datetime.datetime(tommorow.year, tommorow.month, tommorow.day, hour, minute, 0))
            if schedule.isFull():
                break
            minute += 1
            if minute==60:
                minute=0
                hour+=1
        lista = []
        for event in schedule.events:
            lista.append(event)
        return lista


if __name__ == "__main__":
    e1 = MyEvent("event 1", "ecvev", ("adr", "bart"), 60)
    e2 = MyEvent("event 2", "ecvev", ("adr", "szym"), 30)
    e3 = MyEvent("event 3", "ecvev", ("hub", "wac", "adr"), 30)
    e4 = MyEvent("event 4", "ecvev", ("edward", "wac"), 90)
    e5 = MyEvent("event 5", "ecvev", ("lukasz", "wac", "hubert"), 60)
    e6 = MyEvent("event 6", "ecvev", ("szym", "eustach", "edward"), 15)
    e7 = MyEvent("event 7", "ecvev", ("szym", "wac"), 30)
    e8 = MyEvent("event 8", "ecvev", ("szym", "eustach"), 45)
    e9 = MyEvent("event 9", "ecvev", ("lukasz", "eustach", "szym"), 30)
    e10 = MyEvent("event 10", "ecvev", ("hub", "edward", "szym"), 45)
    testList = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
    scheduler = Scheduler(testList)
    scheduler.generateConcurrent()
    print("----------")
    events = scheduler.generateSchedule()
    events.sort()
    for event in events:
        print(event.name, event.timeStart.time(), event.timeEnd.time())
    #scheduler.printt()







    '''
class Concurrent:
    def __init__(self) -> None:
        self.events = []
    
    def __init__(self, events: List[MyEvent]) -> None:
        self.events = events

    def _attendeesOverlaps(self, event1: MyEvent, event2: MyEvent) -> bool:
        return bool(set(event1.attendees) & set(event2.attendees))

    def fitEvent(self, event: MyEvent) -> bool:
        for ev in self.events:
            if self._attendeesOverlaps(ev, event):
                return False
        self.events.append(event)
        return True

    def __hash__(self) -> int:
        return hash(frozenset(self.events))
    
    def __eq__(self, other: object) -> bool:
        return self.__hash__() == other.__hash__()

    def getPeopleCount(self):
        count = 0
        for event in self.events:
            count += len(event.attendees)
        return count
class Scheduler:
    def __init__(self, events: List[MyEvent]) -> None:
        self.events = events
        self.allConcurrences = set()
        self.allSchedules = []
        self.eventCount = len(events)

    def _recursiveFindConcurrent(self, previous: List[MyEvent], remaning: List[MyEvent]):
        for event in remaning:
            con = Concurrent(previous.copy())
            if not con.fitEvent(event):
                continue
            self.allConcurrences.add(con)
            rem = remaning.copy()
            rem.remove(event)
            self._recursiveFindConcurrent(con.events, rem)

    def generateConcurrent(self):
        self._recursiveFindConcurrent([], self.events)
        print(len(self.allConcurrences))

    def isFullSchedule(self, schedule: Schedule) -> bool:
        return len(schedule.events) >= self.eventCount


    def _recursiveGenerateSchedule(self, previous: List[Concurrent], remaning: List[Concurrent]):
        for concurrent in remaning:
            schedule = Schedule(previous.copy())
            if not schedule.fitConcurent(concurrent):
                continue
            if self.isFullSchedule(schedule):
                self.allSchedules.append(schedule)
                continue
            rem = remaning.copy()
            rem.remove(concurrent)
            self._recursiveGenerateSchedule(schedule.concurrents, rem)

    def generateSchedule(self):
        self._recursiveGenerateSchedule([], self.allConcurrences.copy())
        print(len(self.allSchedules))

        
    def printt(self):
        for schedule in self.allSchedules:
            print("Schedule: +++++++++++++++++++++++++++++++++++++")
            for concurrent in schedule.concurrents:
                print("Concurrent: ", end="")
                for event in concurrent.events:
                    print(event.name, end=" ")
                print()
            print(schedule.getLength())
            print("End:      +++++++++++++++++++++++++++++++++++++")
'''