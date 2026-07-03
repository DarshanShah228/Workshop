# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:43:29 2026

@author: darsh
"""
'''
The Spam Detector (Search in Stream)-linear search
A cybersecurity intern at a startup is building a basic spam filter incoming emails are 
checked against a blacklist of known spam sender IDs. The blacklist has no order
'''
# List of spam email addresses
blacklist = [
    "fake123@gmail.com",
    "spamuser@gmail.com",
    "fraudmail@yahoo.com",
    "blocked@outlook.com",
    "offer@winner.com"
]

# Function to check whether an email is spam
def spam_detector(email):
    if email in blacklist:
        print(email, "is a Spam Sender.")
    else:
        print(email, "is Not a Spam Sender.")

# Take email input from the user
email = input("Enter Email Address: ")

# Check the email
spam_detector(email)