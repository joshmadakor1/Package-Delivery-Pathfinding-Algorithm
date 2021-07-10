# Nnamdi Joshua Madakor, ID: 000214961
from PackageHandler import PackageHandler
from Graph import Graph
from Truck import Truck
from datetime import timedelta
from operator import itemgetter
from queue import Queue
import datetime
import time
import collections


# Used for storing package status over time
package_status_over_time = dict(dict())
# use: people['10:22']['10'] = 'DELIVERED'

# Initialize Graph Components
g = Graph()

# Initialize Packages
package_handler = PackageHandler()

# Time-complexity: O(n)
# Add packages to the truck and optimizes delivery route
# initialize_truck3


def initialize_truck1():
    # clear the delivery nodes, in case packages are manipulated
    # If you don't clear this, the truck will drive to spots
    # even if there is no package to delvier lol
    truck1.delivery_nodes.clear()
    truck1.add_package(package_handler.get_package_by_id('1'))
    truck1.add_package(package_handler.get_package_by_id('29'))
    truck1.add_package(package_handler.get_package_by_id('7'))
    truck1.add_package(package_handler.get_package_by_id('30'))
    truck1.add_package(package_handler.get_package_by_id('8'))
    truck1.add_package(package_handler.get_package_by_id('34'))
    truck1.add_package(package_handler.get_package_by_id('40'))
    truck1.add_package(package_handler.get_package_by_id('13'))
    truck1.add_package(package_handler.get_package_by_id('39'))
    truck1.add_package(package_handler.get_package_by_id('14'))
    truck1.add_package(package_handler.get_package_by_id('15'))
    truck1.add_package(package_handler.get_package_by_id('16'))
    truck1.add_package(package_handler.get_package_by_id('19'))
    truck1.add_package(package_handler.get_package_by_id('20'))
    truck1.add_package(package_handler.get_package_by_id('37'))
    truck1.add_package(package_handler.get_package_by_id('25'))

    # Calculate optimal routes for the three loaded up trucks
    # g.node_list contains informations on the edges/nodes that will
    # be used in conjunction with the packages on each truck.
    truck1.optimize_delivery_route(g.adjacency_matrix)

# Time-complexity: O(n)
# Add packages to the truck and optimizes delivery route
# initialize_truck3


def initialize_truck1_trip2():
    # clear the delivery nodes, in case packages are manipulated
    # If you don't clear this, the truck will drive to spots
    # even if there is no package to delvier lol
    truck1_trip2.delivery_nodes.clear()
    truck1_trip2.add_package(package_handler.get_package_by_id('6'))
    truck1_trip2.add_package(package_handler.get_package_by_id('5'))

    truck1_trip2.add_package(package_handler.get_package_by_id('21'))
    truck1_trip2.add_package(package_handler.get_package_by_id('4'))
    truck1_trip2.add_package(package_handler.get_package_by_id('24'))
    truck1_trip2.add_package(package_handler.get_package_by_id('23'))
    truck1_trip2.add_package(package_handler.get_package_by_id('26'))
    truck1_trip2.add_package(package_handler.get_package_by_id('22'))
    truck1_trip2.add_package(package_handler.get_package_by_id('10'))
    truck1_trip2.add_package(package_handler.get_package_by_id('11'))
    truck1_trip2.add_package(package_handler.get_package_by_id('31'))

    # Calculate optimal routes for the three loaded up trucks
    # g.node_list contains informations on the edges/nodes that will
    # be used in conjunction with the packages on each truck.
    truck1_trip2.optimize_delivery_route(g.adjacency_matrix)


# Time-complexity: O(n)
# Add packages to the truck and optimizes delivery route
# initialize_truck3

