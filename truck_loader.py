from truck import Truck

# Sorts the packages onto trucks 
# Complexity is O(n^2)
#
# General rules used to sort:
# Truck 1
#   - Packages with an early deadline
#   - Required delivery combinations
# Truck 2 
#   - Any delayed packages
#   - Packages required to be on truck 2
#   - Packages with an early deadline
# Truck 3 
#   - Remaining packages
#
# Fill Truck 3 first, 
# Then fill Truck 1
# Then fill Truck 2 since it has the shortest amount of time to complete its deliveries
def load_trucks(packages):
    truck_1 = Truck(1, 16, "4001 South 700 East")
    truck_2 = Truck(2, 16, "4001 South 700 East")
    truck_3 = Truck(3, 16, "4001 South 700 East")
        

    for package in packages:
        package_notes = package.getNotes()

        if package.getDeadline() != "EOD":
            if package_notes == "None" or 'Must' in package_notes:
                truck_1.addPackage( package )

        if "truck 2" in package_notes:
            truck_2.addPackage( package )

        if "Delayed" in package_notes:
            truck_2.addPackage( package )

        if "Wrong address" in package_notes:
            # Fix the address and put it on truck 3 because we won't get the new address until later in the morning
            package.setAddress('410 S State St')
            package.setZipCode('84111')
            truck_3.addPackage( package )

    # Sort remaining items based on if the truck already visits the address
    for package in packages:
        if truck_1.hasPackage( package.getID() ) or truck_2.hasPackage( package.getID() ) or truck_3.hasPackage( package.getID() ):
            continue

        if truck_1.hasPackageAtAddress( package.getAddress() ) and truck_1.isFull() == False:
            truck_1.addPackage( package )
        elif truck_2.hasPackageAtAddress( package.getAddress() ) and truck_2.isFull() == False:
            truck_2.addPackage( package )
        elif truck_3.hasPackageAtAddress( package.getAddress() ) and truck_3.isFull() == False:
            truck_3.addPackage( package )

    for package in packages:
        if truck_1.hasPackage( package.getID() ) or truck_2.hasPackage( package.getID() ) or truck_3.hasPackage( package.getID() ):
            continue

        if truck_3.isFull() == False:
            truck_3.addPackage( package )
        elif truck_1.isFull() == False:
            truck_1.addPackage( package )        
        elif truck_2.isFull() == False:
            truck_2.addPackage( package )
        
    
    return truck_1, truck_2, truck_3
