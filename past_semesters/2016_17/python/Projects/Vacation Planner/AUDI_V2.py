## Team AUDI (Ariel Dumagan, Kevin DeLaby, Jonathan Hernandez, William Pulkownik)
## CIS 1400 Group project Fall 2015
## We designed a Vacation planner that takes user inputs and suggests destinations

from tkinter import *

####APPLICATION CLASS
#This class creates the window and defines widgets.
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        holder = Destination('0', '0', 0)

        self.whitewater = Destination('Colorado', 'Whitewater Rafting on the \
                                       Colorado River!', 5500.00)
        self.kayak = Destination('Aurora, IL', 'Kayak the Fox River!', 400.00)
        
        self.PI = Destination('Phillipines', 'Relax in the Archipelago Nation!',
                              7500.00)
        
        self.UP = Destination('Upper Peninsula, Michigan', 'Explore the Great Outdoors!',
                     1700.00)
        self.dudeRanch = Destination('Wyoming', 'Become a Cowboy!', 5300.00)
        self.appalachian = Destination('The Appalachian Trail', 'Hike the Smokies!',
                                  2300.00)
        self.lakeTahoe = Destination('Sierra Nevada',
                                'Relax at the border of California and Nevada!',
                                6200.00)
        self.DC = Destination('Washington D.C.', 'Explore our Capitol!', 1500.00)
        self.iceFishing = Destination('Minnesota', 'Sit on a frozen lake!', 1200.00)
        self.alaska = Destination('Alaska', 'Explore the American Frontier!', 5100.00)
        self.wisconsin = Destination('Wisconsin', 'Snowboard close to home!', 450.00)
        self.everest = Destination('Mount Everest', 'Conquer the world\'s \
                                    tallest peak!', 10000.00)
        

    def createWidgets(self):
        self.headerLabel = Label(self)
        self.headerLabel["text"] = 'Vacation Planner!'
        self.headerLabel.grid(row = 0, column = 2, pady = 20)

        self.springImage = PhotoImage(file = 'springG.gif')
        self.summerImage = PhotoImage(file = 'summerG.gif')
        self.fallImage = PhotoImage(file = 'fallG.gif')
        self.winterImage = PhotoImage(file = 'winterG.gif')

        #input labels
        self.cashLabel = Label(self,
                                text = 'How much can you spend?')
        self.cashTextBox = Entry(self, width = 10)
        self.cashLabel.grid(row = 1, column = 0)
        self.cashTextBox.grid(row = 1, column = 1)
        self.riskLabel = Label(self,
                                text = 'how much risk')
        self.riskTextBox = Entry(self, width = 10)
        self.riskLabel.grid(row = 2, column = 0)
        self.riskTextBox.grid(row = 2, column = 1)

        #season Buttons
        self.springButton = Button(self,
                                 image = self.springImage, width = 75,
                                 height = 50,
                                 command = self.temperateButton_Click)
        self.springButton.grid(row = 3, column = 0)
        #Summer
        self.summerButton = Button(self,
                                 image = self.summerImage, width = 75,
                                 height = 50,
                                 command = self.summerButton_Click)
        self.summerButton.grid(row = 3, column = 1)

        #Fall
        self.fallButton = Button(self,
                                 image = self.fallImage, width = 75,
                                 height = 50,
                                 command = self.temperateButton_Click)
        self.fallButton.grid(row = 3, column = 2)

        #Winter
        self.winterButton = Button(self,
                                 image = self.winterImage, width = 75,
                                 height = 50,
                                 command = self.winterButton_Click)
        self.winterButton.grid(row = 3, column = 3)

        #display
        self.resultArea = Text(self, width = 30, height = 10)
        self.resultArea.grid(row = 4, column = 1, rowspan = 8, columnspan = 3,
                             sticky = W)
        self.resultArea.insert(END, 'Help us get to know you. Fill the boxes!')
        
        #display function
    def result(self, destination) :
        self.resultArea.delete(1.0, END)
        self.resultArea.insert(END, destination.getLocation())
        self.resultArea.insert(END, '\n' + destination.getActivities())
        self.resultArea.insert(END, '\n' + str(destination.getTicketPrice()))

    def summerButton_Click(self) :
        risk = int(self.riskTextBox.get())
        cash = float(self.cashTextBox.get())
        if risk > 5 and cash >= 5000 :
            #Use obj names as arg.
            self.result(self.whitewater)
        elif risk > 5 and cash < 5000 :
            self.result(self.kayak)
        elif risk < 5 and cash >= 5000 :
            self.result(self.PI)
        else :
            self.result(self.UP)

    def winterButton_Click(self) :
        risk = int(self.riskTextBox.get())
        cash = float(self.cashTextBox.get())
        if risk > 5 and cash >= 5000 :
            self.result(self.everest)
        elif risk > 5 and cash < 5000 :
            self.result(self.wisconsin)
        elif risk < 5 and cash >= 5000 :
            self.result(self.alaska)
        else :
            self.result(self.iceFishing)

    def temperateButton_Click(self) :
        risk = int(self.riskTextBox.get())
        cash = float(self.cashTextBox.get())
        if risk > 5 and cash >= 5000 :
            self.result(self.dudeRanch)
        elif risk > 5 and cash < 5000 :
            self.result(self.appalachian)
        elif risk < 5 and cash >= 5000 :
            self.result(self.lakeTahoe)
        else :
            self.result(self.DC)

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
    window = Tk()
    window.title('Vacation Planner')
    window.geometry("480x400")

    run = Application(window)

    window.mainloop()

main()
            
