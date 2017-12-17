# Countdownpy

This is a "school bell" countdown app that takes HH:MM strings from the timetable files and then displays a countdown on how many HH:MM:SS is left to the next bell. The result is shown in large, legible letters on a HTML page. It also recognizes Friday night and weekend, at which point it will display the "Go home" message.

## Getting Started

### To set up the environment
```
mkdir countdown_container
cd countdown_container
sudo apt install virtualenv -y
virtualenv venv
. venv/bin/activate
git clone https://github.com/hpaves/countdownpy.git
cd countdownpy
pip install Flask
```

### To launch the app
```
python countdown.py
```

### To see the output
Go to [127.0.0.1:5000/](http://127.0.0.1:5000/) and hit F11

### To exit the virtual environment:
```
deactivate
```

## Running the tests

The tests check the basic functionality of time-strings and be run simply with:
```
python test_countdown.py
```

## Deployment

There's no proper deployment procedure at the moment. 

To jury rig the functionality:
- python countdown.py
- go to [127.0.0.1:5000/](http://127.0.0.1:5000/) in a browser
- hit F11

## Where to go next

### Better deployment guidelines
- The current deployment guide is basically a hack, running the app in a dev environment on linux only
- We'd need tutorials on how to deploy this both on LAN (both linux and windows) and on a website

### Add support for days starting on different times
- The app's current behavior is to count towards the beginning of the SAME day when the day is over, not the next day
- So, if days would start on different times, the app would show the wrong time up until the midnight (at which point the correct timetable is chosen)
- This is not an issue with the current timetables, which begin a the same time

### Smarter data
- The app should eventually compare the two adjacent times given to it in the timetable and figure out whether the next bell is for class or recession
- So, any period that is >40 min would be defined as a class, and any period <40 min would be defined as recession

### Exceptions in the data
- Allow defining some specific_time values as special, to display a different message than class or recession 

### Proper HTML/CSS/JS
- The current website display solution is very basic and doesn't follow the best practices

### HTML formatting flexibility
- The app should have different outputs for the informational text and the actual time displayed (they're single output, currently)
- This would allow more flexible HTML formatting, such as having the text and time different size

## Built With

* [Python](https://www.python.org/) - The main language used
* [Flask](http://flask.pocoo.org/) - The web framework used

## Authors

* **Henri Paves** - *Initial work* - [hpaves](https://github.com/hpaves)

## License

This project is licensed under the GNU GPLv3 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Time string comparison credit: https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
* I'm no HTML guru: https://www.brightcherry.co.uk/scribbles/jquery-auto-refresh-div-every-x-seconds/
* Proper explanation of unittests: https://www.youtube.com/watch?v=6tNS--WetLI
