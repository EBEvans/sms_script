#!/usr/bin/python3

import smtplib
import time
    
print("This script uses Gmail for SMTP text messaging and TLS connections.")
print("This script is based on: https://gist.github.com/alexle/1294495")
print("Look here for help with cell numbers: https://mfitzp.io/list-of-email-to-sms-gateways/")

def main():
    username = input("Gmail Username: ")
    password = input("Password: ")

    from_ = input("From: ")
    print('For "To:" Numbers only, No punctuation, No country code.')
    to_ = input("To: ")
    message = input("Message (Shorter is better): ")
    while len(message) > 140:
        print("You should try a shorter message.")
        message = input("Message (Shorter is better): ")
        
    iterations = int(input("How many times to send the message? "))
    while iterations > 10:
        print("You should maybe get a real service to handle this.")
        print("Please, no more than 10 time.")
        iterations = int(input("How many times to send the message? "))
    print("For delays more than 55 seconds, credintials will be stored")
    print("in system memory, until send cycle is complete, and then erased.")
    delay = int(input("How long between messages (in seconds)? "))
    while delay > 21700:
        print("You should maybe get a real service to handle this.")
        print("Please, no more than 6 hours (21700 seconds)")
        delay = int(input("How long between messages (in seconds)? "))

    current_message = 0
    if delay < 56:
        server = smtplib.SMTP( "smtp.gmail.com", 587 )
        server.starttls()
        server.login(username, password)
        username = None
        password = None
        while current_message < iterations:
            server.sendmail(from_, to_, message)
            current_message += 1
            print("Message " + str(current_message) + " sent.")
            if current_message < iterations:
                time.sleep(delay)
        server.quit()
    elif delay > 55:
        while current_message < iterations:
            server = smtplib.SMTP( "smtp.gmail.com", 587 )
            server.starttls()
            server.login(username, password)
            server.sendmail(from_, to_, message)
            current_message += 1
            print("Message " + str(current_message) + "sent.")
            server.quit()
            if current_message < iterations:
                time.sleep(delay)
        username = None
        password = None

    print("All messages sent")
    restart = input("Do you want to do it again? [yes/no]: ")
    while restart != "yes":
        if restart == "no":
            break
        print('Not valid response ("yes" or "no," no capital letters)')
        restart = input("Do you want to do it again? [yes/no]: ")
    if restart == "no":
        quit()
        username = None
        password = None
    if restart == "yes":
        print("Restarting...")
        main()

main()
