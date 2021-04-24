
# Hash table implemented using chaining method for collisions
class HashTable:

    def __init__(self, starting_capacity=10):
        self._table = []
        for i in range(starting_capacity):
            self._table.append([])

    # Computes hash using key
    # Complexity is O(1)
    def computeHash(self, keyToHash):
        return keyToHash % len(self._table)
      
    # Inserts a new item into the hash table using the hash of the key to determine the bucket index.
    # Complexity is O(1)
    def insert(self, item):

        bucket = self.computeHash( hash( item ) )
        
        if self._table[bucket] is None:
            self._table[bucket] = [item]
        else:
            self._table[bucket].append(item)
         
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # Complexity is O(n)
    def search(self, item):
        # get the bucket list where this key would be.
        bucket = self.computeHash( hash( item ) )
        bucket_item_list = self._table[bucket]       

        # Iterate over the list of items in the bucket
        for bucket_item in bucket_item_list:
            if hash(bucket_item) == hash(item):
                return bucket_item

        return None

    # Searches for an item using a provided key
    # Returns the item if found, or None if not found.
    # Complexity is O(n)
    def searchByKey(self, key):
        # get the bucket list where this key would be.
        bucket = self.computeHash( key )
        bucket_item_list = self._table[bucket]       

        # Iterate over the list of items in the bucket
        for bucket_item in bucket_item_list:
            if hash(bucket_item) == key:
                return bucket_item

        return None

    # Removes an item from the hash table.
    # Complexity is O(n)
    def remove(self, item):
        bucket = self.computeHash(hash(item))
        bucket_item_list = self._table[bucket]

        for bucket_item in bucket_item_list:
            if hash(bucket_item) == hash(item):
                bucket_item_list.remove(bucket_item)

    # Removes an item from the hash table.
    # Complexity is O(n)
    def removeByKey(self, key):
        bucket = self.computeHash( key )
        bucket_item_list = self.table[bucket]

        for bucket_item in bucket_item_list:
            if hash(bucket_item) == key:
                bucket_item_list.remove(bucket_item)

    # Magic python function that is called when "len" is used
    # Complexity is O(n^2)
    def __len__(self):
        tableSize = 0
        for i in range(0, len(self._table)):
            bucket_array = self._table[i]
            for item in bucket_array:
                tableSize += 1
        return tableSize

    # Magic python function that is used for iterating over the hash table
    # Complexity is O(n)
    def __iter__(self):
        return HashTableIterator(self._table)

    def __repr__(self):
        return "".join(str(self._table))


class HashTableIterator:
    def __init__(self, hashTable):
        self._hash_table = hashTable
        self._index = 0
        self._current_bucket_index = 0

    def __next__(self):

        if self._index < len(self._hash_table):

            # Get the value from the current bucket
            if self._current_bucket_index < len( self._hash_table[self._index] ):
                result = self._hash_table[self._index][self._current_bucket_index]
                self._current_bucket_index += 1
            else:
                self._current_bucket_index = 0
                self._index += 1

                if self._index == len(self._hash_table):
                    raise StopIteration
                    
                result = self._hash_table[self._index][self._current_bucket_index]

                self._current_bucket_index += 1

            return result

        raise StopIteration