#!/usr/bin/env python3

from imap_tools import MailBox
import os
import subprocess
import hashlib
from pathlib import Path


savepath = "/home/pi/python_files/mailpics/" # define where the images are being saved
mailliste   = "mailids.txt"                  # define file name of the already read images
mail_lines  = []
my_file = Path(savepath+mailliste)
if my_file.is_file():
    with open(my_file,"r") as f:
        mail_lines = [line.rstrip('\n') for line in f]

pwfile = Path(savepath+"../maillogin.pwd")   # define file with username and password for the mail account
if pwfile.is_file():
	with open(pwfile,"r") as pf:
		pw_lines = [line.rstrip('\n') for line in pf]
	user = pw_lines[0]
	password = pw_lines[1]
else:
	print("Please provide login information in file 'maillogin.pwd'!\nFirst line: jusername\nSecond line: password")  
	quit()

print(mail_lines)

# get all attachments for each email from INBOX folder
with MailBox('imap.gmail.com').login(user, password) as mailbox:
    for msg in mailbox.fetch(reverse=True):
        msghash= hashlib.md5(str(msg.date_str+msg.from_).encode('utf-8')).hexdigest()
        print(msghash, str(msg.from_+msg.date_str).encode('utf-8'))
        if msghash not in mail_lines:
            for att in msg.attachments:
                print("Attachment from "+msg.from_+" received! Sending to picture frame...")
               
                with open(savepath+msghash, 'wb') as f:
                    f.write(att.payload)
                    subprocess.run(["/home/pi/python_files/anyimage.py", savepath+msghash])
                    subprocess.run(["rm", savepath+msghash]) # delete the original attachment file for space saving (it's still in your inbox of course) 
                    mail_lines.append(msghash)

print(mail_lines)
with open(savepath+mailliste,"w") as fl: # save the mail in the 'alredy read list' so that it gets ignored in the next run
    for line in mail_lines:
        fl.write('%s\n' % line)

