from flask import Flask, render_template
from courses import PROGRAM
from time import sleep
from datetime import datetime
from calendar import day_name

app = Flask(__name__)


@app.route('/')
def hello():
    """
        Single page project
    """

    now = datetime.now()
    hour = now.hour
    wd = day_name[now.weekday()]

    if wd not in ['Sunday', 'Sunday']:

        try:
            temp_dict = PROGRAM[f"{str(hour)[:2]}-{str(hour + 1)[:2]}"]
            get_lessons = temp_dict[wd]
        except KeyError:
            get_lessons = ['Καληνύχτα Συνάδελδε, δεν υπάρχουν άλλα μαθήματα.']

        return render_template('main.html', lessons=get_lessons, day=wd)
    else:
        return render_template('main.html', day=wd)


if __name__ == '__main__':
    app.run(debug=True)
