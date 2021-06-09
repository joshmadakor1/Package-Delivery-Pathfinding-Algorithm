from PackageHandler import PackageHandler
from Graph import Graph
from Truck import Truck
from operator import itemgetter
from queue import Queue
import datetime

# TODO: BIG-O notation
# TODO: make searching case insensitive

# Used for storing package status over time
package_status_over_time = list()

# Initialize Graph Components
g = Graph()

# Initialize Packages
package_handler = PackageHandler()

# O(N)
# Add packages to the truck and optimizes delivery route


def initialize_truck1():
    # These are the package ids for the packages that this truck will deliver
    truck1_packages = {'13', '14', '10', '34', '32', '31',
                       '40', '4', '30', '12', '7', '29', '20', '19', '16', '15'}

    # O(N)
    # Add the packages to the truck
    for package in truck1_packages:
        truck1.add_package(package_handler.get_package_by_id(package))

    # Calculate optimal routes for the three loaded up trucks
    # g.adjacency_matrix contains informations on the edges/nodes
    truck1.optimize_delivery_route(g.adjacency_matrix)

# O(N)
# Add packages to the truck and optimizes delivery route


def initialize_truck2():
    # These are the package ids for the packages that this truck will deliver
    truck2_packages = {'1', '3', '22', '25', '18', '37', '38'}

    # O(N)
    # Add the packages to the truck
    for package in truck2_packages:
        truck2.add_package(package_handler.get_package_by_id(package))

    # Calculate optimal routes for the three loaded up trucks
    # g.adjacency_matrix contains informations on the edges/nodes
    truck2.optimize_delivery_route(g.adjacency_matrix)

# O(N)
# Add packages to the truck and optimizes delivery route


def initialize_truck2_2nd_trip():

    # These are the package ids for the packages that this truck will deliver
    truck2_2nd_trip_packages = {'6', '36', '17',
                                '5', '8', '11', '23', '39', '27', '35', '21'}

    # O(N)
    # Add the packages to the truck
    for package in truck2_2nd_trip_packages:
        truck2_2nd_trip.add_package(package_handler.get_package_by_id(package))

    # Calculate optimal routes for the three loaded up trucks
    # g.adjacency_matrix contains informations on the edges/nodes
    truck2_2nd_trip.optimize_delivery_route(g.adjacency_matrix)

# O(N)
# Add packages to the truck and optimizes delivery route


def initialize_truck3():

    # These are the package ids for the packages that this truck will deliver
    truck3_trip_packages = {'9', '26', '2', '33', '28', '24', }

    # O(N)
    # Add the packages to the truck
    for package in truck3_trip_packages:
        truck3.add_package(package_handler.get_package_by_id(package))

    # Calculate optimal routes for the three loaded up trucks
    # g.adjacency_matrix contains informations on the edges/nodes
    truck3.optimize_delivery_route(g.adjacency_matrix)

# O(N)
# Reads in data from the CSV files and stores the information
# This information will be used to formulate optimized delivery maps


def initialize_graph():
    g.initialize_location_name_data()
    g.initialize_location_distance_data()
    g.initialize_nodes_hashmap()


# Initialize Trucks with their ids
initialize_graph()
truck1 = Truck("1")
truck2 = Truck("2")
truck2_2nd_trip = Truck("2-2nd-trip")
truck3 = Truck("3")
initialize_truck1()
initialize_truck2()
initialize_truck2_2nd_trip()
initialize_truck3()

# Keep track of whether or not Package 9's address has been updated
package_9_has_been_updated = False

# O(N)
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
    package_status_over_time.clear()
    # Build a time object: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    eight_am = datetime.datetime(2021, 7, 1, 8, 0, 0, 0)

    # Deliver Packages (Truck1)
    # Departure Time: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    # truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
    truck1_return_metrics = truck1.deliver_packages(
        eight_am, package_handler, package_status_over_time, package_9_has_been_updated)

    # Deliver Packages (Truck2)
    # Departure Time: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    # truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
    truck2_return_metrics = truck2.deliver_packages(
        eight_am, package_handler, package_status_over_time, truck1_return_metrics[3])

    # Deliver Packages (Truck2(second trip))
    # Departure Time: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    # truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
    truck2_2nd_trip_return_metrics = truck2_2nd_trip.deliver_packages(
        truck2_return_metrics[0], package_handler, package_status_over_time, truck2_return_metrics[3])

    # Deliver Packages (Truck3)
    # Departure Time: Immediately after truck2 returns
    # truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
    # Calculate the best route for truck three if changes occurred
    # Re-initialize Truck3 to account for if Package #9 had its address updated
    truck3.delivery_nodes = set()
    initialize_truck3()
    truck3_return_metrics = truck3.deliver_packages(
        truck1_return_metrics[0], package_handler, package_status_over_time, truck2_2nd_trip_return_metrics[3])

    # Sort package_status_over_time by time delivered. This will be used to see the status
    # throughout the delivery lifecycle
    package_status_over_time = sorted(
        package_status_over_time, key=itemgetter(0))

    # Calculate the total miles driven by all three trucks
    total_miles_driven = round(float(
        truck1_return_metrics[2] + truck2_return_metrics[2] + truck2_2nd_trip_return_metrics[2] + truck3_return_metrics[2]), 2)

    # Calculate the total time it took to deliver all the packages by
    time_to_deliver_all_packages = round(
        float(truck1_return_metrics[1] + truck2_2nd_trip_return_metrics[1]), 2)

    # Print out Delivery metrics/outcome to the screen
    print("")
    print("\tTruck1 metrics:")
    print("\t-----------------------------------")
    print(f"\tDeparture Time: {eight_am}")
    print(f"\tReturn Time:    {truck1_return_metrics[0]}")
    print(
        f"\tDrive Time:     {round(float(truck1_return_metrics[1]),2)} hours")
    print(
        f"\tTotal Distance: {round(float(truck1_return_metrics[2]),2)} miles")
    print(f"")
    print("\tTruck2 metrics:")
    print("\t-----------------------------------")
    print(f"\tDeparture Time: {eight_am}")
    print(f"\tReturn Time:    {truck2_return_metrics[0]}")
    print(
        f"\tDrive Time:     {round(float(truck2_return_metrics[1]),2)} hours")
    print(
        f"\tTotal Distance: {round(float(truck2_return_metrics[2]),2)} miles")
    print(f"")
    print("\tTruck2 metrics (2nd trip):")
    print("\t-----------------------------------")
    print(f"\tDeparture Time: {truck2_return_metrics[0]}")
    print(f"\tReturn Time:    {truck2_2nd_trip_return_metrics[0]}")
    print(
        f"\tDrive Time:     {round(float(truck2_2nd_trip_return_metrics[1]),2)} hours")
    print(
        f"\tTotal Distance: {round(float(truck2_2nd_trip_return_metrics[2]),2)} miles")
    print("")
    print("\tTruck3 metrics:")
    print("\t----------------------------------")
    print(f"\tDeparture Time: {truck1_return_metrics[0]}")
    print(f"\tReturn Time:    {truck3_return_metrics[0]}")
    print(
        f"\tDrive Time:     {round(float(truck3_return_metrics[1]),2)} hours")
    print(
        f"\tTotal Distance: {round(float(truck3_return_metrics[2]),2)} miles")
    print(f"")
    print(f"\tCombined mileage all trucks:  {total_miles_driven} miles")
    print(
        f"\tTime to deliver all packages: {time_to_deliver_all_packages} hours")

    # Rebuild the graph in case it has changed due to package updates
    initialize_graph()

    # Rebuild the trucks' routes in case they have changed due to package updates
    initialize_truck1()
    initialize_truck2()
    initialize_truck2_2nd_trip()
    initialize_truck3()

    # Clear package_status_over_time, allowing it to be repopulated when the
    # delivery simulation runs again
    package_status_over_time = list()


