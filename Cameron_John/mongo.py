from pymongo import Connection

def connect():
	Connection = Connection ('mongo.stuycs.org')
	db = Connection.admin
	res=db.authenticate('ml7','ml7')
	db = Connection['z-pd7-Cameron_John']
	return db
	
def addStory(title):
        d = {'title':title, 'lines:[]}
        db = connect()
        db.insert(d)
             
	
