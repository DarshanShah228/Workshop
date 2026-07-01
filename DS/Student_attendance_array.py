# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
1) Imagine a dass with 30 students. The teacher maintains an attendance register where each roll number has a fixed position.

Roll No. 1

Index 0

Roll No. 2

Index 1

Roll No. 30

Index 29

ince every student has a fixed slot (index), the teacher can directly go to any student's attendance without checking the previous records.

For example:

If the teacher wants to mark the atten fance of Roll No. 16, they can directly access Index 15.

There is no need to search from Roll No. 1 to Roll No. 16.

This is called direct (random) access, which is the most important feature of an array

'''
attendance = ["Absent"] * 30
roll_no=int(input("Enter Roll No:"))
attendance[roll_no - 1] = "Present"

print("Roll No.:", roll_no)
print("Index:", roll_no - 1)
print("Attendance:", attendance[roll_no - 1])
