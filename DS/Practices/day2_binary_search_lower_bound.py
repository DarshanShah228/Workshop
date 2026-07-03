# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 19:51:59 2026

@author: darsh
"""

'''
Q:The E-Commerce Price Filter (First occurrence 2 target) 
You're on Flipkart, you filter products: "Show me laptops priced #50,000 or above. 
Products are sorted by price. Elipkart must find the first product 2 50,000-classic binary search 
variant called lower bound.
'''

def lower_bound(prices, target):
    low = 0
    high = len(prices) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if prices[mid] >= target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer

prices = [25000, 32000, 45000, 50000, 55000, 70000]

target = int(input("Enter target price: "))

index = lower_bound(prices, target)

if index != -1:
    print("First product price is", prices[index])
    print("Found at index", index)
else:
    print("No product found")