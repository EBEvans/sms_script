#!/usr/bin/python3

import smtplib
import time
    
print("This script uses Gmail and TLS connections for SMTP text messaging.")
print("This script is based on: https://gist.github.com/alexle/1294495")
print("For help with cell numbers: https://mfitzp.io/list-of-email-to-sms-gateways/")

username = input("Gmail Address: ")
password = input("Password: ")

from_ = input("From: ")
print('For "To:" Numbers only, No punctuation, No country code.')
to_ = input("To: ")
message = input("Message (Shorter is better): ")
while len(message) > 140:
    print("You should try a shorter message.")
    message = input("Message (Shorter is better): ")
        
iterations = int(input("How many times to send the message? "))
while iterations > 12:
    print("Please, no more than 12 times.")
    iterations = int(input("How many times to send the message? "))
delay = int(input("How long between messages (in seconds)? "))
while delay > 10800:
    print("Please, no more than 3 hours (10800 seconds)")
    delay = int(input("How long between messages (in seconds)? "))

current_message = 0
if delay < 61:
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(username, password)
    while current_message < iterations:
        server.sendmail(from_, to_, message)
        current_message += 1
        print("Message "+str(current_message)+" of "+str(iterations)+" sent.")
        if current_message < iterations:
            if delay == 60:
                time.sleep(delay - 2)
            else:
                time.sleep(delay)
    server.quit()
elif delay > 60:
    while current_message < iterations:
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login(username, password)
        server.sendmail(from_, to_, message)
        current_message += 1
        print("Message "+str(current_message)+" of "+str(iterations)+" sent.")
        server.quit()
        if current_message < iterations:
            time.sleep(delay)

print("All messages sent")
username = None
password = None
quit()
