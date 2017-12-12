import time
import datetime

while True:
    rawLessonTime = "18:30:00.000000"
    rawCurrentTime = datetime.datetime.now().time()
    FMT = "%H:%M:%S.%f" # idea from here: https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
    lessonTime = datetime.datetime.strptime(rawLessonTime, FMT)
    currentTime = datetime.datetime.strptime(str(rawCurrentTime), FMT)
    delta = lessonTime - currentTime
    print str(delta).split(".")[0]
    time.sleep(1)