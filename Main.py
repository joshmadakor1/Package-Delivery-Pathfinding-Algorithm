from queue import PriorityQueue
from typing import final
from HashMap import HashMap
from PackageHandler import PackageHandler
from Graph import Graph
from Truck import Truck
from operator import itemgetter
import datetime
import time
from Package import Package
from queue import Queue
# TODO: FIX Reporting of total drive time
# TODO: Delivery times are not in order for some reason when displaying (Al)
# Used for storing package status over time
package_status_over_time = list()

# Initialize Graph Components
g = Graph()

# Initialize Packages
package_handler = PackageHandler()


def initialize_truck1():
    # Truck1: These packages must be delivered together per the rubric
    truck1.add_package(package_handler.get_package_by_id('13'))
    truck1.add_package(package_handler.get_package_by_id('14'))
    truck1.add_package(package_handler.get_package_by_id('15'))
    truck1.add_package(package_handler.get_package_by_id('16'))
    truck1.add_package(package_handler.get_package_by_id('19'))
    truck1.add_package(package_handler.get_package_by_id('20'))
    truck1.add_package(package_handler.get_package_by_id('29'))
    truck1.add_package(package_handler.get_package_by_id('7'))

    truck1.add_package(package_handler.get_package_by_id('12'))
    truck1.add_package(package_handler.get_package_by_id('30'))

    truck1.add_package(package_handler.get_package_by_id('4'))
    truck1.add_package(package_handler.get_package_by_id('40'))
    truck1.add_package(package_handler.get_package_by_id('31'))
    truck1.add_package(package_handler.get_package_by_id('32'))
    truck1.add_package(package_handler.get_package_by_id('34'))
    truck1.add_package(package_handler.get_package_by_id('10'))

    # --29,7 Together
    # --13,39 together
    # --2,33 Together

    # Calculate optimal routes for the three loaded up trucks
    # g.node_list contains informations on the edges/nodes that will
    # be used in conjunction with the packages on each truck.
    truck1.calculate_best_delivery_route(g.node_list)


def initialize_truck2():
    # "Can only be on truck 2" per the rubric
    truck2.add_package(package_handler.get_package_by_id('1'))
    truck2.add_package(package_handler.get_package_by_id('3'))
    truck2.add_package(package_handler.get_package_by_id('22'))
    truck2.add_package(package_handler.get_package_by_id('25'))
    truck2.add_package(package_handler.get_package_by_id('18'))
    truck2.add_package(package_handler.get_package_by_id('37'))
    truck2.add_package(package_handler.get_package_by_id('38'))
    # --5,37,38 togehter
    # --40,4 together
    # --27,35 together
    # --8,30 together
    truck2.calculate_best_delivery_route(g.node_list)


def initialize_truck2_2nd_trip():
    # "Can only be on truck 2" per the rubric
    truck2_2nd_trip.add_package(package_handler.get_package_by_id('6'))
    truck2_2nd_trip.add_package(package_handler.get_package_by_id('36'))

    truck2_2nd_trip.add_package(package_handler.get_package_by_id('17'))

    truck2_2nd_trip.add_package(package_handler.get_package_by_id('5'))
    truck2_2nd_trip.add_package(package_handler.get_package_by_id('8'))
    truck2_2nd_trip.add_package(package_handler.get_package_by_id('11'))
    truck2_2nd_trip.add_package(package_handler.get_package_by_id('23'))
    truck2_2nd_trip.add_package(package_handler.get_package_by_id('39'))
    truck2_2nd_trip.add_package(package_handler.get_package_by_id('27'))
    truck2_2nd_trip.add_package(package_handler.get_package_by_id('35'))
    truck2_2nd_trip.add_package(package_handler.get_package_by_id('21'))
    # --5,37,38 togehter
    # --40,4 together
    # --27,35 together
    # --8,30 together
    truck2_2nd_trip.calculate_best_delivery_route(g.node_list)


def initialize_truck3():

    # "Delayed on flight---will not arrive to depot until 9:05 am"
    truck3.add_package(package_handler.get_package_by_id('9'))
    truck3.add_package(package_handler.get_package_by_id('26'))
    truck3.add_package(package_handler.get_package_by_id('2'))
    truck3.add_package(package_handler.get_package_by_id('33'))
    truck3.add_package(package_handler.get_package_by_id('28'))
    truck3.add_package(package_handler.get_package_by_id('24'))
    # --25,26 together
    # --2,33 together
    # --31,32 together
    # -- Address will be updated by this time (incorrect address package)
    # -- Remaining Packages

    # Calculate optimal routes for the three loaded up trucks
    # g.node_list contains informations on the edges/nodes that will
    # be used in conjunction with the packages on each truck.
    truck3.calculate_best_delivery_route(g.node_list)


def initialize_graph():
    g.initialize_location_name_data()
    g.initialize_location_distance_data()
    g.initialize_nodes_hashmap()


# Initialize Trucks with their ids
initialize_graph()
truck1 = Truck("1")
initialize_truck1()
truck2 = Truck("2")
initialize_truck2()
truck2_2nd_trip = Truck("2-2nd-trip")
initialize_truck2_2nd_trip()
truck3 = Truck("3")
initialize_truck3()

