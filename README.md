# eInk picture frame

What you need:
-------------------

* Run the Pimoroni install script: https://github.com/pimoroni/inky for eInk support on your Pi
* Install feedparser for the atom feed news script
* Install imap_tools for the mail script
* Install ImageMagick for converting the image

Files in this repository:
-------------------------

### Display images by email ###
* **anyimage.py**: Fork of image.py from the examples in Pimoroni repository. Takes an image and automatically converts it to 600x448px which is the exact size the display needs. If you give it a vertical image it centers your image in a white margin. Also copies the most recent picture to the 'recentimage' folder so that you can revert back to the latest picture after displaying the news or other content 
* **getmail.py**: Checks your mail, gets attachment of the mail, sends it to anyimage.py for displaying it. Also creates a unique ID of the mail (generated by the time the message was sent and the sender email) and saves it in a text file so that when the script checks the mail again this email gets ignored, because the attachment was already saved.
* **maillogin.pwd**: Email/username and password in two seperate lines.

### Display an atom feed ###
* **feeds.py**: Get atom feed and create a html file for which is optimized for viewing on the display.
* **style.css**: Style the html file.
* **getfeedrenderanddisplay.sh**: Use headless chromium to take a screenshot of the html file with the right resolution. Display the screenshot on the display.
* **image.py**: The original image file from Pimoroni. I use it to revert back to the latest photo that was being sent to the picture frame after displaying the news for a specific amount of time a few times a day

### Smartphone admin area ###
*Warning: I wouldn't recommend running this on a pi that is reachable over the actual internet since I don't know if I did a good enough job escaping all the user inputs :P I'm running it in my local network, so it's fine..*
* I got a lighttpd running because I use RaspAP in AP-STA mode. I installed it to be able to configure the wifi settings anywhere I go but that's a little complicated to document lol so right now I'm focusing on the admin area
* **start.php**: Display the options to get mail and to display already saved images.
* **selectimage.php**: Show all saved images and display the one the user clicks on on the picture frame
* **wifi.png, pictures.png, mailpicture.png and bootstrap.min.css** not included for licencing reasons but you can get fitting icons on flaticon.com and the bootstrap file on getbootstrap.com
* **091_mod**: You also have to be careful with this file :D You can save it in /etc/sudoers.d/ and it's being added to the sudoers file. That is required because we run some shell commands in the PHP scripts which are being executed under the www-data user (because this users starts the lighttpd server). So I use the workaround and sudo the scripts, for that to be possible I define exceptions which programs the user can run in this file. It might not be a good idea to allow the user www-data access to commands like tee so be careful
