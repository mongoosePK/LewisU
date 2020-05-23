## Ryan Melody, Kevin Morgan, Sebastian Calderon, Aleksey Grinash, Krista Robinson
## Due 12/15/2014
## PlanetaryInformation.py
## CIS 1400 Logic and Technique Mon/Wed 10AM
## Creates a window that displays information about the planets in our solar system.
## Also allows the user to find their weight and age on each planet.
########
###!!!!NOTE FOR PROFESSOR ENGLAND!!!!###
#Do NOT use tab to go between the input boxes. It treats it as input, not as
#a switch-to-next-input button as usual.


from tkinter import *

####APPLICATION CLASS
#This class creates the window and defines widgets.
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        #blank planet as current planet until something is clicked
        #so it doesn't freak out if you hit convert before clicking a planet
        self.currentPlanet = Planet("0","0","0","0","0","0","0","0","0")      
        
        
########        
    ##### Planet defining. Due to python restrictions, I had to move it inside the application class.
    #Mercury
    def planet1(self):
        self.mercury = Planet("Mercury is named after the Roman deity Mercury, the messenger of the gods. Also known in Greek mythology as Hermes.",\
                         "58d 15h 30m",\
                         "88",\
                         "35,980,000",\
                         "0.38",\
                         "-280F (night) 800F (day)",\
                         "42% Molecular Oxygen; 29.0% Sodium; 22.0% Hydrogen; 6.0% Helium; 0.5% Potassium",\
                         "0.241",\
                         "0.38")
        self.planetaryInfo(self.mercury)
        self.currentPlanet = self.mercury
        #change image
        self.planetImage = PhotoImage(file = 'planet1.gif')
        self.planetImageLabel["image"] = self.planetImage
    ####
    #Venus
    def planet2(self):
        self.venus = Planet("Venus is named after the Roman goddess of love and beauty Venus; Also known in Greek mythology as Aphrodite.",\
                         "116d 18h",\
                         "225",\
                         "67,240,000",\
                         "0.9",\
                         "863",\
                         "96.5% Carbon Dioxide; 3.5% Nitrogen; 0.015% Sulfur dioxide; 0.007% Argon",\
                         "0.615",\
                         "0.91")
        self.planetaryInfo(self.venus)
        self.currentPlanet = self.venus
        #change image
        self.planetImage = PhotoImage(file = 'planet2.gif')
        self.planetImageLabel["image"] = self.planetImage
    ####
    #Earth
    def planet3(self):
        self.earth = Planet("All of the planets get their names from Greek and/or Roman gods, except for Earth which comes from the English or German name for ground.",\
                         "24h",\
                         "365",\
                         "92,960,000",\
                         "1.0",\
                         "-128.56 -- 159.26",\
                         "78.08% Nitrogen; 20.95% Oxygen; 0.930% Argon; 0.039% Carbon Dioxide",\
                         "1.0",\
                         "1.0")
        self.planetaryInfo(self.earth)
        self.currentPlanet = self.earth
        self.planetImage = PhotoImage(file = 'planet3.gif')
        self.planetImageLabel["image"] = self.planetImage
    ####
    #Mars
    def planet4(self):
        self.mars = Planet("Named after the Roman God of War, also known in Greek mythology as Ares.",\
                         "1d 40m",\
                         "687",\
                         "141,600,000",\
                         "0.38",\
                         "-225 -- 95",\
                         "95.75% Carbon Dioxide; 1.93% Argon; 1.89% Nitrogen; 0.146% Oxygen",\
                         "1.88",\
                         "0.38")
        self.planetaryInfo(self.mars)
        self.currentPlanet = self.mars
        self.planetImage = PhotoImage(file = 'planet4.gif')
        self.planetImageLabel["image"] = self.planetImage
    ####
    #Jupiter
    def planet5(self):
        self.jupiter = Planet("Named after the Roman god Jupiter whose Greek equivalent is Zeus.",\
                         "9h 56m",\
                         "12",\
                         "483,800,000",\
                         "2.364",\
                         "(N/A)",\
                         "89.8% Hydrogen; 10.2% Helium; 0.3% Methane; 0.026% Ammonia",\
                         "12",\
                         "2.364")
        self.planetaryInfo(self.jupiter)
        self.currentPlanet = self.jupiter
        self.planetImage = PhotoImage(file = 'planet5.gif')
        self.planetImageLabel["image"] = self.planetImage
    ####
    #Saturn
    def planet6(self):
        self.saturn = Planet("Named after the Roman god Saturn whose Greek equivalent is Kronos",\
                         "10h 39m",\
                         "29",\
                         "890,700,000",\
                         "1.07",\
                         "(N/A)",\
                         "96.5% Carbon Dioxide; 3.5% Nitrogen; 0.015% Sulfur dioxide; 0.007% Argon",\
                         "29",\
                         "1.07")
        self.planetaryInfo(self.saturn)
        self.currentPlanet = self.saturn
        self.planetImage = PhotoImage(file = 'planet6.gif')
        self.planetImageLabel["image"] = self.planetImage
    ####
    #Uranus
    def planet7(self):
        self.uranus = Planet("Only planet whose name is of Greek mythological origin (latinized Ouranos) Greek god of the sky.",\
                         "17h 14m",\
                         "84",\
                         "1,787,000,000",\
                         "0.91",\
                         "(N/A)",\
                         "83% Hydrogen; 15% Helium; 2.3% Methane; 0.009% Elemental Hydrogen",\
                         "84",\
                         "0.91")
        self.planetaryInfo(self.uranus)
        self.currentPlanet = self.uranus
        self.planetImage = PhotoImage(file = 'planet7.gif')
        self.planetImageLabel["image"] = self.planetImage
    ####
    #Neptune
    def planet8(self):
        self.neptune = Planet("Named after the Roman god of the sea.",\
                         "16h 6m",\
                         "164.8",\
                         "2,800,000,000",\
                         "1.14",\
                         "Average of 328.64",\
                         "96.5% Carbon Dioxide; 3.5% Nitrogen; 0.015% Sulfur dioxide; 0.007% Argon",\
                         "0.44",\
                         "1.14")
        self.planetaryInfo(self.neptune)
        self.currentPlanet = self.neptune
        self.planetImage = PhotoImage(file = 'planet8.gif')
        self.planetImageLabel["image"] = self.planetImage