package_9_has_been_updated = False


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

    truck3.delivery_nodes = set()
    initialize_truck3()
    truck3_return_metrics = truck3.deliver_packages(
        truck1_return_metrics[0], package_handler, package_status_over_time, truck2_2nd_trip_return_metrics[3])

    # Sort the packages by time delivered
    package_status_over_time = sorted(
        package_status_over_time, key=itemgetter(0))

    total_miles_driven = round(float(
        truck1_return_metrics[2] + truck2_return_metrics[2] + truck2_2nd_trip_return_metrics[2] + truck3_return_metrics[2]), 2)
    time_to_deliver_all_packages = round(
        float(truck2_return_metrics[1] + truck3_return_metrics[1]), 2)

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

    # Rebuild the graph in case it has changed
    initialize_graph()

    # Rebuild the trucks' routes in case they have changed
    initialize_truck1()
    initialize_truck2()
    initialize_truck2_2nd_trip()
    initialize_truck3()

    # Clear this, allowing it to be repopulated when the deliver simulation runs again
    package_status_over_time = list()


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
                        f"\t36 - {package_status_over_time[36][0]}\t37 - {package_status_over_time[37][0]}\t38 - {package_status_over_time[38][0]}\t39 - {package_status_over_time[39][0]}")
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

                    if (query_type == "a"):
                        delivered_packages = set()
                        final_package_status = Queue()
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])
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
                        while(final_package_status.qsize() > 0):
                            print(f"\t{final_package_status.get()}")
                        user_input = "b"

                    elif (query_type == "i"):
                        print("")
                        print("\tEnter the Target Package ID. Example: 14")
                        print("")
                        target_id = input(">")
                        print("")
                        delivered_packages = set()
                        final_package_status = list()
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])
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
                        if (package_filtered_by_id != ""):
                            print(f"\t{package_filtered_by_id}")
                        else:
                            print("\tNo packages found with that criteria.")
                        user_input = "b"
                    elif (query_type == "r"):
                        print("")
                        print(
                            "\tEnter the Target Package ADDRESS. Example: 4300 S 1300 E")
                        print("")
                        target_address = input(">")
                        print("")
                        delivered_packages = set()
                        final_package_status = list()
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])
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
                        if (len(packages_filtered_by_address) != 0):
                            for pack in packages_filtered_by_address:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")
                        user_input = "b"
                    elif (query_type == "d"):
                        print("")
                        print(
                            "\tEnter the Target Package DEADLINE. Example: 10:30 AM")
                        print("")
                        target_deadline = input(">")
                        print("")
                        delivered_packages = set()
                        final_package_status = list()
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])
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

                        packages_filtered_by_deadline = list()
                        for package in final_package_status:
                            if (package.split(",")[4].strip() == target_deadline):
                                packages_filtered_by_deadline.append(package)
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]} with DEADLINE [{target_deadline}]:")
                        print("\t--------------------------------------------------")
                        if (len(packages_filtered_by_deadline) != 0):
                            for pack in packages_filtered_by_deadline:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")
                        user_input = "b"
                    elif (query_type == "c"):
                        print("")
                        print(
                            "\tEnter the Target Package DELIVERY_CITY. Example: Salt Lake City")
                        print("")
                        target_city = input(">")
                        print("")
                        delivered_packages = set()
                        final_package_status = list()
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])
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
                        for package in final_package_status:
                            if (package.split(",")[5].strip() == target_city):
                                packages_filtered_by_city.append(package)
                        print("")
                        print(
                            f"\tAll Package Statuses as of {package_status_over_time[int(user_input)][0]} with DELIVERY_CITY [{target_city}]:")
                        print("\t--------------------------------------------------")
                        if (len(packages_filtered_by_city) != 0):
                            for pack in packages_filtered_by_city:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")
                        user_input = "b"
                    elif (query_type == "z"):
                        print("")
                        print(
                            "\tEnter the Target Package DELIVERY_ZIP. Example: 84117")
                        print("")
                        target_zip = input(">")
                        print("")
                        delivered_packages = set()
                        final_package_status = list()
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])
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
                        if (len(packages_filtered_by_zip) != 0):
                            for pack in packages_filtered_by_zip:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")
                        user_input = "b"
                    elif (query_type == "w"):
                        print("")
                        print(
                            "\tEnter the Target Package WEIGHT. Example: 7")
                        print("")
                        target_weight = input(">")
                        print("")
                        delivered_packages = set()
                        final_package_status = list()
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])
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
                        if (len(packages_filtered_by_weight) != 0):
                            for pack in packages_filtered_by_weight:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")
                        user_input = "b"
                    elif (query_type == "s"):
                        print("")
                        print(
                            "\tEnter the Target Package STATUS. Example: IN TRANSIT (or DELIVERED)")
                        print("")
                        target_status = input(">")
                        print("")
                        delivered_packages = set()
                        final_package_status = list()
                        for i in range(0, int(user_input) + 1):
                            #print(f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")
                            delivered_packages.add((package_status_over_time[i][1])[
                                                   0:(package_status_over_time[i][1]).index(",")])
                            # final_package_status.add((package_status_over_time[i][1])[0:(package_status_over_time[i][1]).index(",")])
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
                        if (len(packages_filtered_by_status) != 0):
                            for pack in packages_filtered_by_status:
                                print(f"\t{pack}")
                        else:
                            print("\tNo packages found with that criteria.")
                        user_input = "b"
                    elif (query_type == "s"):
                        print("enter Status")
                        user_input = "b"

                elif(user_input == "b"):
                    user_input = ""
                else:
                    print("")
                    print("\tInvalid input. What would you like to do next?")
