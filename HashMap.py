import csv


class HashMap:
    # Default Constructor
    def __init__(self):
        self.size = 128
        self.map = [None] * self.size

    # Calculates the array index where the item will stored
    def calculate_hash_index(self, input):
        pre_mod_hash = 0
        # Sum up the ASCII/Decimal value of the input.
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
        else:
            for keyValuePair in self.map[hash]:
                # If the key is the same, overwrite the value
                if keyValuePair[0] == key:
                    keyValuePair[1] = val
                    return True
                # If the key is not the same, append it to the list
                self.map[hash].append(value)
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
                return True


h = HashMap()
contents = [None]
with open("data.csv") as file:
    reader = csv.reader(file)
    contents = list(reader)

for c in contents:
    h.add(c[0], c[1])
    # print(c[1])

non_none = 0
for item in h.map:
    if item is not None:
        # print(len(item))
        non_none += 1

print(f"Non-empty elements: {non_none}")
