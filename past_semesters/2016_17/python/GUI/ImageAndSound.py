# Author:  Carolyn England
# Date:    
# Program: ImageAndSound.py
# Descr:
# Sample Python code to demonstrate use of GUI labels and buttons
# with images and playing a .wav file in Windows.

import tkinter   # needed for access to gui libraries
import winsound  # needed to play .wav files under windows

class TestImageAndSound:
    def __init__(self):
        
        # create window
        self.mainWindow = tkinter.Tk()
        # set window title
        self.mainWindow.title('Image And Sound')
        # set opening window width and height
        self.mainWindow.geometry('250x120')
        # set minimum and maximum window sizes
        # if same as opening size, prevents resizing
        self.mainWindow.minsize(250, 120)
        self.mainWindow.maxsize(250, 120)

        # create image of Python logo
        # NOTE: Tkinter only reads gif and ppm images
        # use the Python Image Library (PIL) for other image formats
        self.pythonImage = tkinter.PhotoImage(file = 'python.gif')

        # create image of Java Duke logo
        self.dukeImage = tkinter.PhotoImage(file = 'duke.gif')

        # create image of exit logo
        self.exitImage = tkinter.PhotoImage(file = 'exit.gif')
        
        # create frame to group GUI widgets
        self.widgetFrame = tkinter.Frame(self.mainWindow)

        # create button with Python image
        # include callback event handler for button click
        self.pythonButton = tkinter.Button(self.widgetFrame, \
                                image = self.pythonImage, \
                                width = '50', height = '50',\
                                command = self.pythonButtonClick)

        # create label with Java Duke image
        self.dukeLabel = tkinter.Label(self.widgetFrame, \
                                image = self.dukeImage, \
                                width = '65', height = '115')

        # create exit button with text
        # include built-in command for button click
        # callback event handler
        self.exitButton = tkinter.Button(self.widgetFrame, \
                                text = 'Exit', \
                                # combine image and text
                                image = self.exitImage, \
                                # use compound for image placement
                                compound = 'left', \
                                # callback function to end program
                                command = self.exitButtonClick)
        
        
        # pack widgets into frame
        self.pythonButton.pack(side = 'left')
        self.dukeLabel.pack(side = 'left')
        self.exitButton.pack(side = 'left')
        
        # pack frame into window
        self.widgetFrame.pack()
        
        # enter the main gui loop
        tkinter.mainloop()

    # The pythonButtonClick is an event handler for
    # the pythonButton to play a sound (on Windows).
    def pythonButtonClick(self):
        winsound.PlaySound('applause.wav', winsound.SND_FILENAME)       

    # The exitButtonClick is an event handler for
    # the exitButton to play a sound (on Windows).
    def exitButtonClick(self):
        winsound.PlaySound('whoosh.wav', winsound.SND_FILENAME)
        self.mainWindow.destroy()

        
# create GUI window and widget object
def main():
    tias = TestImageAndSound()

# call main
main()
