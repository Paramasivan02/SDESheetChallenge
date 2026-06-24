class StackQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        """Adds element x to the end of the queue."""
        self.input_stack.append(x)

    def pop(self) -> int:
        """Removes and returns the front element of the queue."""
        self.peek()
        
        if self.isEmpty():
            return -1
            
        return self.output_stack.pop()

    def peek(self) -> int:
        """Returns the front element of the queue without removing it."""
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
                
        if not self.output_stack:
            return -1
            
        return self.output_stack[-1]

    def isEmpty(self) -> bool:
        """Returns true if the queue is empty, false otherwise."""
        return not self.input_stack and not self.output_stack