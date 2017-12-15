#!/usr/bin/env python
"""This script compares a list of school bell times with the current time
of the day and shows you the countdown to the next bell in HH:MM:SS"""

import time
import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def main():
    """This it the main function of the script that executes other functions."""
    while True:
        output = final_countdown_value()
        return output

def final_countdown_value():
    """This function figures out the final output message."""
    weekday = datetime.datetime.today().weekday()
    if weekday == 5 or weekday == 6:
        return "It's weekend, go home!"
    else:
        return countdown()

def pick_the_correct_file():
    """If monday, picks timetable1, if any other weekday, picks timetable2."""
    if datetime.datetime.today().weekday() == 0:
        return "timetable1"
    else:
        return "timetable2"

def read_file():
    """Reads a timetable from a file and makes it a list."""
    with open(pick_the_correct_file()) as file_contents:
        timetable_list = file_contents.read().splitlines()
        return timetable_list

def find_next_lesson():
    """Iterates over the timetable to find out the start of the next lesson."""
    timetable_today = read_file()
    counter = 0
    for specific_time in timetable_today:
        lesson_time_string = specific_time + str(":00")
        current_time_string = str(datetime.datetime.now().time()).split(".")[0]
        time_formatter_formula = "%H:%M:%S" # idea from here: http://bit.ly/2C3F0Rj
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
    lesson_time_string = find_next_lesson() + str(":00")
    current_time_string = str(datetime.datetime.now().time()).split(".")[0]
    time_formatter_formula = "%H:%M:%S" # idea from here: http://bit.ly/2C3F0Rj
    lesson_time = datetime.datetime.strptime(lesson_time_string, time_formatter_formula)
    current_time = datetime.datetime.strptime(str(current_time_string), time_formatter_formula)
    if lesson_time < current_time: # +1 day to avoid negative if the lessons are over for today
        lesson_time = lesson_time + datetime.timedelta(days=1)
    else:
        pass
    delta = lesson_time - current_time
    return str(delta)

if __name__ == "__main__":
    app.run(debug=True)
