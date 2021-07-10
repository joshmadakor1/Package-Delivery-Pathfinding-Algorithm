# Nnamdi Joshua Madakor, ID: 000214961
class HashMap:
    # Default Constructor
    def __init__(self):
        self.size = 128
        self.map = [None] * self.size
        self.length = -1  # -1 Accounts for \ufeff in top row of CSV for some reason

    # Calculates the array index where the item will stored
    def calculate_hash_index(self, input):
        pre_mod_hash = 0
        input = str(input)
        # Very basic hashing function; sum up the ASCII/Decimal value of the input.
        for c in input:
            pre_mod_hash += ord(c)
        return pre_mod_hash % self.size

    # Add a Key-Value pair to the HashMap
    def add(self, key, val):

        # Calculate the hash value for the key(/value pair) to add
        hash = self.calculate_hash_index(key)

        value = [key, val]

        # If the key doesn't exist in the map yet, add it
        if self.map[hash] is None:
            self.map[hash] = list([value])
            self.length += 1
        else:
            for keyValuePair in self.map[hash]:
                # If the key is the same, overwrite the value
                if keyValuePair[0] == key:
                    keyValuePair[1] = val
                    return True
                # If the key is not the same, append it to the list
                self.map[hash].append(value)
                self.length += 1
                return True

    # Retrieve a Key-Value pair from the HashMap
    def get(self, key):

        # Calculate the hash value for the key(/value pair) to retrieve
        hash = self.calculate_hash_index(key)

        # If the key exists in the Hashmap...
        if self.map[hash] is not None:
            # Iterate the list and return the value
            for keyValuePair in self.map[hash]:
                if keyValuePair[0] == key:
                    return keyValuePair[1]
        # Specified key does not exist in the HashMap
        return None

    # Delete a Key-Value pair from the HashMap
    def delete(self, key):
        # Calculate the hash value for the key(/value pair) to delete
        hash = self.calculate_hash_index(key)

        # If the hash does not exist, exit the function
        if self.map[hash] is None:
            return False

        # Iterate through the list...
        for i in range(0, len(self.map[hash])):

            # Pop the entry whos key matches the target key
            if self.map[hash][i][0] == key:
                self.map[hash].pop(i)
                self.length -= 1
                return True

    def print(self, key):
        # Calculate the hash value for the key(/value pair) to delete
        hash = self.calculate_hash_index(key)
        for i in range(0, len(self.map[hash])):
            # Pop the entry whos key matches the target key
            if self.map[hash][i][0] == key:
                print(self.map[hash][0][1])
