from queue import PriorityQueue
from HashMap import HashMap
from PackageHandler import PackageHandler
from Graph import Graph
from Truck import Truck
from operator import itemgetter
import datetime
import _thread

# Used for storing package status over time
package_status_over_time = list()

# Initialize Graph Components
g = Graph()

# Initialize Packages
package_handler = PackageHandler()


def initialize_trucks():
    # Truck1: These packages must be delivered together per the rubric
    truck1.add_package(package_handler.get_package_by_id('13'))
    truck1.add_package(package_handler.get_package_by_id('14'))
    truck1.add_package(package_handler.get_package_by_id('15'))
    truck1.add_package(package_handler.get_package_by_id('16'))
    truck1.add_package(package_handler.get_package_by_id('19'))
    truck1.add_package(package_handler.get_package_by_id('20'))
    # Truck1:  -- Deadline 10:30 AM -- #
    truck1.add_package(package_handler.get_package_by_id('29'))
    truck1.add_package(package_handler.get_package_by_id('1'))
    truck1.add_package(package_handler.get_package_by_id('30'))
    truck1.add_package(package_handler.get_package_by_id('31'))
    # Truck1: -- Remaining Capacity in same Zips
    truck1.add_package(package_handler.get_package_by_id('8'))
    truck1.add_package(package_handler.get_package_by_id('17'))
    truck1.add_package(package_handler.get_package_by_id('12'))
    truck1.add_package(package_handler.get_package_by_id('22'))
    truck1.add_package(package_handler.get_package_by_id('7'))
    truck1.add_package(package_handler.get_package_by_id('2'))

    # "Can only be on truck 2" per the rubric
    truck2.add_package(package_handler.get_package_by_id('3'))
    truck2.add_package(package_handler.get_package_by_id('18'))
    truck2.add_package(package_handler.get_package_by_id('36'))
    truck2.add_package(package_handler.get_package_by_id('38'))
    # -- Deadline 10:30 AM -- #
    truck2.add_package(package_handler.get_package_by_id('40'))
    truck2.add_package(package_handler.get_package_by_id('37'))
    truck2.add_package(package_handler.get_package_by_id('34'))
    # Truck2: -- Remaining Capacity in same Zip
    truck2.add_package(package_handler.get_package_by_id('24'))
    truck2.add_package(package_handler.get_package_by_id('27'))
    truck2.add_package(package_handler.get_package_by_id('35'))
    truck2.add_package(package_handler.get_package_by_id('39'))

    # "Delayed on flight---will not arrive to depot until 9:05 am"
    truck3.add_package(package_handler.get_package_by_id('6'))
    truck3.add_package(package_handler.get_package_by_id('25'))
    truck3.add_package(package_handler.get_package_by_id('28'))
    truck3.add_package(package_handler.get_package_by_id('32'))
    # -- Address will be updated by this time (incorrect address package)
    truck3.add_package(package_handler.get_package_by_id('9'))
    # -- Remaining Packages
    truck3.add_package(package_handler.get_package_by_id('10'))
    truck3.add_package(package_handler.get_package_by_id('4'))
    truck3.add_package(package_handler.get_package_by_id('5'))
    truck3.add_package(package_handler.get_package_by_id('11'))
    truck3.add_package(package_handler.get_package_by_id('21'))
    truck3.add_package(package_handler.get_package_by_id('23'))
    truck3.add_package(package_handler.get_package_by_id('26'))
    truck3.add_package(package_handler.get_package_by_id('33'))

    # Calculate optimal routes for the three loaded up trucks
    # g.node_list contains informations on the edges/nodes that will
    # be used in conjunction with the packages on each truck.
    truck1.calculate_best_delivery_route(g.node_list)
    truck2.calculate_best_delivery_route(g.node_list)
    truck3.calculate_best_delivery_route(g.node_list)


def initialize_graph():
    g.initialize_location_name_data()
    g.initialize_location_distance_data()
    g.initialize_nodes_hashmap()


# Initialize Trucks with their ids
truck1 = Truck("1")
truck2 = Truck("2")
truck3 = Truck("3")
initialize_graph()
initialize_trucks()


