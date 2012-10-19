from pymongo import Connection

def smartprint(mongodata):
    for entry in mongodata:
        del entry['_id']
        print entry

Connection = Connection('mongo.stuycs.org')
db = Connection.admin
res = db.authenticate('ml7','ml7')
db = Connection['z-pd7-zachary']

#########################################################

db.test.
db.test.insert({'name':'fred'})

smartprint(db.test.find())
