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
        node, next = Node(val), self.head.next
        self.head.next = node
        node.next = next

    def addAtTail(self, val: int) -> None:
        cur = self.head.next
        while cur.next:
            cur = cur.next
        node = Node(val)
        cur.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        while cur.next and index > 0:
            cur = cur.next
            index -= 1
        if index == 0:
            node, next, prev = Node(val), cur.next, cur
            node.next = next
            prev.next = node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head.next
        while cur and index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        if cur and index == 0:
            prev.next = cur.next
        
        
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