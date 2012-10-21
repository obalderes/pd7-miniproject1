from pymongo import Connection

Connection=Connection('mongo.stuycs.org')

db=Connection.admin
res=db.authenticte('ml7','ml7')
db=Connection['z-pd7-JackSteven]