def initialize_truck2():
    # clear the delivery nodes, in case packages are manipulated
    # If you don't clear this, the truck will drive to spots
    # even if there is no package to delvier lol
    truck2.delivery_nodes.clear()
    truck2.add_package(package_handler.get_package_by_id('17'))
    truck2.add_package(package_handler.get_package_by_id('12'))
    truck2.add_package(package_handler.get_package_by_id('28'))
    truck2.add_package(package_handler.get_package_by_id('32'))
    truck2.add_package(package_handler.get_package_by_id('3'))
    truck2.add_package(package_handler.get_package_by_id('18'))
    truck2.add_package(package_handler.get_package_by_id('36'))
    truck2.add_package(package_handler.get_package_by_id('38'))
    # Only on truck 2 ^ ^ ^
    truck2.add_package(package_handler.get_package_by_id('27'))
    truck2.add_package(package_handler.get_package_by_id('35'))
    truck2.add_package(package_handler.get_package_by_id('2'))
    truck2.add_package(package_handler.get_package_by_id('33'))
    truck2.add_package(package_handler.get_package_by_id('9'))
    # No requirements ^ ^ ^

    # Calculate optimal routes for the three loaded up trucks
    # g.node_list contains informations on the edges/nodes that will
    # be used in conjunction with the packages on each truck.
    truck2.optimize_delivery_route(g.adjacency_matrix)

# Time-complexity: O(n + n + n^2) = O(2n + n^2) -> O(n^2)
# initialize_graph


def initialize_graph():
    g.initialize_location_name_data()
    g.initialize_location_distance_data()
    g.initialize_nodes_hashmap()


# Initialize Trucks with their ids
initialize_graph()
truck1 = Truck("1")
truck1_trip2 = Truck("1_trip2")
truck2 = Truck("2")
initialize_truck1()
initialize_truck1_trip2()
initialize_truck2()

# Keep track of whether or not Package 9's address has been updated
package_9_has_been_updated = False

# O(n + n + n) -> O(3n) -> O(n)
# Runs the delivery simulation
#   Truck1 and Truck2 both leave at 8am
#   Truck2 returns and performs a second trip
#   Truck3 leaves when Truck1 returns
#
#  Delivery information will be printed out on the screen:
#   Total Drive Time and Miles for each truck
#
# @para - package_status_over_time:
#   Used to store delivery information that is later used to query
#   package statuses at different points along the way.


def delivery_simulation(package_status_over_time):
    # Build a time object: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    eight_am = datetime.datetime(2021, 7, 1, 8, 0, 0, 0)

    # Build a time object: 2021-07-01 08:00:00 (July 1, 2021, 9:05 AM)
    nine_oh_five = datetime.datetime(2021, 7, 1, 9, 5, 0, 0)

    # Build a time object: 2021-07-01 10:20:00 (July 1, 2021, 8:00 AM)
    ten_twenty = datetime.datetime(2021, 7, 1, 10, 20, 0, 0)

    # Deliver Packages (Truck1)
    # Departure Time: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    # truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
    initialize_truck1()
    truck1_return_metrics = truck1.deliver_packages(
        eight_am, package_handler, package_status_over_time, package_9_has_been_updated)

    initialize_truck1_trip2()
    truck1_trip2_return_metrics = truck1_trip2.deliver_packages(
        truck1_return_metrics[0], package_handler, package_status_over_time, truck1_return_metrics[3])

    # Deliver Packages (Truck2)
    # Departure Time: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    # truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
    initialize_truck2()
    truck2_return_metrics = truck2.deliver_packages(
        ten_twenty, package_handler, package_status_over_time, truck1_trip2_return_metrics[3])

    # Sort package_status_over_time by time delivered. This will be used to see the status
    # throughout the delivery lifecycle
    # Sort the packages by time delivered
    #package_status_over_time = sorted(package_status_over_time, key=itemgetter(0))

    # I don't know how to manipulate time in python and I'm lazy.
    # The following code finds the time difference between when the first
    # truck departs and when the last truck arrives and converts it into a string.
    start = eight_am
    finish = truck2_return_metrics[0]
    finish = finish - start
    hours = finish.seconds // 3600
    minutes = (finish.seconds % 3600) // 60
    total_trip_time = str(hours) + ":" + str(minutes)

    time_to_deliver_all_packages = round(
        float(truck2_return_metrics[1] + truck1_trip2_return_metrics[1]), 2)
    time_to_deliver_all_packages = datetime.datetime(
        2021, 7, 1, 0, 0, 0, 0) + timedelta(hours=time_to_deliver_all_packages)

    total_miles_driven = truck1_return_metrics[2] + \
        truck1_trip2_return_metrics[2] + truck2_return_metrics[2]
    print("")
    print("")
    print("\tTruck1 metrics:")
    print("\t-----------------------------------")
    print(f"\tDeparture Time: {eight_am}")
    print(f"\tReturn Time:    {truck1_return_metrics[0]}")
    print(
        f"\tDrive Time:     {round(float(truck1_return_metrics[1]),2)} hours")
    print(
        f"\tTotal Distance: {round(float(truck1_return_metrics[2]),2)} miles")
    print("")
    print("\tTruck1 (Second Trip) metrics:")
    print("\t-----------------------------------")
    print(f"\tDeparture Time: {truck1_return_metrics[0]}")
    print(f"\tReturn Time:    {truck1_trip2_return_metrics[0]}")
    print(
        f"\tDrive Time:     {round(float(truck1_trip2_return_metrics[1]),2)} hours")
    print(
        f"\tTotal Distance: {round(float(truck1_trip2_return_metrics[2]),2)} miles")
    print(f"")
    print("\tTruck2 metrics:")
    print("\t-----------------------------------")
    print(f"\tDeparture Time: {ten_twenty}")
    print(f"\tReturn Time:    {truck2_return_metrics[0]}")
    print(
        f"\tDrive Time:     {round(float(truck2_return_metrics[1]),2)} hours")
    print(
        f"\tTotal Distance: {round(float(truck2_return_metrics[2]),2)} miles")
    print(f"")
    print(f"")
    print(
        f"\tCombined mileage all trucks:  {round(float(total_miles_driven),2)} miles")
    print(
        f"\tTime to deliver all packages: ({hours}) hours and ({minutes}) minutes")
    initialize_graph()
    initialize_truck1()
    initialize_truck1_trip2()
    initialize_truck2()

    # Clear package_status_over_time, allowing it to be repopulated when the
    # delivery simulation runs again
    package_status_over_time = list()