def delivery_simulation(package_status_over_time):
    # Build a time object: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    eight_am = datetime.datetime(2021, 7, 1, 8, 0, 0, 0)

    # Deliver Packages (Truck1)
    # Departure Time: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    # truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
    truck1_return_metrics = truck1.deliver_packages(
        eight_am, package_handler, package_status_over_time)

    # Deliver Packages (Truck2)
    # Departure Time: 2021-07-01 08:00:00 (July 1, 2021, 8:00 AM)
    # truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
    truck2_return_metrics = truck2.deliver_packages(
        eight_am, package_handler, package_status_over_time)

    # Deliver Packages (Truck3)
    # Departure Time: Immediately after truck2 returns
    # truck*_return_metrics = [return_time, drive_time_in_hours, drive_distance]
    truck3_return_metrics = truck3.deliver_packages(
        truck2_return_metrics[0], package_handler, package_status_over_time)

    # Sort the packages by time delivered
    package_status_over_time = sorted(
        package_status_over_time, key=itemgetter(0))

    total_miles_driven = round(float(
        truck1_return_metrics[2] + truck2_return_metrics[2] + truck3_return_metrics[2]), 2)
    time_to_deliver_all_packages = round(
        float(truck2_return_metrics[1] + truck3_return_metrics[1]), 2)

    print("")
    print("Truck1 metrics:")
    print("-----------------------------------")
    print(f"Departure Time: {eight_am}")
    print(f"Return Time:    {truck1_return_metrics[0]}")
    print(f"Drive Time:     {round(float(truck1_return_metrics[1]),2)} hours")
    print(f"Total Distance: {round(float(truck1_return_metrics[2]),2)} miles")
    print(f"")
    print("Truck2 metrics:")
    print("-----------------------------------")
    print(f"Departure Time: {eight_am}")
    print(f"Return Time:    {truck2_return_metrics[0]}")
    print(f"Drive Time:     {round(float(truck2_return_metrics[1]),2)} hours")
    print(f"Total Distance: {round(float(truck2_return_metrics[2]),2)} miles")
    print(f"")
    print("Truck3 metrics:")
    print("----------------------------------")
    print(f"Departure Time: {truck2_return_metrics[0]}")
    print(f"Return Time:    {truck3_return_metrics[0]}")
    print(f"Drive Time:     {round(float(truck3_return_metrics[1]),2)} hours")
    print(f"Total Distance: {round(float(truck3_return_metrics[2]),2)} miles")
    print(f"")
    print(f"Combined mileage all trucks:  {total_miles_driven}")
    print(f"Time to deliver all packages: {time_to_deliver_all_packages}")
    initialize_graph()
    initialize_trucks()


user_input = ""
while (user_input != "q"):
    print("")
    print("What would you like to do?")
    print("")
    print("d - Delivery Simulation and Package Information Lookup")
    print("q - Quit")
    print("")
    user_input = input(">").lower()

    if (user_input == "d"):
        print("")
        print("Beginning delivery simulation...")
        print("")
        delivery_simulation(package_status_over_time)
        print("")
        print(
            "Delivery simulation complete. What would you like to do next?")
        while (user_input != "q"):
            print("")
            print("p - Package Information Lookup")
            print("q - Back to main menu")
            print("")
            user_input = input(">").lower()

            if (user_input == "p"):
                print("")
                print("For what time period would you like to view package information?")
                print(
                    "Type the number next to the time period and press [Enter].")
                print("")
                print(
                    f" 0 - {package_status_over_time[0][0]}\t 1 - {package_status_over_time[1][0]}\t 2 - {package_status_over_time[2][0]}\t 3 - {package_status_over_time[3][0]}")
                print(
                    f" 4 - {package_status_over_time[4][0]}\t 5 - {package_status_over_time[5][0]}\t 6 - {package_status_over_time[6][0]}\t 7 - {package_status_over_time[7][0]}")
                print(
                    f" 8 - {package_status_over_time[8][0]}\t 9 - {package_status_over_time[9][0]}\t10 - {package_status_over_time[10][0]}\t11 - {package_status_over_time[11][0]}")
                print(
                    f"12 - {package_status_over_time[12][0]}\t13 - {package_status_over_time[13][0]}\t14 - {package_status_over_time[14][0]}\t15 - {package_status_over_time[15][0]}")
                print(
                    f"16 - {package_status_over_time[16][0]}\t17 - {package_status_over_time[17][0]}\t18 - {package_status_over_time[18][0]}\t19 - {package_status_over_time[19][0]}")
                print(
                    f"20 - {package_status_over_time[20][0]}\t21 - {package_status_over_time[21][0]}\t22 - {package_status_over_time[22][0]}\t23 - {package_status_over_time[23][0]}")
                print(
                    f"24 - {package_status_over_time[24][0]}\t25 - {package_status_over_time[25][0]}\t26 - {package_status_over_time[26][0]}\t27 - {package_status_over_time[27][0]}")
                print(
                    f"28 - {package_status_over_time[28][0]}\t29 - {package_status_over_time[29][0]}\t30 - {package_status_over_time[30][0]}\t31 - {package_status_over_time[31][0]}")
                print(
                    f"32 - {package_status_over_time[32][0]}\t33 - {package_status_over_time[33][0]}\t34 - {package_status_over_time[34][0]}\t35 - {package_status_over_time[35][0]}")
                print(
                    f"36 - {package_status_over_time[36][0]}\t37 - {package_status_over_time[37][0]}\t38 - {package_status_over_time[38][0]}\t39 - {package_status_over_time[39][0]}")
                print("")
                user_input = input(">").lower()

                if (user_input.isnumeric and int(user_input) >= 0 and int(user_input) <= 39):
                    print("")

                    for i in range(0, int(user_input)):
                        print(
                            f"{package_status_over_time[i][0]} - {package_status_over_time[i][1]}")

            else:
                print("")
                print("Invalid input. What would you like to do next?")
