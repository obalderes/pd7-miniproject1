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

addStory("This is a new story")
print db.collection_names()
