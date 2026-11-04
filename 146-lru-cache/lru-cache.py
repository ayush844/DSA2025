class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val  
        self.prev = None
        self.next = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left=Node()
        self.right=Node()
        self.hash={}
        
        self.left.next, self.right.prev = self.right, self.left


    def remove(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev
        node.prev, node.next = None, None


    def insert(self, node):
        l, r = self.right.prev, self.right
        l.next, r.prev = node, node
        node.prev, node.next = l, r   
        
    def get(self, key: int) -> int:
        if key in self.hash:
            node=self.hash[key]
            self.remove(node)
            self.insert(node)
            return node.val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])

        new_node = Node(key, value)
        self.hash[key] = new_node
        self.insert(new_node)

        if len(self.hash) > self.capacity:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.hash[lru_node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)