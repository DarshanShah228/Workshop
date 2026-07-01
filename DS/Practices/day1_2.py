# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:05:30 2026

@author: darsh
"""
'''
Toll Plaza Simulation (Circular Queue)
A toll plaza has a fixed capacity of 5 vehicles. If full, new vehicles must wait. Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory.
'''
#global variable
capacity = 5
toll = [None] * capacity

front = -1
rear = -1

def enqueue(vehicle_number):
    global front, rear
    
    #check queue is full
    if (rear + 1) % capacity == front:
        print("Toll plaza is FULL! Vehicle", vehicle_number, "must wait.")
        return
        
    # queue is empty, set front to 0
    if front == -1:
        front = 0
        
    # Move rear pointer circularly and insert vehicle
    rear = (rear + 1) % capacity
    toll[rear] = vehicle_number
    print("Result: Vehicle", vehicle_number, "entered the toll lane at space", rear)


def dequeue():
    """Removes a vehicle from the front after they pay the toll."""
    global front, rear
    
    # Check if the queue is empty
    if front == -1:
        print("Toll plaza is EMPTY!")
        return
        
    #vehicle leaving
    removed_vehicle = toll[front]
    toll[front] = None  # Clear the space
    
    # reset
    if front == rear:
        front = -1
        rear = -1
    else:
        # Move front pointer circularly
        front = (front + 1) % capacity
        
    print("Vehicle", removed_vehicle, "paid toll and left.")


def display_queue():
    print("Toll Plaza Status:", toll)
    print("Front Pointer Position:", front, "| Rear Pointer Position:", rear)

while True:
    print("1. Vehicle Arrives (Enqueue)")
    print("2. Vehicle Pays & Leaves (Dequeue)")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        v_num = input("Enter Vehicle Number: ")
        enqueue(v_num)
        
    elif choice == "2":
        dequeue()
        
    elif choice == "3":
        print("Thnak You!")
        break
        
    else:
        print("Invalid choice!")
