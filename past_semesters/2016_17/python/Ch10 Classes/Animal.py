# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Animal.py
# Descr:
# In-class exercise to create the Python version of 
# Class Listings 14-10, 14-11, 14-12.

class Animal:
    def showSpecies(self):
        print('I am just a regular animal.')

    def makeSound(self):
        print('Grrrrrr')

class Dog(Animal):
    def showSpecies(self):
        print('I am a dog.')

    def makeSound(self):
        print('Woof! Woof!')

class Cat(Animal):
    def showSpecies(self):
        print('I am a cat.')

    def makeSound(self):
        print('Meow')
   
