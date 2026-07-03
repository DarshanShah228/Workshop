# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:12:06 2026

@author: darsh
"""

book = [110, 180, 350, 200]
n = len(book)
count = 0

for i in range(len(book)):
    count = count + 1
    
    # Standard inner loop comparing adjacent books
    for j in range(len(book) - i - 1):
        count = count + 1
        
        # Swap elements if the top book is heavier than the bottom book
        if book[j] > book[j + 1]:
            temp = book[j]
            book[j] = book[j + 1]
            book[j + 1] = temp

print(book)
print(count)
