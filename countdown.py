#!/usr/bin/env python
"""This script compares a list of school bell times with the current time
of the day and shows you the countdown to the next bell in HH:MM:SS"""

import time
import datetime

def main():
    """This it the main function of the script that executes other functions."""
    countdown()


def readfile():
    """Reads a timetable from a file and makes it a list."""
    with open("timetable1") as filecontents:
        timetable_list = filecontents.read().splitlines()
        return timetable_list

def findnextlesson():
    """Iterates over the timetable to find out the start of the next lesson."""
    timetable_today = readfile()
    counter = 0
    for specific_time in timetable_today:
        lesson_time_string = specific_time + str(".000000")
        current_time_string = datetime.datetime.now().time() # get current time, strip the date
        time_formatter_formula = "%H:%M:%S.%f" # idea from here: http://bit.ly/2C3F0Rj
        lesson_time = datetime.datetime.strptime(lesson_time_string, time_formatter_formula)
        current_time = datetime.datetime.strptime(str(current_time_string), time_formatter_formula)
        if lesson_time > current_time:
            return str(lesson_time).split(" ")[1]
        else:
            counter = counter + 1
            if counter == len(timetable_today):
                return timetable_today[0]

def countdown():
    """"Compares the school bell time to the current time."""
    while True:
        lesson_time_string = findnextlesson() + str(".000000")
        current_time_string = datetime.datetime.now().time() # get current time, strip the date
        time_formatter_formula = "%H:%M:%S.%f" # idea from here: http://bit.ly/2C3F0Rj
        lesson_time = datetime.datetime.strptime(lesson_time_string, time_formatter_formula)
        current_time = datetime.datetime.strptime(str(current_time_string), time_formatter_formula)
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
