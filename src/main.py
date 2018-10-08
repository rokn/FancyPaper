#!/home/rokner/anaconda3/envs/fancypaper/bin/python
import praw
import os
import random
import subprocess
import urllib.request
from pathlib import Path

CLIENT_ID='sEaKhcj7acvm1w'
CLIENT_SECRET='szUCnRpN87urPDc-fOcPLddqxR0'

USER_AGENT = 'User-Agent: rokn.github.io.fancypaper:v1.0.0 (by /u/ProgrammerAway)'

subreddits = ['earthporn', 'wallpapers']

directory = Path(Path.home(), Path(".fancypaper"))
defFilename = Path(directory, Path("current.jpg"))

def setWallpaper(file):
    subprocess.Popen(['feh', '--bg-scale', file])

setWallpaper(defFilename)

reddit = praw.Reddit(user_agent=USER_AGENT, client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

urls = []
extensions = ('jpg', 'png')
maxUrls = 6

for subreddit in subreddits:
    for submission in reddit.subreddit(subreddit).hot(limit=maxUrls):
        if submission.url.endswith(extensions):
            urls.append(submission.url)

url = random.choice(urls)
_, ext = os.path.splitext(url)

filename = Path(directory, Path("current" + ext))

if not os.path.exists(directory):
    os.makedirs(directory)

urllib.request.urlretrieve(url, filename)

setWallpaper(filename)
