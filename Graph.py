import csv
from HashMap import HashMap


class Graph:

    # Default Constructor
    def __init__(self):
        self.location_names = [None] * 27
        self.distance_map = HashMap()
        self.raw_distance_data = []

    # Populates the location name data
    def populate_location_name_data(self):

        with open("distance_names.csv") as file:
            names_reader = csv.reader(file)
            raw_distance_names = list(names_reader)
            # print(raw_distance_names)
            i = 0
        for entry in raw_distance_names:
            self.location_names[i] = entry
            i += 1

    # Populates the location distance data
    def populate_location_distance_data(self):
        with open("distance_data.csv") as file:
            reader = csv.reader(file)
            self.raw_distance_data = list(reader)

    # Populates the hashmap with distance data for each address
    def populate_hashmap_with_distance_data_for_each_adress(self):
        for i in range(len(self.raw_distance_data)):
            list = []
            for j in range(len(self.raw_distance_data)):

                # Add distance entries horizontally
                if j < i:
                    list.append([self.location_names[j][1],
                                self.raw_distance_data[i][j]])
                # Add distance entries vertically, to account for 2 way mapping
                elif j > i:
                    list.append([self.location_names[j][1],
                                self.raw_distance_data[j][i]])

            # Create an entry in the hash map for for all the distances to that address
            self.distance_map.add(self.location_names[i][1], list)


g = Graph()
g.populate_location_name_data()
g.populate_location_distance_data()
g.populate_hashmap_with_distance_data_for_each_adress()

for name in g.location_names:
    print(g.distance_map.get(name[1]))
    print("")
    print("")
