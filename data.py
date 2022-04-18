import json

USERNAME = "admin"
PASSWORD = "password"
IP = "localhost"
PORT = 27017

with open('./general_db.json', 'r') as f:
    PROGRAM = json.load(f)
