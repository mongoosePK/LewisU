from view import View
from controller import Controller
from calculator_model import CalculatorModel
#from subject import Observer, Subject, ConcreteSubject
if __name__ == '__main__':
    ''' Main function, instantiate instances of Model, View and a Controller'''

    model = CalculatorModel()
    view = View(model = model)

    controller = Controller(model=model, view=view)
    controller.run()