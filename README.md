# Data Structures and Algorithms II – C950

## WGUPS Routing Program

This is a project specified by WGU to solve a package delivery routing problem, which is essentially the traveling salesman problem with a dedicated starting node and a few restrictions/requirements. For my solution, I implemented the nearest neighbor algorithm which operates with a time-complexity of O(n).

## Usage

To get the code run this from the command line:

```commandline
git clone https://github.com/joshmadakor1/C950.git
```

Once that is done, in the main directory where `main.py` is located run:

```commandline
python3 main.py
```

depending on python version^^^

From there you should see the Command Line Interface like this:

```commandline
nnamdimadakor@nnamdis-Mac-mini C950 % python3 Main.py

	What would you like to do?

	d - Begin Delivery Simulation and Package Information Lookup
	q - Quit

>d

	Beginning delivery simulation...

	During deliver, new information has come in about package #9!
	Would you like to correct the address for package #9? Enter 'y' or 'n'
>y
	Package #9's address has been updated to: 410 S State St., Salt Lake City, UT 84111!

	Truck1 metrics:
	-----------------------------------
	Departure Time: 2021-07-01 08:00:00
	Return Time:    2021-07-01 10:05:40
	Drive Time:     2.09 hours
	Total Distance: 37.7 miles

	Truck2 metrics:
	-----------------------------------
	Departure Time: 2021-07-01 08:00:00
	Return Time:    2021-07-01 10:05:00
	Drive Time:     2.08 hours
	Total Distance: 37.5 miles

	Truck2 metrics (2nd trip):
	-----------------------------------
	Departure Time: 2021-07-01 10:05:00
	Return Time:    2021-07-01 11:59:00
	Drive Time:     1.9 hours
	Total Distance: 34.2 miles

	Truck3 metrics:
	----------------------------------
	Departure Time: 2021-07-01 10:05:40
	Return Time:    2021-07-01 11:13:00
	Drive Time:     1.12 hours
	Total Distance: 20.2 miles

	Combined mileage all trucks:  129.6 miles
	Time to deliver all packages: 3.99 hours

	Delivery simulation complete.

	What would you like to do next?

	p - Package Information Lookup
	b - Back to Main Menu

>p

	For up to what time would you like to view package information?
	Type the number next to the time period and press [Enter].

	 0 - 08:06:20	 1 - 08:08:00	 2 - 08:12:20	 3 - 08:13:00
	 4 - 08:13:00	 5 - 08:13:00	 6 - 08:29:40	 7 - 08:29:40
	 8 - 08:36:20	 9 - 08:39:00	10 - 08:48:00	11 - 08:48:00
	12 - 08:48:20	13 - 08:51:20	14 - 09:02:20	15 - 09:21:40
	16 - 09:21:40	17 - 09:27:00	18 - 09:28:20	19 - 09:28:40
	20 - 09:33:20	21 - 09:53:40	22 - 09:53:40	23 - 10:11:40
	24 - 10:13:40	25 - 10:19:20	26 - 10:19:40	27 - 10:24:00
	28 - 10:29:20	29 - 10:35:20	30 - 10:35:20	31 - 10:38:40
	32 - 10:38:40	33 - 10:39:00	34 - 10:44:00	35 - 10:51:20
	36 - 10:54:40	37 - 10:58:00	38 - 11:36:20	39 - 11:37:40 (and later)

>13

	How would you like to query packages?

	a - Show ALL package statuses as of 08:51:20
	i - Lookup by package ID
	r - Lookup by package ADDRESS
	d - Lookup by package DEADLINE
	c - Lookup by package CITY
	z - Lookup by package ZIP
	w - Lookup by package WEIGHT
	s - Lookup by package STATUS

>a

	All Package Statuses as of 08:51:20
	---------------------------------
	1, DELIVERED (08:36:20), South Salt Lake Public Works, 195 W Oakland Ave, 10:30 AM, Salt Lake City, 84115, 21
	2, IN TRANSIT, Columbus Library, 2530 S 500 E, EOD, Salt Lake City, 84106, 44
	3, DELIVERED (08:51:20), Salt Lake City Ottinger Hall, 233 Canyon Rd, EOD, Salt Lake City, 84103, 2
	4, IN TRANSIT, Utah DMV Administrative Office, 380 W 2880 S, EOD, Salt Lake City, 84115, 4
	5, IN TRANSIT, Third District Juvenile Court, 410 S State St, EOD, Salt Lake City, 84111, 5
	6, IN TRANSIT, Redwood Park, 3060 Lester St, 10:30 AM, West Valley City, 84119, 88
	7, DELIVERED (08:29:40), Sugar House Park, 1330 2100 S, EOD, Salt Lake City, 84106, 8
	8, IN TRANSIT, Council Hall, 300 State St, EOD, Salt Lake City, 84103, 9
	9, IN TRANSIT, Third District Juvenile Court, 410 S State St, EOD, Salt Lake City, 84111, 2
	10, DELIVERED (08:39:00), Rice Terrace Pavilion Park, 600 E 900 South, EOD, Salt Lake City, 84105, 1
	11, IN TRANSIT, Taylorsville City Hall, 2600 Taylorsville Blvd, EOD, Salt Lake City, 84118, 1
	12, IN TRANSIT, West Valley Prosecutor, 3575 W Valley Central Station bus Loop, EOD, West Valley City, 84119, 1
	13, IN TRANSIT, Salt Lake City Streets and Sanitation, 2010 W 500 S, 10:30 AM, Salt Lake City, 84104, 2
	14, DELIVERED (08:06:20), Cottonwood Regional Softball Complex, 4300 S 1300 E, 10:30 AM, Millcreek, 84117, 88
	15, DELIVERED (08:13:00), Holiday City Office, 4580 S 2300 E, 9:00 AM, Holladay, 84117, 4
	16, DELIVERED (08:13:00), Holiday City Office, 4580 S 2300 E, 10:30 AM, Holladay, 84117, 88
	17, IN TRANSIT, Salt Lake County Mental Health, 3148 S 1100 W, EOD, Salt Lake City, 84119, 2
	18, IN TRANSIT, Taylorsville-Bennion Heritage City Gov Off, 1488 4800 S, EOD, Salt Lake City, 84123, 6
	19, IN TRANSIT, Salt Lake City Division of Health Services, 177 W Price Ave, EOD, Salt Lake City, 84115, 37
	20, IN TRANSIT, Housing Auth. of Salt Lake County, 3595 Main St, 10:30 AM, Salt Lake City, 84115, 37
	21, IN TRANSIT, Housing Auth. of Salt Lake County, 3595 Main St, EOD, Salt Lake City, 84115, 3
	22, DELIVERED (08:12:20), Wheeler Historic Farm, 6351 South 900 East, EOD, Murray, 84121, 2
	23, IN TRANSIT, Valley Regional Softball Complex, 5100 South 2700 West, EOD, Salt Lake City, 84118, 5
	24, IN TRANSIT, Murray City Museum, 5025 State St, EOD, Murray, 84107, 7
	25, DELIVERED (08:08:00), City Center of Rock Springs, 5383 South 900 East #104, 10:30 AM, Salt Lake City, 84117, 7
	26, IN TRANSIT, City Center of Rock Springs, 5383 South 900 East #104, EOD, Salt Lake City, 84117, 25
	27, IN TRANSIT, International Peace Gardens, 1060 Dalton Ave S, EOD, Salt Lake City, 84104, 5
	28, IN TRANSIT, South Salt Lake Police, 2835 Main St, EOD, Salt Lake City, 84115, 7
	29, DELIVERED (08:29:40), Sugar House Park, 1330 2100 S, 10:30 AM, Salt Lake City, 84106, 2
	30, DELIVERED (08:48:20), Council Hall, 300 State St, 10:30 AM, Salt Lake City, 84103, 1
	31, IN TRANSIT, Salt Lake County/United Police Dept, 3365 S 900 W, 10:30 AM, Salt Lake City, 84119, 1
	32, IN TRANSIT, Salt Lake County/United Police Dept, 3365 S 900 W, EOD, Salt Lake City, 84119, 1
	33, IN TRANSIT, Columbus Library, 2530 S 500 E, EOD, Salt Lake City, 84106, 1
	34, DELIVERED (08:13:00), Holiday City Office, 4580 S 2300 E, 10:30 AM, Holladay, 84117, 2
	35, IN TRANSIT, International Peace Gardens, 1060 Dalton Ave S, EOD, Salt Lake City, 84104, 88
	36, IN TRANSIT, Deker Lake, 2300 Parkway Blvd, EOD, West Valley City, 84119, 88
	37, DELIVERED (08:48:00), Third District Juvenile Court, 410 S State St, 10:30 AM, Salt Lake City, 84111, 2
	38, DELIVERED (08:48:00), Third District Juvenile Court, 410 S State St, EOD, Salt Lake City, 84111, 9
	39, IN TRANSIT, Salt Lake City Streets and Sanitation, 2010 W 500 S, EOD, Salt Lake City, 84104, 9
	40, IN TRANSIT, Utah DMV Administrative Office, 380 W 2880 S, 10:30 AM, Salt Lake City, 84115, 45

	What would you like to do?

	d - Begin Delivery Simulation and Package Information Lookup
	q - Quit

>q
```

