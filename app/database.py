from pymongo import MongoClient
import certifi
ca = certifi.where()

def get_db(db_link, db_name):
    """
        Searches for X database else it creates one
        db_link: mongodb link with credentials
        db_name: name of the database
    """
    client = MongoClient(db_link, tlsCAFile=ca)
    return client[db_name]


def create_tmp_clt(db):
    """
        creates a dummie collection on the database that has been passed
    """
    return db['temp']

