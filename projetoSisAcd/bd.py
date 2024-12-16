from tinydb import TinyDB

db = TinyDB('database.json')

def addData(args):
    db.insert(args)