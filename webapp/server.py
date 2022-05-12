from flask import Flask, render_template
from time import sleep
from datetime import datetime
from calendar import day_name
from json import load
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import certifi
ca = certifi.where()


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
            client = MongoClient("mongodb+srv://scheduler:macaroni13@cluster0.bl40b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)
            db = client['semesters']
            collection = db['temp']

            lessons = list()

            key_query = str(hour)[:2] + '-' + str(hour + 1)[:2]            

            for x in collection.find():
                for item in x:
                    if item == key_query:
                        lessons.extend(x[key_query][wd])
                        break

            get_lessons = lessons if len(lessons) != 0 else ['Κενό!']

        except KeyError:
            get_lessons = ['Δεν υπάρχουν άλλα μαθήματα.']
        
        except ServerSelectionTimeoutError as SET:
            get_lessons = ['Αδύνατη σύνδεση με την βάση.', SET]  

        return render_template('main.html', lessons=get_lessons, day=wd)
    else:
        return render_template('main.html', day=wd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='99', debug=True)
