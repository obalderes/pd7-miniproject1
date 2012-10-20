from pymongo import Connection

connection = Connection('mongo.stuycs.org')

def auth():
    db = connection.admin
    res = db.authenticate('ml7','ml7')

#connects to db
def initiate():
    auth()
    db = connection['peng_zeng-pd7']

#adds a new story with title 'title'; returns False if duplicate story
def add_story(title):
    db = connection['peng_zeng-pd7']
    collection = db.stories
    res = get_story_names() #prevents creation of stories with same title
    if(title in res):
        return False
    else:
        collection.insert({'title':title
                           , 'story':['no']})
#returns all story names
def get_story_names():
    db = connection['peng_zeng-pd7']
    collection = db.stories
    ans = []
    collection = collection.find()
    for x in collection:
        ans.append(x['title'])
    return ans

#add a new line to story; assumes story with 'title' exists
def add_to_story(title,line):
    db = connection['peng_zeng-pd7']
    collection = db.stories
    story = collection.find_one({'title':title}) #cursor
    body = story['story']
    body.append(str(line))
    collection.update({'title':title}, {'$set':{'story':body}})

#tests
initiate()
add_story('hello world')
add_story('banana boat')
add_story('keel')
add_to_story('keel','nooo')
cur = connection['peng_zeng-pd7'].stories.find_one({'title':'keel'})
print cur
