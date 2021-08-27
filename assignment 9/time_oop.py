class Time:

    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.second = s

    def sum(self, guest):
        result = Time()
        result.hour = self.hour + guest.hour
        result.minute = self.minute + guest.minute
        result.second = self.second + guest.second

        if result.second >= 60:
            result.second -= 60
            result.minute += 1

        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1

        if result.hour >= 23:
            result.hour -= 24

        return result

    def minus(self, guest):
        result = Time()
        result.hour = self.hour - guest.hour
        result.minute = self.minute - guest.minute
        result.second = self.second - guest.second

        if result.minute <= 0:
            result.hour -= 1
            result.minute += 60

        if result.second <= 0:
            result.minute -= 1
            result.second += 60

        return result

    def timetosec(self):
        self.result = ((self.hour*3600)+(self.minute*60)+self.second)
        print(self.result)

    def sectotime(self):
        result = Time()
        while True:
            if self.second >= 3600:
                self.second -= 3600
                result.hour = result.hour+1
            elif self.second >= 60:
                self.second -= 60
                result.minute = result.minute+1
            else:
                result.second = self.second
                break    
        return result

    def show(self):
        print(self.hour, ":", self.minute, ":", self.second)


time1 = Time(8, 35, 48)
time2 = Time(1, 53, 16)
time = Time(0, 0, 30948)

print("The sum of these two hours is: ")
time1.sum(time2).show()
print("The minus of these two hours is: ")
time1.minus(time2).show()
print("The total seconds of time1 is: ")
time1.timetosec()
print("The is full time is: ")
time.sectotime().show()