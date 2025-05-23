class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)
    def peak(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return 'Стек пуст'
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return 'Стек пуст'