## INTRODUCTION

```text
For this assessment, you will apply the algorithms and data structures you studied in this course to solve a real programming problem. You will implement an algorithm to route
delivery trucks that will allow you to meet all delivery deadlines while traveling the least number of miles. You will also describe and justify the decisions you made while creating
this program.

The skills you showcase in your completed project may be useful in responding to technical interview questions for future employment. This project may also be added to your
portfolio to show to future employers.
```

## SCENARIO

```text
The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution for their Daily Local Deliveries (DLD) because packages
are not currently being consistently delivered by their promised deadline. The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver
each day; each package has specific criteria and delivery requirements.

Your task is to determine the best algorithm, write code, and present a solution where all 40 packages, listed in the attached “WGUPS Package File,” will be delivered on time
with the least number of miles added to the combined mileage total of all trucks. The specific delivery locations are shown on the attached “Salt Lake City Downtown Map” and
distances to each location are given in the attached “WGUPS Distance Table.”

While you work on this assessment, take into consideration the specific delivery time expected for each package and the possibility that the delivery requirements—including the
expected delivery time—can be changed by management at any time and at any point along the chosen route. In addition, you should keep in mind that the supervisor should be
able to see, at assigned points, the progress of each truck and its packages by any of the variables listed in the “WGUPS Package File,” including what
has been delivered and what time the delivery occurred.

The intent is to use this solution (program) for this specific location and to use the same program in many cities in each state where WGU has a presence. As such, you will need to
include detailed comments, following the industry-standard Python style guide, to make your code easy to read and to justify the decisions you made while writing your program.
```

