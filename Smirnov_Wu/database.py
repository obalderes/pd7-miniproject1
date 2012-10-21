from pymongo import Connection

Connection = Connection("mongo.stuycs.org")

def connect():
    db = Connection.admin
    res = db.authenticate("ml7","ml7")
    db = Connection["z-pd7-KurKalva"]
    return db

def newStory(title):
    db = connect()
    collection = db.stories
    newStory = {"title":title, "lines":[]}
    collection.insert(newStory)

def removeAllStories():
    db = connect()
    db.stories.remove()
    
