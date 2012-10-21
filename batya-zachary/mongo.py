from pymongo import Connection

def smartprint(mongodata):
    for entry in mongodata:
        del entry['_id']
        print entry

def conn():
    """
    Makes a connection and returns the database.
    This will make it easier for us to run each method.
    """
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate('ml7','ml7')
    db = connection['z-pd7-ZZ']
    return db  

#########################################################

def addStory(title):
    """
    Adds a new story title.
    Gives an empty list for lines.
    """
    db = conn()
    d = {'title':title, 'lines':[]}
    db.stories.insert(d)

def getStoryNames():
    """
    Returns all the story titles.
    """
    db = conn()
    d = db.stories.find()
    l = [x['title'] for x in d]
    return l

def addLine(story, line):
    """
    Adds a line to the story.
    Appends the line to the list of lines.
    If the story doesn't exist the method returns without doing anything.
    """
    db = conn()
    d = [x for x in db.stories.find({'title':story})]
    if len(d) == 0:
        return
    d = d[0]
    li = d['lines']
    li.append(line)
    db.stories.update({'title':story},d)

from pymongo import Connection

def smartprint(mongodata):
    for entry in mongodata:
        del entry['_id']
        print entry

def conn():
    connection = Connection('mongo.stuycs.org')
    db = connection.admin
    res = db.authenticate('ml7','ml7')
    db = connection['z-pd7-ZZ']
    return db  

#########################################################

def addStory(title):
    db = conn()
    d = {'title':title, 'lines':[]}
    db.stories.insert(d)

def getStoryNames():
    db = conn()
    d = db.stories.find()
    l = [x['title'] for x in d]
    return l

def addLine(story, line):
    db = conn()
    d = [x for x in db.stories.find({'title':story})]
    if len(d) == 0:
        return
    d = d[0]
    li = d['lines']
    li.append(line)
    db.stories.update({'title':story},d)


addLine("dd", "argh")