########
    #Widget defining, places things in the window.
    def createWidgets(self):
        self.headerLabel = Label(self)
        self.headerLabel["text"] = "Planetary Info"
        self.headerLabel.grid(row = 0, column = 2, pady = 20)
        ####
        # Planet buttons
        #
        self.buttonMercury = Button(self)
        self.buttonMercury["text"] = "Mercury"
        self.buttonMercury["command"] = self.planet1
        self.buttonMercury.grid(row = 1, column = 0, padx = 20)
        #
        self.buttonVenus = Button(self)
        self.buttonVenus["text"] = "Venus"
        self.buttonVenus["command"] = self.planet2
        self.buttonVenus.grid(row = 2, column = 0)
        #
        self.buttonEarth = Button(self)
        self.buttonEarth["text"] = "Earth"
        self.buttonEarth["command"] = self.planet3
        self.buttonEarth.grid(row = 3, column = 0)
        #
        self.buttonMars = Button(self)
        self.buttonMars["text"] = "Mars"
        self.buttonMars["command"] = self.planet4
        self.buttonMars.grid(row = 4, column = 0)
        #
        self.buttonJupiter = Button(self)
        self.buttonJupiter["text"] = "Jupiter"
        self.buttonJupiter["command"] = self.planet5
        self.buttonJupiter.grid(row = 5, column = 0)
        #
        self.buttonSaturn = Button(self)
        self.buttonSaturn["text"] = "Saturn"
        self.buttonSaturn["command"] = self.planet6
        self.buttonSaturn.grid(row = 6, column = 0)
        #
        self.buttonUranus = Button(self)
        self.buttonUranus["text"] = "Uranus"
        self.buttonUranus["command"] = self.planet7
        self.buttonUranus.grid(row = 7, column = 0)
        #
        self.buttonNeptune = Button(self)
        self.buttonNeptune["text"] = "Neptune"
        self.buttonNeptune["command"] = self.planet8
        self.buttonNeptune.grid(row = 8, column = 0)
        ####
        # Info body
        # NOTE: To clear and set text to something else, do .delete(1.0, END)
        self.infoBodyText = Text(self, width = 40, height = 10)
        self.infoBodyText.grid(row = 1, column = 1, rowspan = 8, columnspan = 3, padx = 20, sticky = W)
        self.infoBodyText.insert(END, "Please select a planet!")
        ####
        # Planet age labels
        #
        self.inputAgeLabel = Label(self)
        self.inputAgeLabel["text"] = "Your age:"
        self.inputAgeLabel.grid(row = 9, column = 1)
        #
        self.inputAgeText = Text(self, width = 6, height = 1)
        self.inputAgeText.grid(row = 10, column = 1)
        #
        self.outputAgeLabel = Label(self)
        self.outputAgeLabel["text"] = " Age on this planet: "
        self.outputAgeLabel.grid(row = 11, column = 1, padx = 20)
        #
        self.outputAgeText = Text(self, width = 6, height = 1)
        self.outputAgeText.grid(row = 12, column = 1)
        ####
        # Planet weight labels
        #
        self.inputWeightLabel = Label(self)
        self.inputWeightLabel["text"] = "Your weight:"
        self.inputWeightLabel.grid(row = 9, column = 3)
        #
        self.inputWeightText = Text(self, width = 6, height = 1)
        self.inputWeightText.grid(row = 10, column = 3)
        #
        self.outputWeightLabel = Label(self)
        self.outputWeightLabel["text"] = "Weight on this planet:"
        self.outputWeightLabel.grid(row = 11, column = 3, padx = 20)
        #                
        self.outputWeightText = Text(self, width = 6, height = 1)
        self.outputWeightText.grid(row = 12, column = 3)
        ####
        # Age/weight conversion button
        #
        self.conversionButton = Button(self)
        self.conversionButton["text"] = "CONVERT"
        self.conversionButton["command"] = self.conversionButton_Click
        self.conversionButton.grid(row = 11, column = 2)
        ####
        # Planet image container
        self.planetImage = PhotoImage(file = 'planet0.gif')  
        self.planetImageLabel = Label(self, image = self.planetImage,\
                                      width = '50', height = '50')
        self.planetImageLabel.grid(row = 0, column = 3, pady = 20)
                                              
