import tkinter as Tk


class View():
    '''View in the MVC pattern assumes role of rendering user
    interface to the user, and maintaining an up to date view as
    it handles user interaction it receives from Controller.
    '''

    def _add_numbers_keypad(self, frame):
        # calculator display
        self.display = Tk.Label(frame, text=0, width=12, height=1)
        self.display.grid(row=0, column=0, columnspan=10, pady=5)

        #calculator numbers pad
        self.one = Tk.Button(frame, text="1")
        self.one.grid(row=1, column=0)

        self.two = Tk.Button(frame, text="2")
        self.two.grid(row=1, column=1)

        self.three = Tk.Button(frame, text="3")
        self.three.grid(row=1, column=2)

        self.four = Tk.Button(frame, text="4")
        self.four.grid(row=2, column=0)

        self.five = Tk.Button(frame, text="5")
        self.five.grid(row=2, column=1)

        self.six = Tk.Button(frame, text="6")
        self.six.grid(row=2, column=2)

        self.seven = Tk.Button(frame, text="7")
        self.seven.grid(row=3, column=0)

        self.eight = Tk.Button(frame, text="8")
        self.eight.grid(row=3, column=1)

        self.nine = Tk.Button(frame, text="9")
        self.nine.grid(row=3, column=2)

        self.zero = Tk.Button(frame, text="0")
        self.zero.grid(row=4, column=1)

    def _add_operations_keypad(self, frame):
        #operations pad
        self.clear = Tk.Button(frame, text="C")
        self.clear.grid(row=4, column=0)

        self.equal = Tk.Button(frame, text="=")
        self.equal.grid(row=4, column=2)

        self.add = Tk.Button(frame, text="+")
        self.add.grid(row=2, column=5)

        self.sub = Tk.Button(frame, text="-")
        self.sub.grid(row=3, column=5)

        self.mul = Tk.Button(frame, text="*")
        self.mul.grid(row=2, column=6)

        self.div = Tk.Button(frame, text="/")
        self.div.grid(row=3, column=6)

    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("MVC example: Calculator")
        self.root.geometry()

        self._frame = Tk.Frame(self.root)
        self._frame.pack()
        self._add_numbers_keypad(self._frame)
        self._add_operations_keypad(self._frame)


    def refresh(self, value):
        self.display.config(text=value)

    def attach_keyboard(self, callback):
        self.root.bind("<Key>", callback)

    def start(self):
        self.root.mainloop()
