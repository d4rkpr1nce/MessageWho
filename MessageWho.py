import csv

import pywhatkit as pyw

import datetime as dt

from time import sleep

import pyfiglet

from termcolor import colored

filename = "c:/Users/User/Desktop/RuleAll/DeepSec/Projects/whatsapp_automater/contacts.csv"

names = []

numbers = []

with open(filename,'r') as csvfile:
    
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:

        names.append(row['Name'])

        numbers.append(row['Number'])

contacts = dict(zip(names,numbers))

def banner():

    custom_fig = pyfiglet.Figlet(font='doom')

    print(colored(custom_fig.renderText('WhatsApp Automator'),'green'))

    print(colored("***************************************************************************************************************************",'red'))
    
    print(colored("\t\t\t\t\t\t  Author  : d4rkpr1nce\n\t\t\t\t\t\t GitHub  : https://github.com/d4rkpr1nce",'cyan',attrs=['bold']))
    
    print(colored("***************************************************************************************************************************",'red'))    
    
def choice():

    userChoice = "0"

    while userChoice in ["0","1", "2"]:
    
        print("\nPress 1 to : Send a message to some of your contacts which are specified by you.\nPress 2 to : Notify all your contacts that you have changed your number .\nPress 3 : Exit from the program.")
        
        userChoice = input("Your choice: ")
        
        userChoice = userChoice.splitlines()[0]
    
        if int(userChoice)==1:
        
            message_group()
        
        if int(userChoice)==2:
            
            number_changed()

    print("\n[+]Exiting the program...")

    sleep(1)

    exit()

def send_message(name,number,time,message):

    #country_code = int(input("Please enter your country code: "))

    pyw.sendwhatmsg(f"+90{number}",f"{message}",time.hour,time.minute)


def message_group(contacts):
    
    receiver_number = input("Specify how many people you want to message.")

    while receiver_number > contacts:
        
            print("Number of receivers must be less than your total contact number!")

            receiver_number = int(input("Please provide a legit number: "))

    receivers = list(map(int,input("\nEnter the names of receivers: ").strip().split()))[:receiver_number]

    hour, minute = map(int,input("Please give the time to message in 00:00 format.").split(":"))

    time = dt.time(hour,minute)

    for counter,name in enumerate(receivers):

        if name == names[counter]:

            message = str(input(f"What would you like to tell to {name}? "))
            
            send_message(name,contacts[name],time,message)
        
def number_changed():

    message = "Hello, this is d4rkpr1nce.I have changed my number to +90XXX XXX XXXX"

    time = dt.datetime.now()

    for name in names:

        send_message(name,contacts[name],time,message)

    print("Successfully sent!")

def main():

    banner()

    choice()

if __name__ == '__main__':
    main()