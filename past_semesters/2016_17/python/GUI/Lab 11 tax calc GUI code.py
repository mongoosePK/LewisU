##William Pulkownik
##CIS 1400 3 DEC 2015
##Lab 11.py

#import tkinter module/workspace

from tkinter import *

#GUI class
class TaxCalc_GUI :
    def __init__(self) :
        self.mainWindow = Tk()
        self.mainWindow.title('Tax Calculator')
        self.mainWindow.geometry('350x200')

        #user entry
        self.valueLabel = Label(self.mainWindow,
                                text = 'Enter your property\'s full value: ')
        self.valueTextBox = Entry(self.mainWindow, width = 10)
        self.valueLabel.grid(row = 0, column = 0)
        self.valueTextBox.grid(row = 0, column = 1)

        #calc button
        self.calcButton = Button(self.mainWindow,
                                 text = 'Calculate Taxes',
                                 command = self.calcButton_Click)
        self.calcButton.grid(row = 1, column = 1)

        #result displays
        self.assessLabel = Label(self.mainWindow, text = 'Assessment Value: $')
        self.assessResult = Label(self.mainWindow, text = ' ')
        self.taxLabel = Label(self.mainWindow, text = 'Tax owed: $')
        self.taxResult = Label(self.mainWindow, text = ' ')
        self.assessLabel.grid(row = 3, column = 0)
        self.assessResult.grid(row = 3, column = 1)
        self.taxLabel.grid(row = 4, column = 0)
        self.taxResult.grid(row = 4, column = 1)

        #exit button
        self.exitButton = Button(self.mainWindow, text = 'Exit',
                                 command = self.mainWindow.destroy)
        self.exitButton.grid(row = 5, column = 1)

        #main loop
        self.mainWindow.mainloop()

    #calcButton Function
    def calcButton_Click(self) :
        #processing
        value = float(self.valueTextBox.get())
        assessment = value * .6
        tax = value * .00384
        #display functionality
        self.assessResult.configure(text = format(assessment, '.2f'))
        self.taxResult.configure(text = format(tax, '.2f'))

#main function
def main() :
    taxLab = TaxCalc_GUI()

#call it.
main()
