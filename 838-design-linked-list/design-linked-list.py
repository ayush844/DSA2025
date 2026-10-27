class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if not self.head or index < 0 or index >= self.size:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next

        return curr.val
        

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.addAtHead(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next

        node = Node(val)
        curr.next = node
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            node = Node(val)
            prev = None
            curr = self.head

            for i in range(index):
                prev = curr
                curr = curr.next

            prev.next = node
            node.next = curr

            self.size+=1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size or not self.head:
            return

        if index == 0:
            self.head = self.head.next
            self.size-=1
            return

        curr = self.head

        for _ in range(index-1):
            curr = curr.next

        curr.next = curr.next.next
        self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)