from PackageHandler import PackageHandler
from Graph import Graph


def graph_test():
    g = Graph()
    g.initialize_location_name_data()
    g.initialize_location_distance_data()
    g.initialize_nodes_hashmap()
    g.initialize_edges_hashmap()

    g.print_adjacency_list()


def package_handler_test():
    p = PackageHandler()

    my_packages = p.get_packages_by_status("Can only be on truck 2")
    print(my_packages[0])
    print(my_packages[1])
    print(my_packages[2])
    print(len(my_packages))
    # print(p.packages)
    print(len(p.packages))
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


graph_test()
# package_handler_test()
