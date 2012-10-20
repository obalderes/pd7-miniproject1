from pymongo import Connection

Connection=Connection('mongo.stuycs.org')
db = Connection.admin
res=db.authenticate('ml7','ml7')
db = Connection['z-pd7-EliHayden']

collection = db.collection1


def addStory(title,story):
    d = {'title':title,'story':story}
    collection.insert(d)

def getTitles(cursor):
    titles = []
    res = cursor.find()
    for i in res:
        titles.append(str(i['title']))

    return titles

x = getTitles(collection)
print x
