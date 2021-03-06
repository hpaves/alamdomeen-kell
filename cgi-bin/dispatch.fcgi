#!/usr/bin/env python3.5

from __future__ import print_function
import os, sys

DOMAIN = "melliste.ee" # Teie domeeni nimi (ilma www.-ta)
PREFIX = "/www/apache/domains/www.%s" % (DOMAIN,)

# Add a custom Python path.
sys.path.insert(0, os.path.join(PREFIX, ".virtualenvs/flask-website/lib/python3.5/site-packages/"))

from flup.server.fcgi import WSGIServer
from flask import Flask
import time
import datetime

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
                    <title>Kellani</title>
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
    if weekday == 5 or weekday == 6 or lessons_are_over():
        return "Mine koju"
    return "Kellani " + str(countdown(current_time_w_seconds(), find_next_lesson()))

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

def current_time_w_seconds():
    """Finds the current system time in HH:MM:SS"""
    ct_output = str(datetime.datetime.now().time()).split(".")[0]
    return ct_output

def second_input_larger(current_time_string, other_string):
    """Takes two inputs -- HH:MM:SS, HH:MM -- and tells whether the second is larger."""
    other_string = other_string + str(":00")
    time_formatter_formula = "%H:%M:%S" # idea from here: http://bit.ly/2C3F0Rj
    other_time = datetime.datetime.strptime(other_string, time_formatter_formula)
    current_time = datetime.datetime.strptime(str(current_time_string), time_formatter_formula)
    if other_time < current_time:
        return False
    return True

def lessons_are_over():
    """Determines if the lessons are over for today."""
    lessons_are_over = second_input_larger(current_time_w_seconds(), find_next_lesson()) is False
    if lessons_are_over:
        return True

def find_next_lesson():
    """Iterates over the timetable to find out the start of the next lesson."""
    timetable_today = read_file()
    counter = 0
    for specific_time in timetable_today:
        if second_input_larger(current_time_w_seconds(), specific_time):
            return specific_time
        else:
            counter = counter + 1
            if counter == len(timetable_today):
                return timetable_today[0]

def countdown(current_time_argument, next_lesson_argument):
    """Compares the school bell time to the current time."""
    next_lesson_argument_w_seconds = next_lesson_argument + str(":00")
    time_formatter_formula = "%H:%M:%S" # idea from here: http://bit.ly/2C3F0Rj
    lesson_time = datetime.datetime.strptime(next_lesson_argument_w_seconds, time_formatter_formula)
    current_time = datetime.datetime.strptime(str(current_time_argument), time_formatter_formula)
    if lesson_time < current_time: # +1 day to avoid negative if the lessons are over for today
        lesson_time = lesson_time + datetime.timedelta(days=1)
    else:
        pass
    delta = lesson_time - current_time
    time.sleep(1)
    return str(delta)

class ScriptNameStripper(object):
   def __init__(self, app):
       self.app = app

   def __call__(self, environ, start_response):
       environ['SCRIPT_NAME'] = ''
       return self.app(environ, start_response)

app = ScriptNameStripper(app)

if __name__ == '__main__':
    WSGIServer(app).run()

