from abc import abstractmethod
from dataclasses import dataclass

import pymongo

import datetime

import gc

from time import sleep

from random import randint


from calendar import day_name

from .courses import (
    PORT,
    SEMESTERS, 
    PROGRAM,
    IP,
    PASSWORD,
    USERNAME,
    PASSWORD
)

from .database import (
    create_tmp_clt, 
    get_db
)

class Scheduler:
    
    def __init__(self) -> None:
        self.db = self.create_table()
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.day = self.now.day
        self.hour = self.now.hour
        self.minute = self.now.minute
        self.second = self.now.second
        self.wd = day_name[self.now.weekday()]
        
    @classmethod
    def create_table(self) -> pymongo.collection.Collection:
        """
            Troll feature
            
            Friendly tip, dont bother deleting the duplicate collections, just close the docker app 🧠
        """
        try:
            database_name = 'temp_data'
            database = get_db(f'mongodb://{USERNAME}:{PASSWORD}@{IP}:{PORT}', database_name)
            collection = create_tmp_clt(database)
            collection.insert_many(SEMESTERS)

        except pymongo.errors.BulkWriteError:
            # print("Collection duplicate found, creating a clone.")
            database_name = f'temp_data{randint(0,128)}'
            database = get_db(f'mongodb://{USERNAME}:{PASSWORD}@{IP}:{PORT}', database_name)
            collection = create_tmp_clt(database)
            collection.insert_many(SEMESTERS)
            
        # print(collection.find_one())
        return collection
            

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
        # self.wd = 'Monday' # Debugging
        print(f"Σήμερα είναι {self.wd} {self.day}/{self.month}/{self.year}")
        
    
    def grab_lesson(self) -> None:
        
        if self.wd not in ['Saturday', 'Sunday']:
            
            temp_dict = PROGRAM[f"{str(self.hour)[:2]}-{str(self.hour + 1)[:2]}"]
            
            get_lessons = temp_dict[self.wd]
            
            print('Τι μαθήματα υπάρχουν αυτοί την στιγμή: ')
            
            for lesson in get_lessons:
                print(f"  - {lesson}") 
    
            # Constant is THICC, save user's memory.
            del temp_dict
            gc.collect()
            gc.collect()
            
        else:
            print("Είναι Σαββατοκύριακο χαζούλη")
        
        
    def run(self) -> None:
        """
            Main Program
        """
        while True:
            self.print_status()
            self.grab_lesson()
            sleep(3600)