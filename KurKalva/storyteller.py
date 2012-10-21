#!usr/bin/python

#Shreya Kalva & David Kurkovskiy ML7 pd7

from pymongo import Connection

Connection=Connection('mongo.stuycs.org')

db = Connection.admin
res = db.authenticate('ml7', 'ml7')

db = Connection['z-pd7-KurKalva']

kurkalva = db.kurkalva

def addStory(x):
    if (kurkalva.find_one({'title': x}) != []):
        for line in kurkalva.find({'title' : x}):
            removeStory(x)
    d = {'title': str(x), 'lines': []}
    kurkalva.insert(d)

def addLine(x, newLine):
    #res = kurkalva.find_one({'title': x})
    #oldList = res['lines']
    #newList = oldList.append(newLine)
    #kurkalva.update({'title': x}, {'title' : x, 'lines' : newList})
    kurkalva.update({'title' : x}, {'$push' : {'lines' : newLine }})

def removeStory(x):
    kurkalva.remove({'title' : x})
    #kurkalva.remove(x)

def returnStory(x):
    return kurkalva.find_one({'title' : x})

def returnStories():
    titles = []
    results = kurkalva.find()
    for line in results:
        titles.append(line['title'])
    return titles

addStory("This is a new story")
#print db.collection_names()
#print kurkalva.find_one()
#addLine("This is a new story", "and it sounds a little something like this")
#print returnStory("This is a new story")
#addLine("This is a new story", "and it goes a lil somethin like this")
#print returnStory("This is a new story")
#print returnStories()
new_posts = [{'title' : "This is a new title"},
	     {'title' : "This is a title with two lines",
	      'lines' : ["one line", "two lines"]}
             {'title' : "Story with only one line",
	      'lines' : ["lonely line"]}]
kurkalva.insert(new_posts)
returnStories()
	     