#### Assumptions

- Each truck can carry a maximum of 16 packages.
- Trucks travel at an average speed of 18 miles per hour.
- Trucks have a “infinite amount of gas” with no need to stop.
- Each driver stays with the same truck as long as that truck is in service.
- Drivers leave the hub at 8:00 a.m., with the truck loaded, and can return to the hub for packages if needed. The day ends when all 40 packages have been delivered.
- Delivery time is instantaneous, i.e., no time passes while at a delivery (that time is factored into the average speed of the trucks).
- There is up to one special note for each package.
- The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is 410 S State St., Salt Lake City, UT 84111.
- The package ID is unique; there are no collisions.
- No further assumptions exist or are allowed.

## REQUIREMENTS

```text
Your submission must be your original work. No more than a combined total of 30% of the submission and no more than a 10% match to any one individual source can be directly
quoted or closely paraphrased from sources, even if cited correctly. An originality report is provided when you submit your task that can be used as a guide.

You must use the rubric to direct the creation of your submission because it provides detailed criteria that will be used to evaluate your work. Each requirement below may be
evaluated by more than one rubric aspect. The rubric aspect titles may contain hyperlinks to relevant portions of the course.

Section 1: Programming/Coding


    A. Identify the algorithm that will be used to create a program to deliver the packages and meets all  requirements specified in the scenario.

    B.  Write a core algorithm overview, using the sample given, in which you do the following:

        1.  Comment using pseudocode to show the logic of the algorithm applied to this software solution.

        2.  Apply programming models to the scenario.

        3.  Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.

        4.  Discuss the ability of your solution to adapt to a changing market and to scalability.

        5.  Discuss the efficiency and maintainability of the software.

        6.  Discuss the self-adjusting data structures chosen and their strengths and weaknesses based on the scenario.

    C.  Write an original code to solve and to meet the requirements of lowest mileage usage and having all  packages delivered on time.

        1.  Create a comment within the first line of your code that includes your first name, last name, and student ID.

        2.  Include comments at each  block of code to explain the process and flow of the coding.

    D.  Identify a data structure that can be used with your chosen algorithm to store the package data.

        1.  Explain how your data structure includes the relationship between the data points you are storing.

        Note: Do NOT use any existing data structures. You must design, write, implement, and debug all code that you turn in for this assessment. Code downloaded from the internet or acquired from another student or any other source may not be submitted and will result in automatic failure of this assessment.

    E.  Develop a hash table, without using any additional libraries or classes, with an insertion function that takes the following components as input and inserts the components into the hash table:

        •  package ID number

        •  delivery address

        •  delivery deadline

        •  delivery city

        •  delivery zip code

        •  package weight

        •  delivery status (e.g., delivered, in route)

    F.  Develop a look-up function that takes the following components as input and returns the corresponding data elements:

        •  package ID number

        •  delivery address

        •  delivery deadline

        •  delivery city

        •  delivery zip code

        •  package weight

        •  delivery status (e.g., delivered, in route)

    G.  Provide an interface for the insert and look-up functions to view the status of any package at any time. This function should return all information about each package, including delivery status.

        1.  Provide screenshots to show package status of all packages at a time between 8:35 a.m. and 9:25 a.m.

        2.  Provide screenshots to show package status of all packages at a time between 9:35 a.m. and 10:25 a.m.

        3.  Provide screenshots to show package status of all packages at a time between 12:03 p.m. and 1:12 p.m.

    H.  Run your code and provide screenshots to capture the complete execution of your code.


Section 2: Annotations


    I.  Justify your choice of algorithm by doing the following:

        1.  Describe at least  two strengths of the algorithm you chose.

        2.  Verify that the algorithm you chose meets all  the criteria and requirements given in the scenario.

        3.  Identify two other algorithms that could be used and would have met the criteria and requirements given in the scenario.

            a.  Describe how each  algorithm identified in part I3 is different from the algorithm you chose to use in the solution.

    J.  Describe what you would do differently if you did this project again.

    K.  Justify your choice of data structure by doing the following:

        1.  Verify that the data structure you chose meets all  the criteria and requirements given in the scenario.

            a.  Describe the efficiency of the data structure chosen.

            b.  Explain the expected overhead when linking to the next data item.

            c.  Describe the implications of when more package data is added to the system or other changes in scale occur.

        2.  Identify two other data structures that can meet the same criteria and requirements given in the scenario.

            a.  Describe how each  data structure identified in part K2 is different from the data structure you chose to use in the solution.

    L.   Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.

    M.  Demonstrate professional communication in the content and presentation of your submission.
```