# Time-complexity: O(3n) -> O(n)
# Code blocks executed:
#   run delivery simulation  -> O(n)
#   package history sort     -> O(n)
#   package query branch     -> O(n)
# Run the user interface
user_input = ""
while (user_input != "q"):
    print("")
    print("\tWhat would you like to do?")
    print("")
    print("\td - Begin Delivery Simulation and Package Information Lookup")
    print("\tq - Quit")
    print("")
    # You have to clear this, otherwise it will fill up with duplicate historical
    # delivery records rofl
    package_status_over_time.clear()
    user_input = input(">").lower()

    if (user_input == "d"):
        print("")
        print("\tBeginning delivery simulation...")
        print("")
        delivery_simulation(package_status_over_time)
        print("")
        print("\tDelivery simulation complete.")

        while (user_input != "p" and user_input != "b"):
            print("")
            print("\tWhat would you like to do next?")
            print("")
            print("\tp - Package Information Lookup")
            print("\tb - Back to Main Menu")
            print("")
            user_input = input(">").lower()

            selected_time = None
            if (user_input == "p"):
                while (selected_time == None):

                    print("")
                    while True:
                        print(
                            "\tEnter a point in time for which you want to view package information. For Example: 13:05")
                        print("")
                        selected_time = input(">").lower()
                        try:
                            if (time.strptime(selected_time, "%H:%M")):

                                # Time selected by the user
                                selected_time = time.strptime(
                                    selected_time, "%H:%M")

                                break
                        except ValueError:
                            print("\tInvalid time entered.")
                            continue

                    print("")
                    print("\tHow would you like to query packages?")
                    print("")
                    print(
                        f'\ta - Show ALL package statuses as of {time.strftime("%H:%M", selected_time)}')
                    print("\ti - Lookup by package ID")
                    print("\tr - Lookup by package ADDRESS")
                    print("\td - Lookup by package DEADLINE")
                    print("\tc - Lookup by package CITY")
                    print("\tz - Lookup by package ZIP")
                    print("\tw - Lookup by package WEIGHT")
                    print("\ts - Lookup by package STATUS")
                    print("")
                    query_type = input(">")

                    while (query_type != "a" and query_type != "i" and query_type != "r" and query_type != "d" and query_type != "c" and query_type != "z" and query_type != "w" and query_type != "s"):
                        print("\tinvalid input")
                        print("")
                        print("\tHow would you like to query packages?")
                        print("")
                        print(
                            f"\ta - Show ALL package statuses as of {package_status_over_time[int(user_input)][0]}")
                        print("\ti - Lookup by package ID")
                        print("\tr - Lookup by package ADDRESS")
                        print("\td - Lookup by package DEADLINE")
                        print("\tc - Lookup by package CITY")
                        print("\tz - Lookup by package ZIP")
                        print("\tw - Lookup by package WEIGHT")
                        print("\ts - Lookup by package STATUS")
                        print("")
                        query_type = input(">")

                    # If the user wants to return ALL packages
                    if (query_type == "a"):
                        # Set that will hold packages that have been delievered up to the given time
                        filtered_packages = dict()

                        for package_id in sorted(package_status_over_time["DELIVERED_TIMES"]):
                            if (time.strptime(package_status_over_time["DELIVERED_TIMES"][package_id], "%H:%M:%S") <= selected_time):
                                delivered_time = package_status_over_time["DELIVERED_TIMES"][package_id]
                                package_handler.get_package_by_id(str(package_id)).set_status(
                                    'DELIVERED (' + delivered_time + ')')
                                filtered_packages[int(package_id)] = package_handler.get_package_by_id(
                                    str(package_id))

                            elif ((time.strptime(package_status_over_time["DELIVERED_TIMES"][package_id], "%H:%M:%S") > selected_time) and (time.strptime(package_status_over_time["HUB_DEPARTURE"][package_id], "%H:%M:%S") <= selected_time)):
                                package_handler.get_package_by_id(
                                    str(package_id)).set_status('EN ROUTE')
                                filtered_packages[int(package_id)] = package_handler.get_package_by_id(
                                    str(package_id))

                            elif (time.strptime(package_status_over_time["HUB_DEPARTURE"][package_id], "%H:%M:%S") > selected_time):
                                package_handler.get_package_by_id(
                                    str(package_id)).set_status('AT THE HUB')
                                filtered_packages[int(package_id)] = package_handler.get_package_by_id(
                                    str(package_id))

                            else:
                                package_handler.get_package_by_id(
                                    str(package_id)).set_status('AT THE HUB')
                                filtered_packages[int(package_id)] = package_handler.get_package_by_id(
                                    str(package_id))

                        print("")
                        print(
                            f'\tAll Package Statuses as of {time.strftime("%H:%M", selected_time)}')
                        print("\t---------------------------------")

                        # Print out all the packages with their statuses to the user
                        for key in filtered_packages:
                            print(filtered_packages[key])

                        # Reset input to "b" to go back to the main menu
                        user_input = "b"

                    # If the user wants to return a package matching an index number
                    elif (query_type == "i"):
                        print("")
                        print("\tEnter the Target Package ID. Example: 14")
                        print("")
                        target_id = input(">")
                        print("")
                        # Set that will hold packages that have been delievered up to the given time
                        delivered_packages = set()

                        # A list that will hold all the packages to be printed to the screen
                        final_package_status = list()

                        # Step through the delivery history, grabbing entries up until the specified time
                        # and placing them into the delivered_packages set
                        for i in range(0, int(user_input) + 1):
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])

                        # Get the package IDs of those packages that were not delivered (from above)
                        # these packages are assumbed to be IN TRANSIT as they have not been delivered.
                        # Setting the status to an emptry string will default them to IN TRANSIT,
                        # Otherwise, add the package as-is
                        for j in range(1, 41):
                            if str(j) not in delivered_packages:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                package.set_status("")
                                final_package_status.append(str(package))
                            else:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                final_package_status.append(str(package))

                        package_filtered_by_id = ""
                        for package in final_package_status:
                            if (package.split(",")[0] == target_id):
                                package_filtered_by_id = package
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]} with ID [{target_id}]:")
                        print("\t--------------------------------------------------")

                        # Print out all the packages with their statuses to the user
                        if (package_filtered_by_id != ""):
                            print(f"\t{package_filtered_by_id}")
                        else:
                            print("\tNo packages found with that criteria.")

                        # Reset input to "b" to go back to the main menu
                        user_input = "b"

                    # If the user wants to return a package matching an address
                    elif (query_type == "r"):
                        print("")
                        print(
                            "\tEnter the Target Package ADDRESS. Example: 4300 S 1300 E")
                        print("")
                        target_address = input(">")
                        print("")

                        # Set that will hold packages that have been delievered up to the given time
                        delivered_packages = set()

                        # A list that will hold all the packages to be printed to the screen
                        final_package_status = list()

                        # Step through the delivery history, grabbing entries up until the specified time
                        # and placing them into the delivered_packages set
                        for i in range(0, int(user_input) + 1):
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])

                        # Get the package IDs of those packages that were not delivered (from above)
                        # these packages are assumbed to be IN TRANSIT as they have not been delivered.
                        # Setting the status to an emptry string will default them to IN TRANSIT,
                        # Otherwise, add the package as-is
                        for j in range(1, 41):
                            if str(j) not in delivered_packages:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                package.set_status("")
                                final_package_status.append(str(package))
                            else:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                final_package_status.append(str(package))

                        packages_filtered_by_address = list()
                        for package in final_package_status:
                            if (package.split(",")[3].strip() == target_address):
                                packages_filtered_by_address.append(package)
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]} with ADDRESS [{target_address}]:")
                        print("\t--------------------------------------------------")

                        # Print out all the packages with their statuses to the user
                        if (len(packages_filtered_by_address) != 0):
                            for pack in packages_filtered_by_address:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")

                        # Reset input to "b" to go back to the main menu
                        user_input = "b"

                    # If the user wants to return a package matching a deadline
                    elif (query_type == "d"):
                        print("")
                        print(
                            "\tEnter the Target Package DEADLINE. Example: 10:30 AM")
                        print("")
                        target_deadline = input(">")
                        print("")

                        # Set that will hold packages that have been delievered up to the given time
                        delivered_packages = set()

                        # A queue that will hold all the packages to be printed to the screen
                        final_package_status = list()

                        # Step through the delivery history, grabbing entries up until the specified time
                        # and placing them into the delivered_packages set
                        for i in range(0, int(user_input) + 1):
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                        for j in range(1, 41):
                            if str(j) not in delivered_packages:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                package.set_status("")
                                final_package_status.append(str(package))
                            else:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                final_package_status.append(str(package))

                        # A list to hold the deadlines grabbed from final_package_status
                        packages_filtered_by_deadline = list()

                        # Add the packages who's status match the target status into the deadline list
                        for package in final_package_status:
                            if (package.split(",")[4].strip() == target_deadline):
                                packages_filtered_by_deadline.append(package)
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]} with DEADLINE [{target_deadline}]:")
                        print("\t--------------------------------------------------")

                        # Print out all the packages with their statuses to the user
                        if (len(packages_filtered_by_deadline) != 0):
                            for pack in packages_filtered_by_deadline:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")

                        # Reset input to "b" to go back to the main menu
                        user_input = "b"

                    # If the user wants to return a package matching a city
                    elif (query_type == "c"):
                        print("")
                        print(
                            "\tEnter the Target Package DELIVERY_CITY. Example: Salt Lake City")
                        print("")
                        target_city = input(">")
                        print("")

                        # Set that will hold packages that have been delievered up to the given time
                        delivered_packages = set()

                        # A queue that will hold all the packages to be printed to the screen
                        final_package_status = list()

                        # Step through the delivery history, grabbing entries up until the specified time
                        # and placing them into the delivered_packages set
                        for i in range(0, int(user_input) + 1):
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])

                        # Get the package IDs of those packages that were not delivered (from above)
                        # these packages are assumbed to be IN TRANSIT as they have not been delivered.
                        # Setting the status to an emptry string will default them to IN TRANSIT,
                        # Otherwise, add the package as-is
                        for j in range(1, 41):
                            if str(j) not in delivered_packages:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                package.set_status("")
                                final_package_status.append(str(package))
                            else:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                final_package_status.append(str(package))

                        packages_filtered_by_city = list()

                        # Step through the packages and grab only the ones where the city matches
                        # the user input
                        for package in final_package_status:
                            if (package.split(",")[5].strip() == target_city):
                                packages_filtered_by_city.append(package)
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]} with DELIVERY_CITY [{target_city}]:")
                        print("\t--------------------------------------------------")

                        # Print out all the packages with their statuses to the user
                        if (len(packages_filtered_by_city) != 0):
                            for pack in packages_filtered_by_city:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")

                        # Reset input to "b" to go back to the main menu
                        user_input = "b"

                    # If the user wants to return a package matching a zip
                    elif (query_type == "z"):
                        print("")
                        print(
                            "\tEnter the Target Package DELIVERY_ZIP. Example: 84117")
                        print("")
                        target_zip = input(">")
                        print("")

                        # Set that will hold packages that have been delievered up to the given time
                        delivered_packages = set()

                        # A queue that will hold all the packages to be printed to the screen
                        final_package_status = list()

                        # Step through the delivery history, grabbing entries up until the specified time
                        # and placing them into the delivered_packages set
                        for i in range(0, int(user_input) + 1):
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])

                        # Get the package IDs of those packages that were not delivered (from above)
                        # these packages are assumbed to be IN TRANSIT as they have not been delivered.
                        # Setting the status to an emptry string will default them to IN TRANSIT,
                        # Otherwise, add the package as-is
                        for j in range(1, 41):
                            if str(j) not in delivered_packages:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                package.set_status("")
                                final_package_status.append(str(package))
                            else:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                final_package_status.append(str(package))

                        packages_filtered_by_zip = list()
                        for package in final_package_status:
                            if (package.split(",")[6].strip() == target_zip):
                                packages_filtered_by_zip.append(package)
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]} with DELIVERY_ZIP [{target_zip}]:")
                        print("\t--------------------------------------------------")

                        # Print out all the packages with their statuses to the user
                        if (len(packages_filtered_by_zip) != 0):
                            for pack in packages_filtered_by_zip:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")

                        # Reset input to "b" to go back to the main menu
                        user_input = "b"

                    # If the user wants to return a package matching a certain weight
                    elif (query_type == "w"):
                        print("")
                        print(
                            "\tEnter the Target Package WEIGHT. Example: 7")
                        print("")
                        target_weight = input(">")
                        print("")

                        # Set that will hold packages that have been delievered up to the given time
                        delivered_packages = set()

                        # A queue that will hold all the packages to be printed to the screen
                        final_package_status = list()

                        # Step through the delivery history, grabbing entries up until the specified time
                        # and placing them into the delivered_packages set
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])

                        # Get the package IDs of those packages that were not delivered (from above)
                        # these packages are assumbed to be IN TRANSIT as they have not been delivered.
                        # Setting the status to an emptry string will default them to IN TRANSIT,
                        # Otherwise, add the package as-is
                        for j in range(1, 41):
                            if str(j) not in delivered_packages:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                package.set_status("")
                                final_package_status.append(str(package))
                            else:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                final_package_status.append(str(package))

                        packages_filtered_by_weight = list()
                        for package in final_package_status:
                            if (package.split(",")[7].strip() == target_weight):
                                packages_filtered_by_weight.append(package)
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]} with WEIGHT [{target_weight}]:")
                        print("\t--------------------------------------------------")

                        # Print out all the packages with their statuses to the user
                        if (len(packages_filtered_by_weight) != 0):
                            for pack in packages_filtered_by_weight:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")

                        # Reset input to "b" to go back to the main menu
                        user_input = "b"

                    # If the user wants to return a package matching a certain status
                    elif (query_type == "s"):
                        print("")
                        print(
                            "\tEnter the Target Package STATUS. Example: IN TRANSIT (or DELIVERED)")
                        print("")
                        target_status = input(">")
                        print("")

                        # Set that will hold packages that have been delievered up to the given time
                        delivered_packages = set()

                        # A list that will hold all the packages to be printed to the screen
                        final_package_status = list()

                        # Step through the delivery history, grabbing entries up until the specified time
                        # and placing them into the delivered_packages set
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])

                        # Get the package IDs of those packages that were not delivered (from above)
                        # these packages are assumbed to be IN TRANSIT as they have not been delivered.
                        # Setting the status to an emptry string will default them to IN TRANSIT,
                        # Otherwise, add the package as-is
                        for j in range(1, 41):
                            if str(j) not in delivered_packages:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                package.set_status("")
                                final_package_status.append(str(package))
                            else:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                final_package_status.append(str(package))

                        packages_filtered_by_status = list()
                        for package in final_package_status:
                            if (target_status in package.split(",")[1].strip()):
                                packages_filtered_by_status.append(package)
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]} with STATUS [{target_status}]:")
                        print("\t--------------------------------------------------")

                        # Print out all the packages with their statuses to the user
                        if (len(packages_filtered_by_status) != 0):
                            for pack in packages_filtered_by_status:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")

                        # Reset input to "b" to go back to the main menu
                        user_input = "b"

                # elif(user_input == "b"):
                #    # Setting the user_input to an empty strill will restart the program
                #    user_input = ""
                # else:
                #    print("")
                #   print("\tInvalid input. What would you like to do next?")
