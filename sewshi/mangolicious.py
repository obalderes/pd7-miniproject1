from pymongo import Connection

db = connection('mongo.stuycs.org')

# to auth
db = connection.admin
res=db.authenticate('ml7','ml7')

#connect to your own database
db = Connection['z-pd7']

collection = db.first_collection

#btw shan i didn't actually do anything
