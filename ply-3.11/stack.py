class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
         if self.size() > 0:
             return self.items.pop()
         print('//STACK-VACIO//')

    def top(self):
        return self.items[len(self.items)-1]