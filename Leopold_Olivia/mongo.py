from pymongo import Connection




def connection():
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate('ml7', 'ml7')
    db = connection['z-pd7-LO']
    return db

def chooseStory(title):
    return title

def newStory(title):
    db = connection()
    db.stories.save({title: title, lines: []})

#adds a new line to an already existing story
def addLine(title, line):
    db = connection()
    lines = db.find({title:title})
    lines.append(line)
entry = 
    db.stores.update({title: title}, {lines: lines})


def printLines(title):
    db = connection()
    print db.scores.find({title: title})

