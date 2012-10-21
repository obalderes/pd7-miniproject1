import pymongo
from pymongo import Connection
import mongo2

mongo2.newStory("New Story")
mongo2.newStory("NEWER STORY")
mongo2.newStory("NEWEST STORY")
mongo2.addComment("New Story","NEW COMMENT")
mongo2.addComment("NEWEST STORY","WHAT")
print "\n"
print mongo2.getStories()
print "\n\n"
print mongo2.getComments("New Story")
print "\n"
print mongo2.getComments("NEWEST STORY")
mongo2.deleteAll()
