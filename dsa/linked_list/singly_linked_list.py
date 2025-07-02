# Singly Linked List
# Each node has: data + pointer to next node
# Traversal: One-way (forward)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node (or None)

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # First node of the list

    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link last node to new node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example
print("Singly Linked List:")
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.display()