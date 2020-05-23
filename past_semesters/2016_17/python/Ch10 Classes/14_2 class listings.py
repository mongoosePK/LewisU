##Author: William Pulkownik
##16 Nov 2015
##14_2 Class listing.py

class CellPhone :
##    Python NOTE : __init__ method automatically executed when instance is
##    created and is used to define attributes/fields. (double underscore
##    auto executes)
    def __init__(self, manufact, model, retail) :
        ##use 'self.' object notation because self is object argument
        self.__manufacturer = manufact
        self.__modelNumber = model
        self.__retailPrice = retail

    ## mutator methods
    def setManufacturer(self, manufact) :
        self.__manufacturer = manufact
    def setModelNumber(self, model) :
        self.__modelNumber = model
    def setRetailPrice(self, retail) :
        self.__retailPrice = retail

    ## accessor functions 'getters'
    def getManufacturer(self) :
        return self.__manufacturer
    def getModelNumber(self) :
        return self.__modelNumber
    def getRetailPrice(self) :
        return self.__retailPrice

##Behavior/method to make phone call
    def makeCall(self, phNumber) :
        print('Calling.....', phNumber)
        print('Call made by ', self.__manufacturer, self.__modelNumber)

##main module to test CellPhone class
def main() :
    myPhone = CellPhone('Samsung', 'Galaxy S4', 700.00)
    print('The manufacturer is ', myPhone.getManufacturer())
    print('The model is ', myPhone.getModelNumber())
    print('The retail price is ', myPhone.getRetailPrice())
    myPhone.makeCall('416-4603')
main()
