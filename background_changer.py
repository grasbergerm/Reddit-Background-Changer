import urllib
import praw
import subprocess
import random
import os

f = open('top_image.jpg','wb')
user_agent = ("image grab")
r = praw.Reddit(user_agent=user_agent)
user_name = "GrasbergerM"
for submission in r.get_subreddit('carporn').get_top(limit=5):
    link = submission.url
    if random.randint(0,5) == 3:
        break
if link[len(link)-4:len(link):1] != ".jpg":
    link += ".jpg"
f.write(urllib.urlopen(link).read())
f.close()

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to "%s" as POSIX file
end tell
END"""

def set_desktop_background(filename):
    subprocess.Popen(SCRIPT%filename, shell=True)
set_desktop_background('/Users/grasbergerm/Projects/Reddit Background Changer/top_image.jpg')
process_name = "Dock"
os.system('pkill '+ process_name)
