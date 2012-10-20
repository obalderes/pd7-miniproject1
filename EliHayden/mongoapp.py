from pymongo import Connection

Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['z-pd7-EliHayden']

collection = db.collection1




#Routine to add a story
##may be completely incorrect
story1 = []
d = {'storyname': 'Story Numero 1','story': story1}
collection.insert(d)

##Add a line to an already created story
line2add = 'blah blah blah'
searchfor = 'Story Numero 1'
res = collection.find()
for line in res:
    if line['storyname']== searchfor
        storytmp = 'story' + line2add 
        'story' = storytmp
