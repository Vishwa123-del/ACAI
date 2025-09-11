
class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []
    def push(self, item):
        self._items.append(item)
    def pop(self):
        
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]
    def is_empty(self):
        return len(self._items) == 0
if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.is_empty())  # True
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Peek:", stack.peek())  # 30
    print("Pop:", stack.pop())    # 30
    print("Peek after pop:", stack.peek())  # 20
    print("Pop:", stack.pop())    # 20
    print("Pop:", stack.pop())    # 10
    print("Is stack empty after pops?", stack.is_empty())  # True
