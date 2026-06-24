class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        """Pushes element x onto the stack."""
        self.stack.append(x)

    def pop(self) -> int:
        """Removes and returns the top element of the stack."""
        if self.isEmpty():
            return -1  
        return self.stack.pop()

    def top(self) -> int:
        """Returns the top element of the stack without removing it."""
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def isEmpty(self) -> bool:
        """Returns true if the stack is empty, false otherwise."""
        return len(self.stack) == 0