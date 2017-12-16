#!/usr/bin/env python
"""This script compares a list of school bell times with the current time
of the day and shows you the countdown to the next bell in HH:MM:SS"""

from __future__ import print_function
import time
import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Dislpays the main function output in HTML."""
    # https://www.brightcherry.co.uk/scribbles/jquery-auto-refresh-div-every-x-seconds/
    return """
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>countdown.py</title>
                    <script src="http://code.jquery.com/jquery-latest.js"></script>
                    <script>
                        $(document).ready(function() {
                            $("#container").load("main.php");
                        var refreshId = setInterval(function() {
                            $("#container").load("main.php");
                        }, 1000);
                        $.ajaxSetup({ cache: false });
                        });
                    </script>
                    <style type="text/css">
                        html, body {
                        width: 100%;
                        margin: 0;
                        padding: 0;
                        }
                        #container {
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        font-size: 30vmin;
                        text-align: center;
                        }
                    </style>
                </head>
                <body>
                    <h1><div id="container"></div></h1>
                </body>
            </html>
            """

@app.route("/main.php")
def main():
    """This it the main function of the script that executes other functions."""
    while True:
        output = final_countdown_value()
        return output

def final_countdown_value():
    """This function figures out the final output message."""
    weekday = datetime.datetime.today().weekday()
    if weekday == 1 or weekday == 2:
        return "Go home"
    return "Bell in " + str(countdown())

def pick_the_correct_file():
    """If monday, picks timetable1, if any other weekday, picks timetable2."""
    if datetime.datetime.today().weekday() == 0:
        return "timetable1"
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
            return specific_time
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
    time.sleep(1)
    return str(delta)

if __name__ == "__main__":
    app.run(debug=True)
