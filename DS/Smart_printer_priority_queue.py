'''
c3) The Smart Printer Queue (Priority Queue):
An office printer andes jobs in order, BUT jobs marked URGENT must be printed before normal jobs. Design a system using two queues one for urgent, one-for normal and always drain urgent first

H1) Ag Amazon fulfilment centre has a conveyor belt with exactly & slots numbered, 0-7. Each slot nolds one product. The warehouse manager nee to check what's at a slot, find a product, update a slot, and check if the belt is full. The conveyor belt fixed & slots.
H2) Toll Plaza Simulation (Circular Queue)
A toll plaza has a fixed capacity of 5 vehicles. If full, new vehicles must wait. Implement a Circular Queue to simulate this, since it reuses empty slots without wasting memory.

H3) The GPS Navigation System (Backtracking)
You're building a GPS app like Google Maps for a hiking trail. The hiker moves through checkpoints. If they take a wrong turn, they hit "Go Back" to retum to the previous checkpoint. But once they go back, they can also "Go Forward" if they change their mind again just like a browser's back/forward buttons.

Operations:

visit(place) =move to a new place
back()= go to previous place
forward()= go forward if available
'''
from collections import deque

class Printer_Queue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.urgent = deque(maxlen=self.max_size)
        self.normal = deque(maxlen=self.max_size)

    def add_jobs(self, task, priority="normal"):
        if priority == "urgent":
            self.urgent.append(task)
        elif priority == "normal":
            self.normal.append(task)
        else:
            print("Invalid Priority")

    def print_job(self):
        if self.urgent:
            rm = self.urgent.popleft()
            print("Urgent Job is :", rm)

        elif self.normal:
            rm = self.normal.popleft()
            print("Normal Job is :", rm)

        else:
            print("No Job are there")
# Dry Run
printer = Printer_Queue(max_size=5)

printer.add_jobs("Task-1")
printer.add_jobs("Task-2", "urgent")
printer.add_jobs("Task-3")
printer.add_jobs("Task-4", "urgent")
printer.add_jobs("Task-5")

printer.print_job()
printer.print_job()
printer.print_job()
printer.print_job()
printer.print_job()
printer.print_job()