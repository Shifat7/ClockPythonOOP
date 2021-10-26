import time

class Counter:

    def __init__(self, name):
        self._Name = name
        self._Count = 0

    # properties
    def getName(self):
        return self._Name

    def setName(self, value):
        self._Name = value

    def getCount(self):
        return self._Count

    # methods
    def increment(self):
        self._Count = self._Count + 1

    def Reset(self):
        self._Count = 0


class Clock:
    def __init__(self):
        self._seconds = Counter("Seconds")
        self._minutes = Counter("Minutes")
        self._hours = Counter("Hours")

    def reset(self):
        self._seconds.Reset()
        self._minutes.Reset()
        self._hours.Reset()

    def read_time(self):
        s = self._seconds.getCount()
        m = self._minutes.getCount()
        h = self._hours.getCount()
        return (f'{h:002}' + ':' + f'{m:002}' + ':' f'{s:002}')

    def tick(self):
        if self._seconds.getCount() != 59:
            self._seconds.increment()
        else:
            self._seconds.Reset()
            if self._minutes.getCount() != 59:
                self._minutes.increment()
            else:
                self._minutes.Reset()
                if self._hours.getCount() != 23:
                    self._hours.increment()
                else:
                    self._seconds.Reset()
                    self._minutes.Reset()
                    self._hours.Reset()




clock = Clock()


def PrintCounters(clock):
    for i in range(86401):
        print(clock.read_time())
        clock.tick()
        time.sleep(1)


PrintCounters(clock)