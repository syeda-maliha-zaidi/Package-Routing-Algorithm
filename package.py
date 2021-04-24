
# Package data object representation
# Makes storing and retreiving information about a package simpler
class Package:
    def __init__(self, csvPackageDataRow):
        self._id       = int(csvPackageDataRow[0])
        self._address  = csvPackageDataRow[1]
        self._city     = csvPackageDataRow[2]
        self._state    = csvPackageDataRow[3]
        self._zip_code = csvPackageDataRow[4]
        self._deadline = csvPackageDataRow[5]
        self._mass     = csvPackageDataRow[6]
        self._notes    = csvPackageDataRow[7]
        self._status   = "At HUB"
        self._tod      = "0:00" #Time of delivery

    def __hash__(self):
        return self._id

    def getID(self):
        return self._id

    def getAddress(self):
        return self._address

    def getCity(self):
        return self._city

    def getState(self):
        return self._state

    def getZipCode(self):
        return self._zip_code

    def getDeadline(self):
        return self._deadline

    def getMass(self):
        return self._mass

    def getNotes(self):
        return self._notes;

    def getStatus(self):
        return self._status

    def getTimeOfDelivery(self):
        return self._tod

    def setAddress(self, newAddress):
        self._address = newAddress

    def setZipCode(self, newZipCode):
        self._zip_code = newZipCode

    def setStatus(self, newStatus):
        self._status = newStatus

    def setTimeOfDelivery(self, newTOD):
        self._tod = newTOD

    def printDataHeader(self):
        print("{0:<5s}\
            {1:<67s}\
            {2:<15s}\
            {3:<5s}\
            {4:<60s}\
            {5:<20s}".
            format("ID", "Address", "Deadline", "Mass (kg)", "Notes", "Time of Delivery/Status")
        )

    def __repr__(self):
        full_address = "{0}, {1}, {2} {3}".format(self._address, self._city, self._state, self._zip_code)
        return "{0:<5s}\
            {1:<67s}\
            {2:<15s}\
            {3:<5s}\
            {4:<60s}\
            {5:<20s}\
            ".format( 
                str(self._id),
                full_address,
                self._deadline,
                str(self._mass),
                self._notes,
                "{0}/{1}".format(self._tod,self._status)
            )

    def __str__(self):
        full_address = "{0}, {1}, {2} {3}".format(self._address, self._city, self._state, self._zip_code)
        return "{0:<5s}\
            {1:<67s}\
            {2:<15s}\
            {3:<5s}\
            {4:<60s}\
            {5:<20s}\
            ".format( 
                str(self._id),
                full_address,
                self._deadline,
                str(self._mass),
                self._notes,
                "{0}/{1}".format(self._tod,self._status)
            )