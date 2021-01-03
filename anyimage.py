#!/usr/bin/env python3

import sys
import subprocess
import os
import time
from PIL import Image
from inky.inky_uc8159 import Inky

inky = Inky()
saturation = 0.5

timestamp=str(int(time.time()))

if len(sys.argv) == 1:
    print("""
Usage: {file} image-file
""".format(file=sys.argv[0]))
    sys.exit(1)

imageargument = sys.argv[1]

newimage=imageargument+'-'+timestamp+'.jpg'

os.system('convert -resize 600x448 -auto-orient '+imageargument+' -gravity center -background white -extent 600x448 '+newimage) # this uses imagemagick to create a 600x448px image which is ready to be sent to the picture frame

image = Image.open(newimage)

if len(sys.argv) > 2:
    saturation = float(sys.argv[2])

inky.set_image(image, saturation=saturation)
inky.show()
os.system('cp '+newimage+ ' /home/pi/python_files/recentimage/recent.jpg') # copy the file to the recentimage folder. I do that to be able to revert back to the latest image after displaying the current news for a limited time period
