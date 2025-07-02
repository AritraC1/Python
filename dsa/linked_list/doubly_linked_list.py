# Doubly Linked List
# Each node points to both next and previous node.
# Traversal can be done forward and backward.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ⇄ ")
            last = current  # Keep track for backward display
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" ⇄ ")
            current = current.prev
        print("None")

# Example
print("Doubly Linked List:")
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display_forward()
print("\nBackward:")
dll.display_backward()