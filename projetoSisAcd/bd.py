from tinydb import TinyDB

def addData(file, dict):
    new = TinyDB(file, )
    new.insert(dict)