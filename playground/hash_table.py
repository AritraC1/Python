# Custom hash map to understand how hash maps work internally.
class HashTable:
    # Initialisation
    def __init__(self, size):
        self.size=size
        self.hash_table=[ [] for _ in range(size) ]

    # Insert or Update: Add a key-value pair. If the key exists, update its value.
    def set_val(self, key, val):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket[index] = (key, val)
                return
        
        bucket.append((key, val))

    # Retrieve: Get the value associated with a key. Returns "No record found" if the key does not exist.
    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for record_key, record_val in bucket:
            if record_key == key:
                return record_val

        return "No record found"
    
    # Delete: Remove a key-value pair from the hash map.
    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        for index, (record_key, _) in enumerate(bucket):
            if record_key == key:
                bucket.pop(index)
                return
            
    # Display: Show all key-value pairs stored in the hash map. 
    def __str__(self):
        return "".join(str(bucket) for bucket in self.hash_table)
    

# Creating and Printing the Hash Table
hashTable = HashTable(4)
print("\nMy custom hashTable:", hashTable)

# Examples
hashTable.set_val("apple", 30)
hashTable.set_val("mango", 50)
hashTable.set_val("banana", 10)
hashTable.set_val("grapes", 10)

print("\nHash table:", hashTable)
print("\nValue for grapes:", hashTable.get_val("grapes"))

hashTable.set_val("orange", 20)
print("\nUpdated custom hashtable: ", hashTable)

hashTable.delete_val("banana")
print("\nAfter Deletion:", hashTable)
print("\nValue for 'banana':", hashTable.get_val("banana"))




