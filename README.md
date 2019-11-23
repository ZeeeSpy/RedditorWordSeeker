# Reddit Word Seeker

This lets you use the Reddits API to crawl through the past 1000 comments of any redditor and find out if they used a given word. 

Loosely based off the nwordcountbot, but with the ability to find any words. as of writing this this script can only be run locally, with the end goal being a bot that responds to @'s with word requests.

### How to use
- Go here https://www.reddit.com/prefs/apps/
- Create a new app, remember the name, app secret and personal secret.
- edit DOTenv to your app name, secret etc.
- rename DOTenv to .env 
- Add words to wordstofind.txt each word should be on a new line
- Run RedditWordFinder.py with python3. 

You'll need a reddit account, python and the following libraries; PRAW, PANDAS, numpy, dotenv. Just use "pip3 install LIBRARYNAME" to get them. 

If your reddit username has a hyphen in it like "Ze-Spy" for example, you'll have to manually add it into RedditWordFinder.py

so instead of it being
username= os.getenv("USER"), \
it should 
username= "YOUR USERNAME HERE", \