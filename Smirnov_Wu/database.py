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
    newstory = {"title":title, "lines":[]}
    collection.insert(newstory)

def removeAllStories():
    db = connect()
    db.stories.remove()

def newLine(name, newline):
    story = collection.find_one({"name": name})
    oldlines = story["lines"]
    oldlines.append(newline)
    collection.update({"name": name}, {"$set": {"lines": oldlines}})

print newStory("yarharhar")



    
    
