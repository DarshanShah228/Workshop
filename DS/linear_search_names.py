# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:28:23 2026

@author: darsh
"""
'''
The Lost Student (Attendance Register)
Professor Sharma enters class and gets a call from the HOD- "is Riya Desai present today?" 
The attendance register is not sorted. Names are written in the order students sat down.
'''
student = ['Darshan', 'Riya','Kaushika','Meet','Karan']
nm = input("Enter name you want to find : ")

for i in student:
    if i == nm:
        print(nm, "is present in class...")
        break
else:
    # This executes ONLY if the loop finished naturally without breaking
    print(nm, "is not present in class!")
