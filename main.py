# Name: Syeda Zaidi 
# Student ID #: 000969487

from data_loader import *
from truck_loader import load_trucks
from utils import create_address_graph

# Runs simulation for each truck route and returns back the truck objects
# Complexity is O(N^2) due to call to truck startRoute function
def simulate_trucks(packages_data, address_graph):    

    truck_1, truck_2, truck_3 = load_trucks(packages_data)

    # Truck 1 leaves at 8 am
    truck_1_distance, truck_1_time = truck_1.startRoute( 480, address_graph )

    # Truck 2 leaves at 9:05 am, packages are loaded instantly and the delayed packages on the truck will arrive at 9:05 am
    truck_2_distance, truck_2_time = truck_2.startRoute( 545, address_graph )

    # Truck 3 leaves at 10:20 am
    truck_3_distance, truck_3_time = truck_3.startRoute( 620, address_graph )

    return truck_1, truck_2, truck_3

def main():
    address_data = load_address_data()
    distance_data = load_distance_data()
    packages_data = load_package_data() 

    address_graph = create_address_graph(address_data, distance_data)

    truck_1, truck_2, truck_3 = simulate_trucks(packages_data, address_graph)

    introduction_text = '''
        Welcome to the WGUPS Package Information System.
        -------------------------------------------------------
        The system allows for the following commands to be used:
        - Enter 1 to view delivery route information
        - Enter 2 to do a time (hh:mm) lookup of package status
        - Enter 3 to do a lookup of package by ID
        - Enter 4 to do a truck lookup by number
        - Enter 'exit' to stop the program

    '''

    command_input = ''
    while command_input != 'exit':
        command_input = input(introduction_text)

        # Retreive and print route info
        # Complexity is O(1)
        if command_input == '1':
            total_distance = truck_1.getDistanceTraveled() + truck_2.getDistanceTraveled() + truck_3.getDistanceTraveled()
            print("Truck 1 distance traveled: {0:.2f} miles in {1} minutes".format( truck_1.getDistanceTraveled(), truck_1.getTravelTime( truck_1.getDistanceTraveled() ) ) )
            print("Truck 2 distance traveled: {0:.2f} miles in {1} minutes".format( truck_2.getDistanceTraveled(), truck_2.getTravelTime( truck_2.getDistanceTraveled() ) ) )
            print("Truck 1 (Second Trip) distance traveled: {0:.2f} miles in {1} minutes".format( truck_3.getDistanceTraveled(), truck_3.getTravelTime( truck_3.getDistanceTraveled() ) ) )
            print("Combined distance traveled: %.2f miles" % total_distance)

        # Retreive and print all package data at a user specified time
        # Complexity is O(n)
        elif command_input == '2':
            start_time_input = input('Enter a start time (hh:mm): ')
            end_time_input = input('Enter a end time (hh:mm): ')

            already_delivered_packages = []
            delivered_packages = []
            not_delivered_packages = []

            all_packages = truck_1.getPackages() + truck_2.getPackages() + truck_3.getPackages()

            for package in all_packages:
                if package.getTimeOfDelivery() >= start_time_input and package.getTimeOfDelivery() <= end_time_input:
                    delivered_packages.append( package )
                elif package.getTimeOfDelivery() <= start_time_input:
                    already_delivered_packages.append( package )                    
                else:
                    not_delivered_packages.append(package)

            print("\nPackages delivered between {0} and {1}:".format( start_time_input, end_time_input) )

            all_packages[0].printDataHeader()

            for package in delivered_packages:
                print(package)

            print("\nPackages already delivered by {0}:".format( start_time_input) )

            all_packages[0].printDataHeader()

            for package in already_delivered_packages:
                print(package)

            print("\nPackages not yet delivered")

            all_packages[0].printDataHeader()
            
            for package in not_delivered_packages:
                print(package)

        # Query the system for package data using its ID
        # Complexity is O(1)
        elif command_input == '3':
            command_input = input('Enter a package id: ')

            try:
                package_id = int(command_input)

                if package_id not in range(1, len(packages_data) + 1):
                    raise

                package = packages_data.searchByKey(package_id)

                package.printDataHeader()
                print(package)
            except Exception:
                print("Invalid entry!")

        # Query the system for truck data using its ID
        # Complexity is O(1)
        elif command_input == '4':
            command_input = input('Enter a truck id (1-3): ')

            try:
                truck_id = int(command_input)

                if( truck_id < 1 or truck_id > 3 ):
                    raise
               
                if truck_id == 1:
                    print( truck_1 )
                elif truck_id == 2:
                    print( truck_2 )
                elif truck_id == 3:
                    print( truck_3 )
            except Exception:
                print("Invalid entry!")
        else:
            if command_input != 'exit':
                print("Invalid entry!")


if __name__ == '__main__':
    main()  