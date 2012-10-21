from pymongo import Connection

def connect():
	Connection = Connection ('mongo.stuycs.org')
	db = Connection.admin
	res=db.authenticate('ml7','ml7')
	db = Connection['z-pd7-Cameron_John']
	return db
	
def addStory(title):
        d = {'title':title, 'lines':[]}
        db = connect()
        collection = db.stories     
        collection.insert(d)

<<<<<<< HEAD
def returnAllTitles():
        db = connect()
        titles = []
        stories = db.find()             
        for x in stories
             titles.append(x['title'])
        return titles
             
=======
def addline(title,line):
	db = connect()
	db.titles.update({'title':title}, {'$push': {lines: line} });
>>>>>>> 953f6f854396d64d35f85a34b87132722759b5a6
	
