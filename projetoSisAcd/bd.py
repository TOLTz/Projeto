from tinydb import TinyDB

def addData(file, dict):
    new = TinyDB(file, indent=4)
    new.insert(dict)