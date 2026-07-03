# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:04:47 2026

@author: darsh
"""
'''
your younger sibling is packing books into a bag. They don't plari- they just look at two adjacent books, 
and if the heavier one is on top of the lighter one, they swap. They keep repeating this until no more swaps 
happen, Heaviest books slowly bubble up" to the bottom.
'''
book=[110,180,350,200]
n=len(book)
count=0
for i in range(len(book)):
    count=count+1
    for j in range(len(book)-1):
        count=count+1
        flag=0
        if(book[j]>book[j+1]):
            flag =1
            temp=book[j]
            book[j]=book[j+1]
            book[j+1]=temp
            
    if flag==0:
        break

print("Sorted:", book)
print("Total loop iterations:", count)