# Run the user interface
user_input = ""
while (user_input != "q"):
    print("")
    print("\tWhat would you like to do?")
    print("")
    print("\td - Begin Delivery Simulation and Package Information Lookup")
    print("\tq - Quit")
    print("")
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

            if (user_input == "p"):
                while (not user_input.isnumeric()):
                    # Sort the packages by time delivered
                    package_status_over_time = sorted(
                        package_status_over_time, key=itemgetter(0))
                    print("")
                    print(
                        "\tFor up to what time would you like to view package information?")
                    print(
                        "\tType the number next to the time period and press [Enter].")
                    print("")
                    print(
                        f"\t 0 - {package_status_over_time[0][0]}\t 1 - {package_status_over_time[1][0]}\t 2 - {package_status_over_time[2][0]}\t 3 - {package_status_over_time[3][0]}")
                    print(
                        f"\t 4 - {package_status_over_time[4][0]}\t 5 - {package_status_over_time[5][0]}\t 6 - {package_status_over_time[6][0]}\t 7 - {package_status_over_time[7][0]}")
                    print(
                        f"\t 8 - {package_status_over_time[8][0]}\t 9 - {package_status_over_time[9][0]}\t10 - {package_status_over_time[10][0]}\t11 - {package_status_over_time[11][0]}")
                    print(
                        f"\t12 - {package_status_over_time[12][0]}\t13 - {package_status_over_time[13][0]}\t14 - {package_status_over_time[14][0]}\t15 - {package_status_over_time[15][0]}")
                    print(
                        f"\t16 - {package_status_over_time[16][0]}\t17 - {package_status_over_time[17][0]}\t18 - {package_status_over_time[18][0]}\t19 - {package_status_over_time[19][0]}")
                    print(
                        f"\t20 - {package_status_over_time[20][0]}\t21 - {package_status_over_time[21][0]}\t22 - {package_status_over_time[22][0]}\t23 - {package_status_over_time[23][0]}")
                    print(
                        f"\t24 - {package_status_over_time[24][0]}\t25 - {package_status_over_time[25][0]}\t26 - {package_status_over_time[26][0]}\t27 - {package_status_over_time[27][0]}")
                    print(
                        f"\t28 - {package_status_over_time[28][0]}\t29 - {package_status_over_time[29][0]}\t30 - {package_status_over_time[30][0]}\t31 - {package_status_over_time[31][0]}")
                    print(
                        f"\t32 - {package_status_over_time[32][0]}\t33 - {package_status_over_time[33][0]}\t34 - {package_status_over_time[34][0]}\t35 - {package_status_over_time[35][0]}")
                    print(
                        f"\t36 - {package_status_over_time[36][0]}\t37 - {package_status_over_time[37][0]}\t38 - {package_status_over_time[38][0]}\t39 - {package_status_over_time[39][0]} (and later)")
                    print("")
                    user_input = input(">").lower()

                if (user_input.isnumeric() and int(user_input) >= 0 and int(user_input) <= 39):
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
                        delivered_packages = set()

                        # A queue that will hold all the packages to be printed to the screen
                        final_package_status = Queue()

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
                                final_package_status.put(package)
                            else:
                                package = package_handler.get_package_by_id(
                                    str(j))
                                final_package_status.put(package)
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]}")
                        print("\t---------------------------------")

                        # Print out all the packages with their statuses to the user
                        while(final_package_status.qsize() > 0):
                            print(f"\t{final_package_status.get()}")

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

                elif(user_input == "b"):
                    user_input = ""
                else:
                    print("")
                    print("\tInvalid input. What would you like to do next?")
