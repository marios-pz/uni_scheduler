from abc import abstractmethod
from dataclasses import dataclass

import pymongo

import datetime

from time import sleep

from random import randint

from calendar import day_name

from data import (
    USERNAME,
    PASSWORD
)

from pymongo import MongoClient


# Colours
bold = "\033[1m"
endc = "\033[0m" 
okblue = "\033[94m"
okcyan = "\033[96m"
black_t = "1033[30m"
red_t = "\033[31m"
green_t = "\033[32m"
yellow_t = "\033[33m"
blue_t = "\033[34m"
magenta_t = "\033[35m"
cyan_t = "\033[36m"
white_t = "\033[37m"

class Scheduler:

    def __init__(self) -> None:

        self.client = pymongo.MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@cluster0.bl40b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client['semesters']
        self.collection = self.db['temp']
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.day = self.now.day
        self.hour = self.now.hour
        self.minute = self.now.minute
        self.second = self.now.second
        self.wd = day_name[self.now.weekday()]

        self.greek_dict = {
                'Monday': 'Δευτέρα',
                'Tuesday': 'Τρίτη',
                'Wednesday': 'Τετάρτη',
                'Thursday': 'Πέμπτη',
                'Friday': 'Παρασκευή'
            }

    def get_time(self) -> None:
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.day = self.now.day
        self.hour = self.now.hour
        self.minute = self.now.minute
        self.second = self.now.second
        self.wd = day_name[self.now.weekday()]

    def print_status(self) -> None:
        self.get_time()
        print(yellow_t + f"Σήμερα είναι {self.greek_dict[self.wd]} {self.day}/{self.month}/{self.year}")
        print(f"Ώρα {self.hour}:{self.minute}:{self.second}" + endc)

    def grab_data(self) -> None:
        self.print_status()

        if self.wd not in ['Saturday', 'Sunday']:

            lessons = list()

            key_query = str(self.hour)[:2] + '-' + str(self.hour + 1)[:2]            

            for x in self.collection.find():
                for item in x:
                    if item == key_query:
                        lessons.extend(x[key_query][self.wd])
                        break

            print(okcyan + '\nΤι μαθήματα υπάρχουν αυτή την στιγμή?' + endc)
            if len(lessons) == 0:
                print(red_t + 'Κενό' + endc)
            else:
                for lesson in lessons:
                    print( green_t + f'- {lesson}' + endc )
    
        else:
            print( red_t + "\nΕίναι Σαββατοκύριακο συνάδελφε.\n" + green_t + "Καλά να περνάς." + endc)

    def run(self, flags=[]) -> None:
        """
            Main Program
        """

        for item in flags:

            if item == 'help':
                print( yellow_t + """

Execution:
$ python cli.py (-o || -l)

flags:

    help: Εμφανίζει ότι βλέπεται.


    -l: Το πρόγραμμα θα παραμείνει ανοικτό και θα ενημερώνει ανά κάθε 1 ώρα

    -ο: Το πρόγραμμα τρέχει μία φορά


    Καλά να περνάς!

                """ + endc)
                raise SystemExit

            elif item == 'once':
                self.grab_data()

            elif item == 'loop':

                try:
                    while True:
                        self.grab_data()
                        print(yellow_t + '\nΤο πρόγραμμα θα ξανά ενημερώσει σε μία ώρα, \033[31mΜΗΝ\033[0m κλείσετε το πρόγραμμα.' + endc)
                        sleep(3600)
                except KeyboardInterrupt:
                    print(green_t + '\nΤα λέμε!' + endc)

                    
from sys import argv
if __name__ == "__main__":

    flag_list = list()

    for arg in argv[1:]:
        
        if arg == '-help':
            flag_list.append('help')
            break

        elif arg == '-l':
            flag_list.append('loop')
            break

        elif arg == '-o':
            flag_list.append('once')
            break

        elif arg in ['help', 'o', 'l']:
            print(red_t + "Ξέσασες να βάλεις '-' μπροστά στα flags." + endc)

        else:
            print(red_t + f"'{arg}' δεν είναι σωστό flag" + endc)
            raise SystemExit


    app = Scheduler()

    if len(argv[1:]) == 0:
        app.run(flags=['help'])

    elif len(argv[1:]) >= 2:
        print(red_t + "Υπερβολική χρήση flag." + endc)
        raise SystemExit
    else:
        app.run(flags=flag_list)