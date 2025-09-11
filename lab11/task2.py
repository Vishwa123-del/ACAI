from collections import deque

class QueueList:
    def __init__(self):
        """Initialize an empty queue using a list."""
        self._items = []
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self._items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._items) == 0

class QueueDeque:
    def __init__(self):
        """Initialize an empty queue using a deque."""
        self._items = deque()
    
    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self._items.append(item)
    
    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._items) == 0
if __name__ == "__main__":
    print("Testing QueueList:")
    q1 = QueueList()
    q1.enqueue(10)
    q1.enqueue(20)
    q1.enqueue(30)
    print("Dequeue:", q1.dequeue())  # 10
    print("Dequeue:", q1.dequeue())  # 20
    print("Is empty?", q1.is_empty())  # False
    print("Dequeue:", q1.dequeue())  # 30
    print("Is empty?", q1.is_empty())  # True
    
    print("\nTesting QueueDeque:")
    q2 = QueueDeque()
    q2.enqueue("A")
    q2.enqueue("B")
    q2.enqueue("C")
    print("Dequeue:", q2.dequeue())  # A
    print("Dequeue:", q2.dequeue())  # B
    print("Is empty?", q2.is_empty())  # False
    print("Dequeue:", q2.dequeue())  # C
    print("Is empty?", q2.is_empty())  # True