#!/home/rokner/anaconda3/envs/fancypaper/bin/python
import praw
import os
import random
import subprocess
import urllib.request
from pathlib import Path

USER_AGENT = 'User-Agent: rokn.github.io.fancypaper:v1.0.0 (by /u/ProgrammerAway)'

subreddits = ['earthporn', 'wallpapers']

reddit = praw.Reddit(user_agent=USER_AGENT)

urls = []
extensions = ('jpg', 'png')
maxUrls = 6

for subreddit in subreddits:
    for submission in reddit.subreddit(subreddit).hot(limit=maxUrls):
        if submission.url.endswith(extensions):
            urls.append(submission.url)

url = random.choice(urls)
_, ext = os.path.splitext(url)

directory = Path(Path.home(), Path(".fancypaper"))
filename = Path(directory, Path("current" + ext))

if not os.path.exists(directory):
    os.makedirs(directory)

urllib.request.urlretrieve(url, filename)

p = subprocess.Popen(['feh', '--bg-scale', filename])
