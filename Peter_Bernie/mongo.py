from pymongo import Connection

def connect_init:
    Connection=Connection('mongo.stuycs.org')
    db = Connection.admin
    res=db.authenticate('ml7','ml7')
    db = Connection['z-pd7']
    collection = db.stories
    return collection



def newStory(title,story):
     x = {'title':title,'story':[]}
     stories = connect_init()
     if(stories.find({'title': title}).count() = 0):
         stories.insert(x)
         

def deleteStory(title):
    stories = connect_init()
    if(stories.find({'title': title}).count() != 0):
        stories.remove(stories.find_one({'title':title}))

def addComment(title,comment):
    stories = connect_init()
    if(stories.find({'title': title}).count() != 0):
        x = stories.find_one({'title':title}
        x['comments'].append(comment)
        stories.remove({'title':title})
        stories.insert(x)


def getStories():
                                 
                      
