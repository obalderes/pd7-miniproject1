from pymongo import Connection

def initialize():
    Connection = Connection ('mongo.stuycs.org')
    data = Connection.admin
    res = data.authenticate('ml7','ml7')
    data = Connection['z-pd7-IanDecker']

def createNewTale(name):
    tale = {'Name':name,'Entries':[]}
    data = connect()
    stories = data.stories
    stories.insert(tale)

def getTaleTitles():
    titles = []
    data = connect()
    stories = data.find()
    for temp in stories:
        titles.append(str(temp['Name']))
    return titles    

def addLineToStory(title,entry):
    data = connect()
    stories = data.find()
    for temp in stories:
        if (temp['Name'] == title):
            temp['Entries'].append(entry)
