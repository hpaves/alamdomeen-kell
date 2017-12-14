#!/usr/bin/env python
"""This script compares a list of school bell times with the current time
of the day and shows you the countdown to the next bell in HH:MM:SS"""

import time
import datetime

def main():
    """This it the main function of the script that executes other functions."""
#    comparetime()
    readfile()

def readfile():
    """Reads a timetable from a file and makes it a list."""
    with open("timetable1") as filecontents:
        timetable_list = filecontents.read().splitlines()
        print timetable_list

def comparetime():
    """"Compares the school bell time to the current time."""
    while True:
        raw_lesson_time = "8:30:00.000000"
        raw_current_time = datetime.datetime.now().time() # get current time, strip the date
        time_formatter_formula = "%H:%M:%S.%f" # idea from here: http://bit.ly/2C3F0Rj
        lesson_time = datetime.datetime.strptime(raw_lesson_time, time_formatter_formula)
        current_time = datetime.datetime.strptime(str(raw_current_time), time_formatter_formula)
        if lesson_time < current_time: # +1 day to avoid negative if the lessons are over for today
            lesson_time = lesson_time + datetime.timedelta(days=1)
        else:
            pass
        delta = lesson_time - current_time
        print(str(delta).split(".")[0])
        time.sleep(1)

def checkday():
    """If monday, picks timetable1, if any other weekday, picks timetable2,
    if weekend, displays a message that tells people to go home."""

if __name__ == "__main__":
    main()
