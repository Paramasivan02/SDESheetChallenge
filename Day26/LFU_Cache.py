import collections

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_head(self, node: Node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
        self.size += 1

    def remove_node(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def remove_tail(self) -> Node:
        if self.size > 0:
            tail_node = self.tail.prev
            self.remove_node(tail_node)
            return tail_node
        return None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_dll = collections.defaultdict(DoublyLinkedList)

    def _update_freq(self, node: Node):
        freq = node.freq
        
        self.freq_to_dll[freq].remove_node(node)
        
        if self.min_freq == freq and self.freq_to_dll[freq].size == 0:
            self.min_freq += 1
            
        node.freq += 1
        self.freq_to_dll[node.freq].insert_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
            
        node = self.key_to_node[key]
        self._update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update_freq(node)
        else:
            if len(self.key_to_node) >= self.capacity:
                dll = self.freq_to_dll[self.min_freq]
                evicted_node = dll.remove_tail()
                del self.key_to_node[evicted_node.key]
                
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            
            self.min_freq = 1
            self.freq_to_dll[1].insert_head(new_node)