from utils import create_address_graph, minutes_to_time
from sys import maxsize 

# Truck data object representation
# Makes storing and retreiving information about a truck simpler
class Truck:
    def __init__(self, id, capacity, hubAddress):
        self._truck_id = id
        self._truck_capacity = capacity
        self._package_list = []
        self._distance_traveled = 0
        self._hub = hubAddress
        self._speed = 18

    def __hash__(self):
        return self._truck_id

    def getDistanceTraveled(self):
        return self._distance_traveled

    def setDistanceTraveled(self, dist):
        self._distance_traveled = dist

    def getPackages(self):
        return self._package_list

    def addPackage(self, package):
        self._package_list.append(package)

    # Checks if a truck has a package loaded with a certain address
    # Complexity is O(n)
    def hasPackageAtAddress(self, address):
        for package in self._package_list:
            if package.getAddress() == address:
                return True
        return False

    # Gets a list of packages loaded with a certain address
    # Complexity is O(n)
    def getPackagesAtAddress(self, address):
        packages = []
        for package in self._package_list:
            if package.getAddress() == address:
                packages.append( package )
        return packages

    # Checks if a truck has a package loaded with a certain id
    # Complexity is O(n)
    def hasPackage(self, package_id):
        for package in self._package_list:
            if package.getID() == package_id:
                return True
        return False

    # Gets a list of addresses a truck must visit based on the packages loaded
    # Complexity is O(n)
    def getListOfAddressesToVisit(self):
        addresses = []
        for package in self._package_list:
            addresses.append( package.getAddress() )
        return addresses

    # Computes the time to travel a distance
    # Complexity is O(1)
    def getTravelTime(self, distance):
        return int((distance / self._speed) * 60)

    # Computes the time to travel a distance
    # Complexity is O(1)
    def isFull(self):
        return len(self._package_list) == self._truck_capacity

    # Sets status of each package on the truck to "Out for Delivery"
    # Complexity is O(N^2)
    def startRoute(self, start_time, address_graph):
        for package in self._package_list:
            package.setStatus("Out for Delivery")       

        truck_route, total_dist = self._computeRoute(address_graph, self._package_list)

        travel_time = start_time

        for idx in range( 1, len( truck_route ) ):
            travel_distance = address_graph.getEdge( truck_route[idx-1], truck_route[idx] )
            travel_time += self.getTravelTime( travel_distance )

            packages_to_deliver = self.getPackagesAtAddress(truck_route[idx].label)

            for package in packages_to_deliver:
                package.setTimeOfDelivery( minutes_to_time(travel_time) )
                package.setStatus("Delivered")

        self.setDistanceTraveled( total_dist )

        return total_dist, (self.getTravelTime( total_dist )+480)

    # Computes the ideal route a truck should travel to deliver the packages traveling the least distance
    # Time complexity is O(N^3)
    def _computeRoute(self, graph, package_list):    
        
        # Time complexity is O(N^2)
        def _getNextLocation(graph, current_address, package_list):
            min_distance = maxsize
            next_package_to_deliver = None
            next_address = None

            current_location_vertex = graph.getVertex( current_address )

            # Time complexity is O(N^2)
            for package in package_list:
                package_vertex = graph.getVertex( package.getAddress() )
                edge_weight = graph.getEdge(current_location_vertex, package_vertex)

                if edge_weight < min_distance:
                    min_distance = edge_weight
                    next_package_to_deliver = package
                    next_address = package.getAddress()
                    
            return next_package_to_deliver, next_address, min_distance

        address_to_visit = self._hub
        hub_vertex = graph.getVertex(address_to_visit)
        total_route_dist = 0
        route = []

        route.append( hub_vertex )

        temp_list = list( package_list )

        # Time complexity is O(N^3)
        for i in range( len(package_list) ):
            next_package, address_to_visit, dist_to_travel = _getNextLocation(graph, address_to_visit, temp_list)

            temp_list.remove( next_package )

            total_route_dist += dist_to_travel

            route.append( graph.getVertex(address_to_visit) )

        # Add on the distance to get back home
        total_route_dist += graph.getEdge(hub_vertex, graph.getVertex(address_to_visit))

        route.append( hub_vertex )

        return route, total_route_dist

    def __repr__(self):
        return "\n\t\t\t(Truck) \n\
            ID: {0}\n\
            Package Count: {1}\n\
            Package IDs: {2}\n\
            ".format( 
                self._truck_id,
                len(self._package_list),
                str([package.getID() for package in self._package_list])
            )

    def __str__(self):
        return "\n\t\t\t(Truck) \n\
            ID: {0}\n\
            Package Count: {1}\n\
            Package IDs: {2}\n\
            ".format( 
                self._truck_id,
                len(self._package_list),
                str([package.getID() for package in self._package_list])
            )