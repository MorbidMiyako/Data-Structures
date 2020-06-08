"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.append(value)
        self.size += 1
        return self.storage[self.size-1]

    def pop(self):
        if self.size is 0:
            return None
        else:
            deleted_item = self.storage[self.size-1]
            print(deleted_item)
            self.storage.pop(self.size-1)
            self.size -= 1
            return deleted_item
"""




from singly_linked_list import LinkedList
class Stack(LinkedList):
    def __init__(self):
        self.size = 0
        self.top_item = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.top_item.add_to_tail(value)
        self.size += 1
        return self.top_item.tail.get_value()

    def pop(self):
        if self.size is 0:
            return None
        else:
            deleted_item = self.top_item.tail.get_value()
            print(deleted_item)
            self.top_item.remove_tail()
            self.size -= 1
            return deleted_item


stack = Stack()
print(stack.push(10))
print(stack.pop())
print(stack.pop())
