class ArrayQueue:
    def __init__(self):
        self.queue = []
        self.head = 0

    def push(self, x: int) -> None:
        """Adds element x to the end of the queue."""
        self.queue.append(x)

    def pop(self) -> int:
        """Removes and returns the front element of the queue."""
        if self.isEmpty():
            return -1  
            
        front_val = self.queue[self.head]
        self.head += 1
        return front_val

    def peek(self) -> int:
        """Returns the front element of the queue without removing it."""
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def isEmpty(self) -> bool:
        """Returns true if the queue is empty, false otherwise."""
        return self.head >= len(self.queue)