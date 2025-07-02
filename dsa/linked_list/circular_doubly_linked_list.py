# Circular Doubly Linked List
# Each node has prev and next.
# Last node's next points to head, head's prev to tail.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node.prev = new_node  # Circle to itself
            return
        tail = self.head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = self.head
        self.head.prev = new_node

    def display_forward(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" ⇄ ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    def display_backward(self):
        if not self.head:
            return
        tail = self.head.prev
        current = tail
        while True:
            print(current.data, end=" ⇄ ")
            current = current.prev
            if current == tail:
                break
        print("(back to tail)")

# Example
print("\nCircular Doubly Linked List:")
cdll = CircularDoublyLinkedList()
cdll.append(100)
cdll.append(200)
cdll.append(300)
cdll.display_forward()
print("\nBackward:")
cdll.display_backward()