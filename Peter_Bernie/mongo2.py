from pymongo import Connection

Connection=Connection('mongo.stuycs.org')

def connect_init():
    db = Connection.admin
    res=db.authenticate('ml7','ml7')
    db = Connection['z-pd7-berniepeter']
    collection = db.stories
    return collection



def newStory(title):
     x = {'title':title,'story':[]}
     stories = connect_init()
     if(stories.find({'title': title}).count() == 0):
         stories.insert(x)

def deleteStory(title):
    stories = connect_init()
    if(stories.find({'title': title}).count() != 0):
        stories.remove(stories.find_one({'title':title}))

def addComment(title,comment):
    stories = connect_init()
    if(stories.find({'title': title}).count() != 0):
        x = stories.find_one({'title':title})
        x['story'].append(comment)
        stories.remove({'title':title})
        stories.insert(x)


def getStories():
    stories = connect_init()
    titles = []
    for story in stories.find():
        titles.append(story['title'])
    return titles

def getComments(title):
    stories = connect_init()
    x = stories.find_one({'title':title})
    return x['story']

def deleteAll():
    stories = connect_init()
    for story in stories.find():
        stories.remove(story)
