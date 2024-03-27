class Stack:
    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def empty(self):
        return len(self.items) == 0

    def search(self, target):
        if not self.isEmpty():
            try:
                index = len(self.items) - self.items[::-1].index(target) - 1
                return len(self.items) - 1 - index
            except ValueError:
                return -1
        else:
            return -1
