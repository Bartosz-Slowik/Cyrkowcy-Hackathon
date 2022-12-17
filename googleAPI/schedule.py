from typing import List, Set
import datetime

class MyEvent:

    def __init__(self,event, name, desc, attendees: Set[str], length):
        self.event = event
        self.timeStart = event.start

        self.name = name
        self.desc = desc
        self.attendees = attendees
        self.timeStart = 0
        self.length = length
    def __str__(self) -> str:
        s = self.name + " (" + str(self.length) + ")\n"
        for attendee in self.attendees:
            s += "  " + attendee + " "
        return s


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

    
class Schedule:
    def __init__(self) -> None:
        self.concurrents = []
        self.events = []

    def __init__(self, concurrents: List[Concurrent]) -> None:
        self.concurrents = concurrents
        self.events = []
        for concurrent in concurrents:
            for event in concurrent.events:
                self.events.append(event)
        
    def fitConcurent(self, concurrent: Concurrent) -> bool:
        for event in concurrent.events:
            if event in self.events:
                return False
        self.events += concurrent.events
        self.concurrents.append(concurrent)
        return True
    
    def getLength(self):
        return len(self.concurrents)
    


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

    def generateSchedule(self):
        self.allConcurrences = list(self.allConcurrences)
        self.allConcurrences.sort(reverse=True)
        schedule = Schedule([])
        for concurrent in self.allConcurrences:
            schedule.fitConcurent(concurrent)
            if self.isFullSchedule(schedule):
                break
        self.allSchedules.append(schedule)

    def getEvents(self):
        lista = []
        hour = 7
        for concurrency in self.allSchedules[0].concurrents:
            for event in concurrency.events:
                event.timeStart = datetime.time(hour, 0, 0)
                lista.append(event)
            hour += 1
        print(len(lista))
        return lista

    def print1(self):
        for concurrent in self.allConcurrences:
            print("Concurrent: ", end="")
            for event in concurrent.events:
                print(event.name, end=" ")
            print()


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

if __name__ == "__main__":
    e1 = MyEvent("event 1", "ecvev", ("adr", "bart"), 1)
    e2 = MyEvent("event 2", "ecvev", ("adr", "szym"), 1)
    e3 = MyEvent("event 3", "ecvev", ("hub", "wac", "adr"), 1)
    e4 = MyEvent("event 4", "ecvev", ("edward", "wac"), 1)
    e5 = MyEvent("event 5", "ecvev", ("lukasz", "wac", "hubert"), 1)
    e6 = MyEvent("event 6", "ecvev", ("szym", "eustach", "edward"), 1)
    e7 = MyEvent("event 7", "ecvev", ("szym", "wac"), 1)
    e8 = MyEvent("event 8", "ecvev", ("szym", "eustach"), 1)
    e9 = MyEvent("event 9", "ecvev", ("lukasz", "eustach", "szym"), 1)
    e10 = MyEvent("event 10", "ecvev", ("hub", "edward", "szym"), 1)
    testList = [e1, e2, e3, e4, e5, e6, e7, e8]
    scheduler = Scheduler(testList)
    scheduler.generateConcurrent()
    print("----------")
    scheduler.generateSchedule()

    events = scheduler.getEvents()
    for event in events:
        print(event.timeStart)
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