########
    #Called whenever a planet button is clicked. Displays info.
    def planetaryInfo(self, planet):
        self.infoBodyText.delete(1.0, END)
        self.infoBodyText.insert(END, planet.getNameOrigin() )
        self.infoBodyText.insert(END, "\n\nThis planet's year is: " + str(planet.getPlanetYear()) + " Earth days.")
        self.infoBodyText.insert(END, "\n\nThe length of day is: " + str(planet.getPlanetDay()))
        self.infoBodyText.insert(END, "\n\nDistance from the sun is: " + str(planet.getPlanetDistance()) + " mi.")
        self.infoBodyText.insert(END, "\n\nThis planet's gravity is: " + str(planet.getPlanetGravity()) + " that of Earth.")
        self.infoBodyText.insert(END, "\n\nAverage temperature range is: " + str(planet.getPlanetTemp()) + " F")
        self.infoBodyText.insert(END, "\n\nAtmospheric Composition is: " + str(planet.getPlanetAtmosphere()))
########
    #Called when convert button is clicked
    def conversionButton_Click(self):
        #Determine which constants to use
        weightPlanetValue = float(self.currentPlanet.getWeightConstant())
        agePlanetValue = float(self.currentPlanet.getAgeConstant())
        #local variabels
        age = 0.0
        realAge = 0.0
        weight = 0.0
        realWeight = 0.0
        #get input
        age = float(self.inputAgeText.get(1.0, END))
        weight = float(self.inputWeightText.get(1.0, END))
        #calculate age
        realAge = age / agePlanetValue
        realWeight = weight * weightPlanetValue
        #display in output boxes
        self.outputAgeText.delete(1.0, END)
        self.outputWeightText.delete(1.0, END)
        self.outputAgeText.insert(END, realAge)
        self.outputWeightText.insert(END, realWeight)
    
########
#####PLANET CLASS
#This class is for containing information about planets.
class Planet:
    def __init__(self, origin, day, year, distance, gravity, temp, atmosphere, ageCon, weightCon):
        self.__nameOrigin = origin
        self.__planetDay = day
        self.__planetYear = year
        self.__planetDistance = distance
        self.__planetGravity = gravity
        self.__planetTemp = temp
        self.__planetAtmosphere = atmosphere
        self.__ageConstant = ageCon
        self.__weightConstant = weightCon
    ####
    #Mutator methods
    def setNameOrigin(self, origin):
        self.__nameOrigin = origin
            
    def setPlanetDay(self, day):
        self.__planetDay = day
        
    def setPlanetYear(self, year):
        self.__planetYear = year
        
    def setPlanetDistance(self, distance):
        self.__planetDistance = distance
        
    def setPlanetGravity(self, gravity):
        self.__planetGravity = gravity
        
    def setPlanetTemp(self, temp):
        self.__planetTemp = temp
        
    def setPlanetAtmosphere(self, atmosphere):
        self.__planetAtmosphere = atmosphere
        
    def setAgeConstant(self, ageCon):
        self.__ageConstant = ageCon
        
    def setWeightConstant(self, weightCon):
        self.__weightConstant = weightCon
    ####
    #Accessor methods
    def getNameOrigin(self):
        return self.__nameOrigin
        
    def getPlanetDay(self):
        return self.__planetDay
        
    def getPlanetYear(self):
        return self.__planetYear
        
    def getPlanetDistance(self):
        return self.__planetDistance
        
    def getPlanetGravity(self):
        return self.__planetGravity
        
    def getPlanetTemp(self):
        return self.__planetTemp
        
    def getPlanetAtmosphere(self):
        return self.__planetAtmosphere
        
    def getAgeConstant(self):
        return self.__ageConstant
        
    def getWeightConstant(self):
        return self.__weightConstant

########
def main():
    #Define the window and prepare it for creation
    window = Tk()
    window.title("Planetary Info")
    window.geometry("480x400")

    app = Application(window)

    window.mainloop()


main()


