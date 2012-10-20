from pymongo import Connection

Connection=Connection('mongo.stuycs.org')

# to auth                                                                     
db = Connection.admin
res=db.authenticate('ml7','ml7')

# connect to your own database                                                 
db = Connection['z-pd7']                                             

#Collection bzstories holds the storie name and a list of lines
collection = db.bzstories # or db['first_collection']                   


#print story 'name' as a paragraph
def getStory(name):
    story = collection.find_one({'name': name})
    lines = story['lines']
    paragraph = ''' '''
    for line in lines:
        paragraph = paragraph +'\n'+ str(line)
    return paragraph

    
#print last line of story 'name'
def getLastLine(name):
    story = collection.find_one({'name': name})
    lines = story['lines']
    lastline = lines[len(lines) - 1]
    return str(lastline)

#add a new story with the name 'name'
def addStory(name):
    collection.insert({'name': name, 'lines':[]})

#add a new line to story 'name'
def addLine(name, line):
    story = collection.find_one({'name': name})
    lines = story['lines']
    lines.append(line)
    collection.update({'name': name}, {'$set': {'lines': lines}})


#removes story 'name'
def deleteStory(name):
    collection.remove({'name' = name})
    
    
#test add story
# collection.insert({'name': 'Arrg', 'lines': ['this is line one', 'this is a boiring story']})
# collection.insert({'name': 'Odessy', 'lines' :['by Homer', 'this is an interesting story', 'about odysseus']})

# addLine('Arrg', 'this is another line')
# res= collection.find()
# for line in res:
#print line['lines']

print getStory('Arrg')
print getLastLine('Odessy')
