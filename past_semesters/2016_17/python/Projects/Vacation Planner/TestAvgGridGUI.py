##William Pulkownik
##CIS 1400 2 DEC 2015
##TestAvgGridGUI.py

#import tkinter module/workspace

from tkinter import *

#GUI class
class TestAvg_GUI :
    def __init__(self) :
        #create window and set title
        self.mainWindow = Tk()
        self.mainWindow.title('Test Average')
        self.mainWindow.geometry('200x100')

        # create my test labels and text boxes
        #Tests and input boxes
        self.test1Label = Label(self.mainWindow,
                                text = 'Enter the score for test 1: ')
        self.test1TextBox = Entry(self.mainWindow, width = 10)
        self.test1Label.grid(row = 0, column = 0)
        self.test1TextBox.grid(row = 0, column = 1)
        self.test2Label = Label(self.mainWindow,
                                text = 'Enter the score for test 2: ')
        self.test2TextBox = Entry(self.mainWindow, width = 10)
        self.test2Label.grid(row = 1, column = 0)
        self.test2TextBox.grid(row = 1, column = 1)
        self.test3Label = Label(self.mainWindow,
                                text = 'Enter the score for test 3: ')
        self.test3TextBox = Entry(self.mainWindow, width = 10)
        self.test3Label.grid(row = 2, column = 0)
        self.test3TextBox.grid(row = 2, column = 1)

        # labels for avg display
        self.resultLabel = Label(self.mainWindow, text = 'Average')
        self.averageLabel = Label(self.mainWindow, text = ' ')
        self.resultLabel.grid(row = 3, column = 0)
        self.averageLabel.grid(row = 3, column = 1)

        #create buttons calcAvg and exit
        self.calcButton = Button(self.mainWindow,
                                 text = 'Calculate Average',
                                 command = self.calcButton_Click)
        self.exitButton = Button(self.mainWindow, text = 'Exit', 
                                command = self.mainWindow.destroy)
        self.calcButton.grid(row = 4, column = 0)
        self.exitButton.grid(row = 4, column = 1)
        
        
        #enter the main loop
        self.mainWindow.mainloop()

    #function to execute when calcButton selected
    def calcButton_Click(self) :
        test1 = float(self.test1TextBox.get())
        test2 = float(self.test2TextBox.get())
        test3 = float(self.test3TextBox.get())
        average = (test1 + test2 + test3) / 3
        #display the avg
        self.averageLabel.configure(text = format(average, '.2f'))
#main function to create object
def main():
    myTestAvg = TestAvg_GUI()

main()
