#This is an exercise for class() only!
#Do not use it as a date object,just import datetime or other plugin

class Date():
    def isvalid(self): #invoker
        if (1 <= self.year <= 3000) and (1 <= self.month <= 12):
            daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 30, 31, 30, 31]
        if isleap(self.year) == True:
            daysInMonth[1] = 29
        if 1 <= self.day <= daysInMonth[self.month - 1]:
            return True
        return False
    def tostr(self):
        return str(self.year) + "/" + str(self.month) + "/" + str(self.day)

def isleap(year):
    if year % 400 == 0:
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False

def strdate(birthday): #birthday is a yyyymmdd string
    d = Date()
    year, month, day = birthday.split("/")
    d.year = int(year)
    d.month = int(month)
    d.day = int(day)
    return d

def printdict(bdDict):
    for p in bdDict.keys():
        b = bdDict[p] #b is the Date object
        print(p + " " + b.tostr())

bdDict = dict()
while True:
    name = input("name: ")
    if(name == ""):
        break

    birthday = input("birthday (yyyy/mm/dd): ")
    birthday = strdate(birthday) #now is a Date object

    if birthday.isvalid() == True:
        bdDict[name] = birthday
    else:
        print("bad date!")

    if birthday == "":
        break
printdict(bdDict)
