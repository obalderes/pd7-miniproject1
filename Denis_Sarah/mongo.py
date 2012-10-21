#!usr/bin/python

from pymongo import Connection


def connect():
    """ Handles connecting to mongo.stuycs.org, authentication, and connecting to our (Denis's/Sarah's) database. Returns our database.
    """
    Connection = Connection('mongo.stuycs.org')
    db = Connection.admin
    res = db.authenticate('ml7','ml7')
    db = Connection['Denis_Sarah']
    return db


def addStory(title):
    """ Given a title, adds a new story to database 
    """
    db = connect()
    collection = db.stories
    story = {'title': title, 'lines': []}
    collection.insert(story)



def addLineToStory(title,line):
    """ Given a title and a line, adds the line to the story with that title.
    """
    db = connect()
    collection = db.stories
    db.stories.update( {'title': title}, {"$push": {"lines": line}});



def removeStory(title):
    """ Given a title, removes a story from the database
    """
    db = connect()
    collection = db.stories
    collection.remove(title)

 
def returnStory(title):
    """ Given a title, returns the story
    """
    db = connect()
    collection = db.stories
    return collection.find({"title" : title})

def returnTitles():
    db = connect()
    collection = db.stories
    print "Story Titles: "
    for c in collection:
        print find({} , {fields: "title"})
        print ", "
        
