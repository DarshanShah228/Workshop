# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 20:33:45 2026

@author: darsh
"""
'''
An Amazon fulfilment centre has a conveyor belt with exactly 8 slots numbered 0-7. Each slot holds one product. The warehouse manager needs to: check what's at a slot, find a product, update a slot, and check if the belt is full. The conveyor belt - fixed 8 slots..
'''

belt = [None] * 8
def check(slot):
    if 0 <= slot <= 7:
        print("slot", slot, "is", belt[slot])
    else:
        print("Error! Invalid slot. Choose 0 to 7.")

def search(name):
    if name in belt:
        print("Product", name, "found at slot", belt.index(name))
    else:
        print("Product", name, "not found on the belt.")

def update(slot, name):
    if 0 <= slot <= 7:
        if name.lower() == "none" or name == "":
            belt[slot] = None
            print("Slot", slot, "cleared.")
        else:
            belt[slot] = name
            print("Slot", slot, "updated")
    else:
        print("Error! Invalid slot. Choose 0 to 7.")

def full():
    if None not in belt:
        print("Its completely FULL.")
    else:
        print("still empty slots available.")


while True:
    
    print("1. Check slot")
    print("2. Search slot")
    print("3. Update/Change slot")
    print("4. Check slot is full")
    print("5. Exit")
    
    ch = input("Enter your choice (1-5): ")
    
    if ch == "1":
        slot_num = int(input("Enter slot number (0-7): "))
        check(slot_num)
        
    elif ch == "2":
        prod_name = input("Enter product name to search: ")
        search(prod_name)
        
    elif ch == "3":
        slot_num = int(input("Enter slot number to change (0-7): "))
        prod_name = input("Enter new product name: ")
        update(slot_num, prod_name)
        
    elif ch == "4":
        full()
        
    elif ch == "5":
        print("Thank You!")
        break
        
    else:
        print("Invalid choice!")
