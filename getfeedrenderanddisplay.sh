#!/bin/bash

CWD='/home/pi/python_files/html' # path to your feeds.py
python3 $CWD/feeds.py
filename='feed.htm' # output name of the html file
chromium-browser  --window-size=600,448 --hide-scrollbars --screenshot=/home/pi/python_files/html/screenshot.png --headless file://$CWD/$filename
/home/pi/python_files/html/image.py /home/pi/python_files/html/screenshot.png
