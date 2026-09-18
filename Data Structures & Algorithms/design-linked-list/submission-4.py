class MyLinkedList:
    def __init__(self):
        self.head = Node(0) 

    def get(self, index: int) -> int:
        cur = self.head.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        prev = self.head
        while prev.next:
            prev = prev.next
        node = Node(val)
        prev.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        prev = self.head
        while prev.next and index > 0:
            prev = prev.next
            index -= 1
        if index == 0:
            node = Node(val)
            node.next = prev.next
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        prev = self.head
        while prev.next and index > 0:
            prev = prev.next
            index -= 1
        if index == 0 and prev.next is not None:
            prev.next = prev.next.next
        
        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)