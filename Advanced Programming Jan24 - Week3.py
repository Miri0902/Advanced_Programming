# Stack lecturer example#
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

last = browsing_session.pop()
print(last)

print(browsing_session)

#print('transfer to', browsing_session[-1])

if not browsing_session:
    print(browsing_session[-1])


# Queue Implementation
print("* * * * * * * * * * * * * * *  Queue Implementation")
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

# Example usage
browsing_session = Queue()

# Enqueue elements
browsing_session.enqueue(1)
browsing_session.enqueue(2)
browsing_session.enqueue(3)

print("Browsing Session:", browsing_session.items)

# Dequeue an element
last = browsing_session.dequeue()
print("Dequeued:", last)

print("Updated Browsing Session:", browsing_session.items)

# Check if the queue is empty before accessing the last element
if not browsing_session.is_empty():
    print("Last Element in Browsing Session:", browsing_session.items[-1])
else:
    print("Browsing Session is empty.")


# Deque Implementation
print('************** Deque Implementation *******')
class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

# Example usage for Deque
browsing_session_deque = Deque()

# Add elements to the front and rear of the deque
browsing_session_deque.add_front(1)
browsing_session_deque.add_rear(2)
browsing_session_deque.add_rear(3)

print("\nBrowsing Session (Deque):", browsing_session_deque.items)

# Remove elements from the front and rear of the deque
removed_front = browsing_session_deque.remove_front()
print("Removed from Front of Deque:", removed_front)

removed_rear = browsing_session_deque.remove_rear()
print("Removed from Rear of Deque:", removed_rear)

print("Updated Browsing Session (Deque):", browsing_session_deque.items)

# Check if the deque is empty before accessing the last element
if not browsing_session_deque.is_empty():
    print("Last Element in Browsing Session (Deque):", browsing_session_deque.items[-1])
else:
    print("Browsing Session (Deque) is empty.")

# Queue Implementation - lecturer example

print('*****************************************')

print('Tell me your favourinte sports')
print('Press enter after each choice, R for remove and Q to quit')

Choice = []

while True:
    data = input()
    if str.upper(data) == 'Q':
        break
    elif str.upper(data) == 'R':
        print('removing', Choice.pop(0))
        print(Choice)
    else:
        Choice.append(data)
        print(Choice)

for sports in Choice:
    print('Your mentioned', sports)
