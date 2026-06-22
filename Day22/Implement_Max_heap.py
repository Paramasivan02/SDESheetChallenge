class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def isEmpty(self) -> bool:
        """Returns True if the heap is empty, False otherwise."""
        return len(self.heap) == 0
        
    def heapSize(self) -> int:
        """Returns the current number of elements in the heap."""
        return len(self.heap)
        
    def insert(self, x: int) -> None:
        """Inserts a new value into the max heap."""
        self.heap.append(x)
        self._heapify_up(len(self.heap) - 1)
        
    def getMax(self) -> int:
        """Returns the maximum value without removing it."""
        if self.isEmpty():
            return -1  
        return self.heap[0]
        
    def extractMax(self) -> int:
        """Removes and returns the maximum element from the heap."""
        if self.isEmpty():
            return -1
            
        max_val = self.heap[0]
        
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop()
            self._heapify_down(0)
            
        return max_val
        
    def changeKey(self, ind: int, val: int) -> None:
        """Updates the value at the given 0-based index."""
        if ind < 0 or ind >= len(self.heap):
            return
            
        old_val = self.heap[ind]
        self.heap[ind] = val
        
        if val > old_val:
            self._heapify_up(ind)
        elif val < old_val:
            self._heapify_down(ind)

    
    def _parent(self, i: int) -> int:
        return (i - 1) // 2
        
    def _left(self, i: int) -> int:
        return 2 * i + 1
        
    def _right(self, i: int) -> int:
        return 2 * i + 2
        
    def _heapify_up(self, i: int) -> None:
        """Bubbles up the element at index i to restore max-heap property."""
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            p = self._parent(i)
            # Swap with parent
            self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
            i = p
            
    def _heapify_down(self, i: int) -> None:
        """Bubbles down the element at index i to restore max-heap property."""
        n = len(self.heap)
        while True:
            largest = i
            l = self._left(i)
            r = self._right(i)
            
            if l < n and self.heap[l] > self.heap[largest]:
                largest = l
                
            if r < n and self.heap[r] > self.heap[largest]:
                largest = r
                
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break