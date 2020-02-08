class Controller():
    '''Controller is the primary coordinator in the MVC patter, it collects
    user input, ininitiates necessary changes to model (data), and refreshes
    view to reflect any changes that might have happened.'''

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.one.bind("<Button>", lambda event, n=1: self.num_callback(n))
        self.view.two.bind("<Button>", lambda event, n=2: self.num_callback(n))
        self.view.three.bind("<Button>", lambda event, n=3: self.num_callback(n))
        self.view.four.bind("<Button>", lambda event, n=4: self.num_callback(n))
        self.view.five.bind("<Button>", lambda event, n=5: self.num_callback(n))
        self.view.six.bind("<Button>", lambda event, n=6: self.num_callback(n))
        self.view.seven.bind("<Button>", lambda event, n=7: self.num_callback(n))
        self.view.eight.bind("<Button>", lambda event, n=8: self.num_callback(n))
        self.view.nine.bind("<Button>", lambda event, n=9: self.num_callback(n))
        self.view.zero.bind("<Button>", lambda event, n=0: self.num_callback(n))
        self.view.add.bind("<Button>", lambda event, op='+': self.operation_callback(op))
        self.view.sub.bind("<Button>", lambda event, op='-': self.operation_callback(op))
        self.view.mul.bind("<Button>", lambda event, op='*': self.operation_callback(op))
        self.view.div.bind("<Button>", lambda event, op='/': self.operation_callback(op))
        self.view.equal.bind("<Button>", self.equal)
        self.view.clear.bind("<Button>", self.clear)


        self.view.attach_keyboard(self.keystroke_callback)

    def keystroke_callback(self, event):
        '''This is where you handle keystroke events from user,
        controller should invoke necessary methods on view and
        refresh view'''
        print('keystroke: {}'.format(event.keysym))

    def num_callback(self, num):
        print('number {} is clicked'.format(num))
        self.model.handle_digit(str(num))
        self.view.refresh(self.model.get_result())

    def operation_callback(self, operation):
        self.model.handle_operation(operation)
        self.view.refresh(self.model.get_expr())
        print('operation: {}'.format(operation))

    def equal(self, event):
        print('equal pressed')
        self.view.refresh(self.model.handle_EQ())

    def clear(self, event):
        print('clear pressed')
        self.model.handle_CE()
        self.view.refresh(self.model.get_result())

    def run(self):
        self.view.start()