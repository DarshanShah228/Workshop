# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:56:32 2026

@author: darsh
"""
'''
Q:Merge Sort-The IRCTC Waitlist Merger

IRCTC has two separately sorted waitlists-one from its mobile app, one from railway counters. 
To produce a final unified waitlist, they don't re-sort from scratch. They merge both sorted lists in one 
pass compare the front of each list, pick the smaller taken advance. This is exactly merge sort's merge step.
'''
def merge_waitlist(list1, list2):
    i = 0
    j = 0
    merged = []

    while i < len(list1) and j < len(list2):

        if list1[i] < list2[j]:
            merged.append(list1[i])
            i = i + 1
        else:
            merged.append(list2[j])
            j = j + 1

    while i < len(list1):
        merged.append(list1[i])
        i = i + 1

    while j < len(list2):
        merged.append(list2[j])
        j = j + 1

    return merged


mobile_waitlist = [2, 5, 8, 12]
counter_waitlist = [1, 4, 7, 10]

final_waitlist = merge_waitlist(mobile_waitlist, counter_waitlist)

print("Merged Waitlist:")
print(final_waitlist)