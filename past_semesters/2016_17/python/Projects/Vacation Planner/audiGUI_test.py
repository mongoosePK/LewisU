from tkinter import *

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

            

#GUI class
class Destination_GUI :
    def __init__(self) :
        self.mainWindow = Tk()
        self.mainWindow.title('Vacation Recommendations!')
        self.mainWindow.geometry('750x500')

        


        self.springImage = PhotoImage(file = 'springG.gif')
        self.summerImage = PhotoImage(file = 'summerG.gif')
        self.fallImage = PhotoImage(file = 'fallG.gif')
        self.winterImage = PhotoImage(file = 'winterG.gif')

        

        #user entry
        self.cashLabel = Label(self.mainWindow,
                                text = 'How much can you spend?')
        self.cashTextBox = Entry(self.mainWindow, width = 10)
        self.cashLabel.grid(row = 0, column = 0)
        self.cashTextBox.grid(row = 0, column = 1)
        self.riskLabel = Label(self.mainWindow,
                                text = 'how much risk')
        self.riskTextBox = Entry(self.mainWindow, width = 10)
        self.riskLabel.grid(row = 1, column = 0)
        self.riskTextBox.grid(row = 1, column = 1)
        #Spring
        self.springButton = Button(self.mainWindow,
                                 image = self.springImage, width = 75, height = 50,
                                 command = self.springButton_Click)
        self.springButton.grid(row = 2, column = 1)

        #Summer
        self.summerButton = Button(self.mainWindow,
                                 image = self.summerImage,
                                 command = self.summerButton_Click)
        self.summerButton.grid(row = 2, column = 2)

        #Fall
        self.fallButton = Button(self.mainWindow,
                                 image = self.fallImage,
                                 command = self.fallButton_Click)
        self.fallButton.grid(row = 2, column = 3)

        #Winter
        self.winterButton = Button(self.mainWindow,
                                 image = self.winterImage,
                                 command = self.winterButton_Click)
        self.springButton.grid(row = 2, column = 4)

        #Display result
        self.result = Label(self.mainWindow, text = ' ')
        self.result.grid(row = 4, column = 2)

        #main loop
        self.mainWindow.mainloop()

    def whitewater(self) :
        self.whitewater = Destination('Colorado', 'Whitewater Rafting', 5500.00)
    def kayak(self) :
        self.kayak = Destination('Naperville', 'Kayaking a river', 400.00)
    def PI(self) :
        self.PI = Destination('Phillipines', 'Relax in the Archipelago Nation!', 7500.00)
    def UP(self) :
        self.UP = Destination('Upper Peninsula, Michigan', 'Explore the Great Outdoors!',
                     1700.00)
        self.getLocation(self)


    def springButton_Click(self) :
        risk = int(self.riskTextBox.get())
        cash = float(self.cashTextBox.get())
        if risk > 5 and cash >= 5000 :
            self.result.configure(text = whitewater.getLocation())
        elif risk > 5 and cash < 5000 :
            self.result.configure(text = kayak.getLocation())
        elif risk < 5 and cash >= 5000 :
            self.result.configure(text = PI.getLocation())
                                  
        else :
            self.result.configure(text = )
                                  
def main() :
    test = Destination_GUI()
    
main()
