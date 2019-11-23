import praw
import pandas
import datetime
import numpy as np
import string
from dotenv import load_dotenv
import os
import WordMapper
#import good stuff


BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR,".env"))
#env is in same directory

reddit = praw.Reddit(client_id= os.getenv("ID"), \
                     client_secret= os.getenv("SECRET"), \
                     user_agent=os.getenv("AGENT"), \
                     username= os.getenv("Ze-Spy"), \
                     password= os.getenv("PASS"))
#set up API
#For some reason dotenv doesn't like hyphens in .env values 
#So now everyone knows my username is "Ze-Spy"


#update wordmap
textinput = input("Update WordMap? Y/N:")
if (textinput == "Y" or textinput == "y"):
    WordMapper.mapwordstofile()
    print("New Words Mapped")
else:
    print("Old Map Used")

#load wordmap
WordsToFind = np.load('WordMap.npy',allow_pickle='TRUE').item()

textinput = input("Redditor to check: \n")
redditor = reddit.redditor(textinput)
counter = 0
foundsomething = 0

try:
    if redditor.id:
        print("User Is Valid")    
except:
    print(textinput +" not found")
    exit()
#Check if user is valid

for comment in redditor.comments.new(limit=None):
    counter +=1
    print (str(counter)+"/1000")
    for c in string.punctuation:
        comment.body = comment.body.replace(c,"")
    comment.body = comment.body.lower()
    for word in comment.body.split():
        if word in WordsToFind:
            WordsToFind[word] += 1
            foundsomething = 1

#summerize words found in comment history
if (foundsomething == 1):
    for i in WordsToFind:
        print (i, WordsToFind[i])
else: 
    print (textinput+" is clean")