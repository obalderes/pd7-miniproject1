from pymongo import Connection
from bson.objectid import ObjectId

def smartprint(mongodata):
    """
    Prints the database without the IDs.
    """
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

def clearDB():
    """
    Removes all entries from the database.
    """
    db = conn()
    db.stories.remove()


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
    l = [str(x['title']) for x in d]
    return l

def getStoryIDs():
    """
    Returns all the story IDs.
    """
    db = conn()
    d = db.stories.find()
    l = [x['_id'] for x in d]
    return l

def addLine(story, line):
    """
    Adds a line to the story, given the story's title.
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

def addLineByID(storyID, line):
    """
    Adds a line to the story, given the story's ID
    Appends the line to the list of lines.
    If the story doesn't exist the method returns without doing anything.
    """
    db = conn()
    d = [x for x in db.stories.find({'_id':storyID})]
    if len(d) == 0:
        return
    d = d[0]
    li = d['lines']
    li.append(line)
    db.stories.update({'_id':storyID},d)

def storyText(story):
    """
    Prints the contents of a story, for debugging purposes.
    Returns if the story is not found.
    """
    db = conn()
    d = [x for x in db.stories.find({'title':story})]
    if len(d) == 0:
        return
    d = d[0]
    print d['title']
    for line in d['lines']:
        print line

if __name__ == '__main__':
    clearDB()
    addStory("new title")
    name = getStoryNames()[0]
    print "NAME: " + name
    id = getStoryIDs()[0]
    print "ID: " + str(id)
    addLine(name,"first line")
    addLineByID(id,"second line")
    storyText(name)
