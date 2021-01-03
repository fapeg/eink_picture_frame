#!/usr/bin/env python3

import feedparser
import os
import time
class color:                # the color definition is just for prettier output on your console. if you're just using this script in a cronjob you can delete that and all the printing directions
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


feed = feedparser.parse("http://www.tagesschau.de/xml/atom/") # define the feed to open
htmldatei = "/home/pi/python_files/html/feed.htm"

feed_entries = feed.entries

with open(htmldatei,"w") as file:
    file.write("<html><head><title>Nachrichten</title><link rel='stylesheet' href='style.css'></head><body><p class='headerfrom'><strong>tagesschau.de vom "+time.strftime("%d.%m.%Y, %H:%M Uhr")+"</strong></p>\n")

for entry in feed.entries[:3]: # you might have to tweak these definitions for your feed of course

    article_title = entry.title
    content = entry.summary

    print (color.DARKCYAN + color.BOLD + "{}".format(article_title) + color.END)
    print(color.GREEN + "{}".format(content)+ color.END + "\n")
    
    with open(htmldatei,"a") as file:
        file.write("<article>\n\t<h2>{}</h2>\n\t<p>{}</p>\n</article>\n\n".format(article_title, content))

with open(htmldatei,"a") as file:
    file.write("</body></html>\n")

