# Circular Singly Linked List
# The last node points back to the head.
# No node points to None.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Circle back to itself
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" → ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

# Example
print("Circular Singly Linked List:")
csll = CircularSinglyLinkedList()
csll.append(5)
csll.append(15)
csll.append(25)
csll.display()