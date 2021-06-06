from PackageHandler import PackageHandler
from Graph import Graph
from queue import PriorityQueue, Queue
from Truck import Truck


def graph_test():
    g = Graph()
    g.initialize_location_name_data()
    g.initialize_location_distance_data()
    g.initialize_nodes_hashmap()
    # g.initialize_edges_hashmap()

    # g.print_nodes()

    nodes_remaining = set()

    # Populate Nodes Remaining O(V-1)
    start = "Western Governors University"
    for vertex in g.location_names:
        # vertex[1] -> Ex. "Western Governors University"
        if (vertex[1] != start):
            nodes_remaining.add(vertex[1])

    total_distance = g.get_shortest_distance_to_all_nodes(
        start, nodes_remaining)
    print(total_distance)


def package_handler_test():
    p = PackageHandler()

    #my_packages = p.get_packages_by_status("Can only be on truck 2")
    # print(my_packages[0])
    # print(my_packages[1])
    # print(my_packages[2])
    # print(len(my_packages))
    # print(p.packages)
    # print(len(p.packages))

    for pack in p.packages:
        print(p.get_package_by_id(pack))
    # print(p.get_package_by_id(str(99)))
    #print(p.get_packages_by_address("4580 S 2300 E"))
    #print(len(p.get_packages_by_address("4580 S 2300 Ex")))

    #print(p.get_packages_by_city("Salt Lake City"))
    #print(len(p.get_packages_by_city("Salt Lake City")))

    # for pack in p.get_packages_by_status("Can only be on truck 2"):
    #    print(pack)
    #print(len(p.get_packages_by_status("Can only be on truck 2")))
    #print(p.get_package_by_id("99") == None)

    # print(len(p.packagez))
    # for pack in p.packagez:
    #    print(f"{pack} --> {p.packagez[pack]}")

    # print(p.get_package_by_id("10"))
    # print(p.get_package_by_id("100"))
    # print(p.get_package_by_id("11"))


def priority_queue_test():
    q = PriorityQueue()
    q.put((10.6, "Rice Terrace Pavilion Park", "Valley Regional Softball Complex"))
    q.put((10.7, "Wheeler Historic Farm", "Deker Lake"))
    q.put((5.2, "Wheeler Historic Farm", "Housing Auth. of Salt Lake County"))
    print(q.queue[0])
    print(q.get())
    print(q.get())
    print(q.get())


# Initialize Graph Components
g = Graph()
g.initialize_location_name_data()
g.initialize_location_distance_data()
g.initialize_nodes_hashmap()

# Initialize Packages
p = PackageHandler()

# Initialize Trucks
truck1 = Truck("1")
truck2 = Truck("2")
truck3 = Truck("3")

# Truck1: These packages must be delivered together per the rubric
truck1.add_package(p.get_package_by_id('13'))
truck1.add_package(p.get_package_by_id('14'))
truck1.add_package(p.get_package_by_id('15'))
truck1.add_package(p.get_package_by_id('16'))
truck1.add_package(p.get_package_by_id('19'))
truck1.add_package(p.get_package_by_id('20'))
# Truck1:  -- Deadline 10:30 AM -- #
truck1.add_package(p.get_package_by_id('29'))
truck1.add_package(p.get_package_by_id('1'))
truck1.add_package(p.get_package_by_id('30'))
truck1.add_package(p.get_package_by_id('31'))
# Truck1: -- Remaining Capacity in same Zips
truck1.add_package(p.get_package_by_id('8'))
truck1.add_package(p.get_package_by_id('24'))
truck1.add_package(p.get_package_by_id('27'))
truck1.add_package(p.get_package_by_id('35'))
truck1.add_package(p.get_package_by_id('39'))
truck1.add_package(p.get_package_by_id('10'))


# "Can only be on truck 2" per the rubric
truck2.add_package(p.get_package_by_id('3'))
truck2.add_package(p.get_package_by_id('18'))
truck2.add_package(p.get_package_by_id('36'))
truck2.add_package(p.get_package_by_id('38'))
# -- Deadline 10:30 AM -- #
truck2.add_package(p.get_package_by_id('40'))
truck2.add_package(p.get_package_by_id('37'))
truck2.add_package(p.get_package_by_id('34'))
# Truck2: -- Remaining Capacity in same Zip
truck2.add_package(p.get_package_by_id('17'))
truck2.add_package(p.get_package_by_id('12'))
truck2.add_package(p.get_package_by_id('22'))
truck2.add_package(p.get_package_by_id('7'))
truck2.add_package(p.get_package_by_id('2'))


# "Delayed on flight---will not arrive to depot until 9:05 am"
truck3.add_package(p.get_package_by_id('6'))
truck3.add_package(p.get_package_by_id('25'))
truck3.add_package(p.get_package_by_id('28'))
truck3.add_package(p.get_package_by_id('32'))
# -- Address will be updated by this time (incorrect address package)
truck3.add_package(p.get_package_by_id('9'))
truck3.add_package(p.get_package_by_id('4'))
truck3.add_package(p.get_package_by_id('5'))
truck3.add_package(p.get_package_by_id('11'))
truck3.add_package(p.get_package_by_id('21'))
truck3.add_package(p.get_package_by_id('23'))
truck3.add_package(p.get_package_by_id('26'))
truck3.add_package(p.get_package_by_id('33'))

# print(truck1)
# print(truck2)
# print(truck3)

# print(p.get_package_by_id('9'))
#p.get_package_by_id('9').update("410 S State St.", "Third District Juvenile Court", "Salt Lake City", "84111", "")
# print(p.get_package_by_id('9'))


# print(truck1.calculate_best_delivery_route(g.node_list))
# print(truck2.calculate_best_delivery_route(g.node_list))
print(truck3.calculate_best_delivery_route(g.node_list))
truck3.remove_package(p.get_package_by_id('9'))
p.get_package_by_id('9').update(
    "410 S State St.", "Third District Juvenile Court", "Salt Lake City", "84111", "")
truck3.add_package(p.get_package_by_id('9'))
print(truck3.calculate_best_delivery_route(g.node_list))

# graph_test()

# package_handler_test()


# priority_queue_test()
