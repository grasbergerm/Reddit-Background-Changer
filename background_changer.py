import urllib
import praw
import subprocess
import random
import os

f = open('top_earth.jpg','wb')
user_agent = ("Top of Earth Porn Grab Bot"
              )
r = praw.Reddit(user_agent=user_agent)
thing_limit = 10
user_name = "GrasbergerM"
for submission in r.get_subreddit('earthporn').get_top(limit=5):
    link = submission.url
    if random.randint(0,5) == 3:
        break
f.write(urllib.urlopen(link+".jpg").read())
f.close()

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def set_desktop_background(filename):
    subprocess.Popen(SCRIPT%filename, shell=True)
set_desktop_background('/Users/grasbergerm/Desktop/top_earth.jpg')
process_name = "Dock"
os.system('pkill '+ process_name)
