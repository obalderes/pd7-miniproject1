from pymongo import Connection
Connection = Connection('mongo.stuycs.org')

#to authenticate
db=Connection.admin
res=db.authenticate('ml7','ml7')

#to connect to database
db=Connection['z-pd7']

#to create a collection called stories
stories=db.stories
for stuff in stories.find():
    if "title" in stuff.keys():
        print stuff
'''
I am thinking using a dictionary with keys title and comments to store stories
"title" stores the title of the story in a string
"comments" stores all of the comments in a list
like this:
story={'title':"this is the title",'comments':["this is the first comment!","here is another one.","the third one"]}
'''

#add a story into stories collection by inserting a new dictionary called story
def add_story(title):
    story={'title':title,'comments':[]}
    stories.insert(story)

#delete a story from stories
#problem can arise if there are two stories with the same title
def delete_story(title):
    story=stories.find_one({'title':title})
    stories.remove(story)

#add a comment to the story having a specific title
#problem can arise if there are two stories with the same title
def add_comment(title,comment):
    story=stories.find_one({'title':title})
    story['comments'].append(comment)

#return all story titles in a list
def get_stories():
    titles=[]
    for story in stories.find():
        if "title" in story.keys():
            titles.append(story["title"])
    return titles

#return all comments in a list
def get_comments(title):
    story=stories.find_one({"title":title})
    return story["comments"]







