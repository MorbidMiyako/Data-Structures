"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1
        return value

    def dequeue(self):
        if self.size is 0:
            return None
        else:
            deleted_item = self.storage[0]
            self.storage.pop(0)
            self.size -= 1
            return deleted_item
"""


"""
from singly_linked_list import LinkedList
class Queue(LinkedList):
    def __init__(self):
        self.size = 0
        self.queue = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.queue.add_to_tail(value)

    def dequeue(self):
        if self.size is 0:
            return None
        else:
            self.size -= 1
            return self.queue.remove_head()
"""




from stack import Stack
class Queue(Stack):
    def __init__(self):
        self.size = 0
        self.queue = Stack()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.queue.push(value)

    def dequeue(self):
        if self.size is 0:
            return None
        else:
            temp_stack = Stack()
            for moves in range(self.size):
                temp_stack.push(self.queue.pop())
            self.size -= 1
            return_value = temp_stack.pop()
            for moves in range(temp_stack.size):
                self.queue.push(temp_stack.pop())
            return return_value
