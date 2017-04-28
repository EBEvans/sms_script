#!/usr/bin/python3

import smtplib
import time
    
print("This script uses Gmail for SMTP text messaging and TLS connections.")
print("This script is based on: https://gist.github.com/alexle/1294495")
print("Look here for help with cell numbers: https://mfitzp.io/list-of-email-to-sms-gateways/")

def connect(username, password):
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(username, password)

def get_credintials():
    username = input("Gmail Username: ")
    password = input("Password: ")
    return (username, password)

def create_message():
    from_ = input("From: ")
    print('For "To:" Numbers only, No punctuation, No country code.')
    to_ = input("To: ")
    message = input("Message (Shorter is better): ")
    while len(message) > 140:
        print("You should try a shorter message.")
        message = input("Message (Shorter is better): ")
        return (from_, to_, message)
        
def create_schedule():
    iterations = int(input("How many times to send the message? "))
    while iterations > 10:
        print("You should maybe get a real service to handle this.")
        print("Please, no more than 10 time.")
        iterations = int(input("How many times to send the message? "))
    print("For delays more than 55 seconds, credintials will be stored,")
    print("until send cycle is complete, and then erased.")
    delay = int(input("How long between messages (in seconds)? "))
    while delay > 21700:
        print("You should maybe get a real service to handle this.")
        print("Please, no more than 6 hours (21700 seconds)")
        delay = int(input("How long between messages (in seconds)? "))
        return (iterations, delay)

def send_cycle(from_, to_, message, username, password, delay, iterations):
    current_message = 0
    if delay < 56:
        connect(username, password)
        username = None
        password = None
        while current_message < iterations:
            server.sendmail(from_, to_, message)
            current_message += 1
            print("Message " + str(current_message) + "sent.")
            if current_message < iterations:
                time.sleep(delay)
        SMTP.quit()
    elif delay > 55:
        while current_message < iterations:
            connect(username, password)
            server.sendmail(from_, to_, message)
            current_message += 1
            print("Message " + str(current_message) + "sent.")
            SMTP.quit()
            if current_message < iterations:
                time.sleep(delay)
        username = None
        password = None

def main():
    get_credintials()
    create_message()
    create_schedule()
    send_cycle(from_, to_, message, username, password, delay, iterations)
    print("All messages sent")
    restart = input("Do you want to go it again? [yes/no]: ")
    while restart != "yes":
        if restart == "no":
            break
        print('Not valid response ("yes" or "no," no capital letters)')
        restart = input("Do you want to do it again? [yes/no]: ")
    if restart == "no":
        quit()
    if restart == "yes":
        print("Restarting...")
        main()

main()
