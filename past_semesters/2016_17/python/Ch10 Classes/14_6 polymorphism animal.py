##William Pulkownik
##23 NOV 2015
## 14_6 polymorphism among inherited classes and overridden methods

import Animal

#function to display animal behavior
def showAnimalInfo(creature) :
    creature.showSpecies()
    creature.makeSound()

#create objects
def main() :
    #create objects
    myAnimal = Animal.Animal()
    myDog = Animal.Dog()
    myCat = Animal.Cat()
    #show information
    print('Here is info about an animal...')
    showAnimalInfo(myAnimal)
    print('learn about my Dog')
    showAnimalInfo(myDog)
    print('My cat\'s dossier')
    showAnimalInfo(myCat)
    
main()

##    OUTPUT
##>>> 
##Here is info about an animal...
##I am just a regular animal.
##Grrrrrr
##learn about my Cat
##I am a dog.
##Woof! Woof!
##My cat's dossier
##I am a cat.
##Meow
##>>> 
