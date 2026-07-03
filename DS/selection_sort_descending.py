# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:20:09 2026

@author: darsh
"""
'''
The Scholarship RankerA college must give scholarships to the top 3 scorers. 
The coordinator scans the entire marksheet, finds the highest scorer, mgyes them to position 
    1. Then scans the remaining students for the next highest, and so on. Each pass = one full scan to select the minimum/maximum
'''
marks = [78, 92, 85, 99, 64, 89, 95]
n = len(marks)
count = 0

for i in range(len(marks)):
    count = count + 1
    for j in range(len(marks) - 1):
        count = count + 1
        
        if marks[j] < marks[j + 1]:
            temp = marks[j]
            marks[j] = marks[j + 1]
            marks[j + 1] = temp

print("Sorted Marks (Descending):", marks)
print("Top 3 Scholars:", marks[:3])
print("Total loop iterations:", count)
