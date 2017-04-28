#!/usr/bin/python3

import smtplib
import time

def main():
    
    print("This script has been customized for the creator's use.")
    print("To customize it to your use, see: https://gist.github.com/alexle/1294495")
    print("and https://mfitzp.io/list-of-email-to-sms-gateways/")
    print("To the extent of my knowledge, a Gmail account is required.")

    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()

    username = input("Gmail Username: ")
    password = input("Password: ")
    server.login( username, password)
    username = None
    password = None

    from_ = input("From: ")
    print("Number only, No punctuation, No country code.")
    to_ = input("To: ")
    #to_ = to_ + "@txt.att.net"
    message = input("Message (Shorter is better): ")
    while len(message) > 140:
        print("You should try a shorter message.")
        message = input("Message (Shorter is better): ")

    iterations = int(input("How many times to send the message? "))
    while iterations > 10:
        print("Too many times! Please, no more than 10.")
        iterations = int(input("How many times to send the message? "))
    delay = int(input("How long between messages (in seconds)? "))
    while delay > 86400:
        print("You should maybe get a real service to handle this.")
        print("Please, no more than 24 hours (86400 seconds)")
        delay = int(input("How long between messages (in seconds)? "))
    
    current_message = 0
    while current_message < iterations:
        server.sendmail( from_, to_, message)
        current_message += 1
        print("message " + str(current_message) + " sent, more may be pending")
        if current_message < iterations:
            time.sleep(delay)

    print("All messages sent")
    restart = input("Do you want to go it again? [yes/no]: ")
    while restart != "yes":
        if restart == "no":
            break
        print("Not valid!")
        restart = input("Do you want to do it again? [yes/no]: ")
    if restart == "no":
        quit()
    if restart == "yes":
        main()
 
main()
