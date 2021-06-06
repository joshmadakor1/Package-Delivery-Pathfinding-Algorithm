from PackageHandler import PackageHandler
from Graph import Graph
from Truck import Truck
import datetime


# Initialize Graph Components
g = Graph()
g.initialize_location_name_data()
g.initialize_location_distance_data()
g.initialize_nodes_hashmap()

# Initialize Packages
p = PackageHandler()

# Initialize Trucks with their ids
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
truck1.add_package(p.get_package_by_id('17'))
truck1.add_package(p.get_package_by_id('12'))
truck1.add_package(p.get_package_by_id('22'))
truck1.add_package(p.get_package_by_id('7'))
truck1.add_package(p.get_package_by_id('2'))


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
truck2.add_package(p.get_package_by_id('24'))
truck2.add_package(p.get_package_by_id('27'))
truck2.add_package(p.get_package_by_id('35'))
truck2.add_package(p.get_package_by_id('39'))


# "Delayed on flight---will not arrive to depot until 9:05 am"
truck3.add_package(p.get_package_by_id('6'))
truck3.add_package(p.get_package_by_id('25'))
truck3.add_package(p.get_package_by_id('28'))
truck3.add_package(p.get_package_by_id('32'))
# -- Address will be updated by this time (incorrect address package)
truck3.add_package(p.get_package_by_id('9'))
# -- Remaining Packages
truck3.add_package(p.get_package_by_id('10'))
truck3.add_package(p.get_package_by_id('4'))
truck3.add_package(p.get_package_by_id('5'))
truck3.add_package(p.get_package_by_id('11'))
truck3.add_package(p.get_package_by_id('21'))
truck3.add_package(p.get_package_by_id('23'))
truck3.add_package(p.get_package_by_id('26'))
truck3.add_package(p.get_package_by_id('33'))


# Calculate optimal routes for the three loaded up trucks
# g.node_list contains informations on the edges/nodes that will
# be used in conjunction with the packages on each truck.
truck1.calculate_best_delivery_route(g.node_list)
truck2.calculate_best_delivery_route(g.node_list)
truck3.calculate_best_delivery_route(g.node_list)


# Fix error in package 9 before departing
# truck2.remove_package(p.get_package_by_id('9'))
# p.get_package_by_id('9').update("410 S State St.", "Third District Juvenile Court", "Salt Lake City", "84111", "")
# truck2.add_package(p.get_package_by_id('9'))

# Build a time object: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
eight_am = datetime.datetime(2021, 7, 1, 8, 0, 0, 0)

# Deliver Packages (Truck1)
# Departure Time: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
# truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
truck1_return_metrics = truck1.deliver_packages(eight_am)

# Deliver Packages (Truck2)
# Departure Time: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
# truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
truck2_return_metrics = truck2.deliver_packages(eight_am)

# Deliver Packages (Truck3)
# Departure Time: Immediately after truck2 returns
# truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
truck3_return_metrics = truck3.deliver_packages(truck2_return_metrics[0])


total_miles_driven = round(float(truck1_return_metrics[2] + truck2_return_metrics[2] + truck3_return_metrics[2]), 2)
time_to_deliver_all_packages = round(float(truck2_return_metrics[1] + truck3_return_metrics[1]), 2)

print(f"Total miles driven:        {total_miles_driven}")
print(f"Hours to deliver packages: {time_to_deliver_all_packages}")
