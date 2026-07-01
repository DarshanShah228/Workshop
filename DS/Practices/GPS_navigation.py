# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:06:58 2026

@author: darsh
"""
'''
The GPS Navigation System (Backtracking)
You're building a GPS app like Google Maps for a hiking trail. The hiker moves through checkpoints. If they take a wrong turn, they hit "Go Back" to return to the previous checkpoint. But once they go back, they can also "Go Forward" d they change their mind again - just like a browser's back forward buttons

Operations:
visit(place) move to a new place
back()- go to previous place
forward()
go forward if available
'''
# global variables 
curr = "Start"
back = []
forward = []

def visit(place):
    global curr
    back.append(curr)
    curr = place
    forward.clear()
    print("Moved to:", curr)

def go_back():
    global curr
    if len(back) == 0:
        print("Cannot go back! Already at the start.")
        return
    forward.append(curr)
    curr = back.pop()
    print("Moved back to:", curr)

def go_forward():
    global curr
    if len(forward) == 0:
        print("Cannot go forward! No history available.")
        return
    back.append(curr)
    curr = forward.pop()
    print("Moved forward to:", curr)

def show():
    print("Back Stack   :", back)
    print("Current Spot :", curr)
    print("Forward Stack:", forward)

while True:
    print("1. Visit new place")
    print("2. Go Back")
    print("3. Go Forward")
    print("4. Exit")
    
    ch = input("Enter choice: ")
    
    if ch == "1":
        name = input("Enter location name: ")
        visit(name)
    elif ch == "2":
        go_back()
    elif ch == "3":
        go_forward()
    elif ch == "4":
        print("Thank You!")
        break
    else:
        print("Invalid choice..")
