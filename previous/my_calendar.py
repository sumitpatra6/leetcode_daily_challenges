class MyCalendar:
    def __init__(self):
        self.timeline = []
    def book(self, start, end):
        if not self.timeline:
            self.timeline.append([start, end])
            return True
        if end <= self.timeline[0][0]:
            self.timeline = [[start, end]] + self.timeline
            return True
        if start>= self.timeline[-1][1]:
            self.timeline.append([start, end])
            return True
        for i in range(1, len(self.timeline)):
            if self.timeline[i-1][1]<= start and self.timeline[i][0]>=end:
                self.timeline = self.timeline[:i] + [[start, end]] + self.timeline[i:]
                return True
        return False


calendar = MyCalendar()
array = [[37,50],[33,50],[4,17],[35,48],[8,25]]
for a in array:
    result = calendar.book(a[0], a[1])
    print(result)





