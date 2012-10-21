from pymongo import Connection
Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['z-pd7']

collection = db.collection1

def newStory(title):
    if collection.find({'title':title}).count() == 0:
        collection.insert({'title':title,'story':''})

def newLine(title,line):
