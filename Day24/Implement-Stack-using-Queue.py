from collections import deque

class QueueStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        """Pushes element x onto the stack."""
        self.q.append(x)
        
        size = len(self.q)
        for _ in range(size - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """Removes and returns the top element of the stack."""
        if self.isEmpty():
            return -1
        return self.q.popleft()

    def top(self) -> int:
        """Returns the top element of the stack without removing it."""
        if self.isEmpty():
            return -1
        return self.q[0]

    def isEmpty(self) -> bool:
        """Returns true if the stack is empty, false otherwise."""
        return len(self.q) == 0