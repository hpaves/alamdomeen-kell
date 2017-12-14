import time
import datetime

def main():
    while True:
        raw_lesson_time = "8:30:00.000000"
        raw_current_time = datetime.datetime.now().time() # get current time, strip the date
        time_formatter_formula = "%H:%M:%S.%f" # idea from here: http://bit.ly/2C3F0Rj
        lesson_time = datetime.datetime.strptime(raw_lesson_time, time_formatter_formula)
        current_time = datetime.datetime.strptime(str(raw_current_time), time_formatter_formula)
        if lesson_time < current_time: # add one day if the lessons are over for today
            lesson_time = lesson_time + datetime.timedelta(days=1)
        else:
            pass
        delta = lesson_time - current_time
        print str(delta).split(".")[0]
        time.sleep(1)

if __name__ == "__main__":
    main()
