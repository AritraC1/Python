# Linked List

'''
A Linked List is a linear data structure where each element (node) points to the next.
Each node contains two parts:
1. Data
2. Pointer (reference) to the next node

Basic Structure of a Linked List

[10 | next] --> [20 | next] --> [30 | None]
 ↑                                    ↑
head                                 tail

- Head is always the first node, here head is 10
- Tail is always the last node, here tail is 30

- next is a reference (or pointer) in a node that points to the next node in the linked list.
- None means the end of the list — it tells us there is no next node after this one.

There are 4 main types of linked lists:
1. Singly Linked List
2. Doubly Linked List
3. Circular Singly Linked List
4. Circular Doubly Linked List

'''

# Step 1: Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Data held by the node
        self.next = None  # Reference to the next node (default is None)

# Step 2: Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initially the list is empty

    # Method to add node at the end (append operation)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            # If list is empty, new node becomes the head
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Method to display the list
    def display(self):
        current = self.head
        if current is None:
            print("Linked List is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to insert a node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Method to insert after a given node
    def insert_after_node(self, prev_node_data, data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if not current:
            print(f"Node with data {prev_node_data} not found.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # Method to delete a node by value
    def delete_node(self, key):
        current = self.head

        # If head node holds the key to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with value {key} not found.")
            return

        prev.next = current.next
        current = None

    # Method to search for a value in the list
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Method to get the length of the list
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
# Step 3: Use the LinkedList class

# Create an instance of LinkedList
ll = LinkedList()

# Append nodes
ll.append(10)
ll.append(20)
ll.append(30)

# Display list
print("Initial list:")
ll.display()

# Prepend node
ll.prepend(5)
print("\nAfter prepending 5:")
ll.display()

# Insert after node
ll.insert_after_node(20, 25)
print("\nAfter inserting 25 after 20:")
ll.display()

# Delete a node
ll.delete_node(10)
print("\nAfter deleting 10:")
ll.display()

# Search for a value
print("\nSearching for 25:", ll.search(25))
print("Searching for 100:", ll.search(100))

# Get length
print("\nLength of the list:", ll.length())