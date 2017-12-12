import time
import datetime

while True:
    rawLessonTime = "8:30:00.000000"
    rawCurrentTime = datetime.datetime.now().time() # get current time, strip the date
    FMT = "%H:%M:%S.%f" # idea from here: https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
    lessonTime = datetime.datetime.strptime(rawLessonTime, FMT) # make string back to datetime
    currentTime = datetime.datetime.strptime(str(rawCurrentTime), FMT) # convert stripped time to string, and then back to datetime
    if lessonTime < currentTime:
        lessonTime = lessonTime + datetime.timedelta(days=1) # add one day to the lessonTime if the lessons are over for today
    else:
        pass
    delta = lessonTime - currentTime
    print str(delta).split(".")[0]
    time.sleep(1)