#!usr/bin/python

#Shreya Kalva & David Kurkovskiy ML7 pd7

from pymongo import Connection

Connection=Connection('mongo.stuycs.org')

db = Connection.admin
res = db.authenticate('ml7', 'ml7')

db = Connection['z-pd7-KurKalva']

kurkalva = db.kurkalva

def addStory(x):
    d = {'title': str(x), 'lines': []}
    kurkalva.insert(d)

def addLine(x, newLine):
    res = kurkalva.find_one({'title': x})
    oldList = res['lines']
    newList = oldList.append(newLine)
    kurkalva.update({'title': x}, {'title' : x, 'lines' : newList})

def removeStory(x):
    kurkalva.remove({'title' : x})

addStory("This is a new story")
#print db.collection_names()
#print kurkalva.find_one()
#addLine("This is a new story", "and it sounds a little something like this")
print kurkalva.find_one({'title': "This is a new story"})
removeStory("This is a new story")
print kurkalva.find_one({'title': "This is a new story"})
