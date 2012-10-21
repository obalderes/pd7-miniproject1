from pymongo import Connection
Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['z-pd7']

collection = db.collection1

def newStory(title):
    if collection.find({'title':title}).count() == 0:
        collection.insert({'title':title,'story':[]})

def returnStory(title):
    story = collection.find_one({'title':title})
    return story

def newLine(title,line):
    storyTitle = collection.find_one({'title':title})
    paragraph = storyTitle['story']
    paragraph.append(line)
    collection.update({'title':title},{'$set': {'story':paragraph}})
def removeStory(title):
    collection.remove({'title':title})
if __name__ == '__main__':
    newStory('The YanYan')
    newLine('The YanYan','HELLO')
    newLine('The YanYan','BYE')
    print returnStory('The YanYan')
