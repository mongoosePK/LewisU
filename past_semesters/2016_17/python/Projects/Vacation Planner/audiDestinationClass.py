##William Pulkownik
##CIS 1400 Team Audi
##5 dec 2015
##Destination class.py

from tkinter import*

class Destination :
    def __init__(self, place, acts, cost) :
        self.__location = place
        self.__activities = acts
        self.__ticketPrice = cost

    def setLocation(self, place) :
        self.__location = place
    def setActivities(self, acts) :
        self.__activities = acts
    def setTicketPrice(self, cost) :
        self.__ticketPrice = cost

    def getLocation(self) :
        return self.__location
    def getActivities(self) :
        return self.__activities
    def getTicketPrice(self) :
        return self.__ticketPrice

        
        

def main() :
    whitewater = Destination('Colorado', 'Whitewater Rafting', 5500.00)
    kayak = Destination('Naperville', 'Kayaking a river', 400.00)
    PI = Destination('Phillipines', 'Relax in the Archipelago Nation!', 7500.00)
    UP = Destination('Upper Peninsula, Michigan', 'Explore the Great Outdoors!',
                     1700.00)
    dudeRanch = Destination('Wyoming', 'Become a Cowboy!', 5300.00)
    appalachian = Destination('The Appalachian Trail', 'Hike the Smokies!',
                              2300.00)
    lakeTahoe = Destination('Sierra Nevada',
                            'Relax at the border of California and Nevada!',
                            6200.00)
    DC = Destination('Washington D.C.', 'Explore our Capitol!', 1500.00)
    iceFishing = Destination('Minnesota', 'Sit on a frozen lake!', 1200.00)
    alaska = Destination('Alaska', 'Explore the American Frontier!', 5100.00)
    wisconsin = Destination('Wisconsin', 'Snowboard close to home!', 450.00)
    everest = Destination('Mount Everest', 'Conquer the world\'s tallest peak!',
                          10000.00)
    print(PI.getLocation())
    print(PI.getTicketPrice())
main()
