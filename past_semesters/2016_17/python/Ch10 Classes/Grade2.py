# Author:  <Your Name Here>
# Date:    MM/DD/YYYY
# Program: Grade2.py
# Descr:
# In-class exercise to create the Python version of 
# Class Listing 14-8 in your textbook.

class GradedActivity:
    def setScore(self, s):
        self.__score = s

    def getScore(self):
        return self.__score

    def getGrade(self):
        if self.__score >= 90:
            grade = 'A'
        elif self.__score >= 80:
            grade = 'B'
        elif self.__score >= 70:
            grade = 'C'
        elif self.__score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        return grade
 
# Class Listing 14-9 in your textbook.
# Python NOTE: By writing GradedActivity inside parentheses after the class name,
# the FinalExam class extends the GradedActivity class (GradedActivity is the
# superclass and FinalExam is the subclass)
class FinalExam(GradedActivity):
	# constructor (Python initializer)
    def __init__(self, questions, missed):
        # set private attributes
        self.__numQuestions = questions
        self.__numMissed = missed
        # calculate pointsEach assuming maximum 100 points
        self.__pointsEach = 100.0/questions
        # determine score
        numericScore = 100.0 - (missed * self.__pointsEach)
        # set score by calling inherited method
        self.setScore(numericScore)

    # accessor methods
    def getPointsEach(self):
        return self.__pointsEach

    def getNumMissed(self):
        return self.__numMissed

   
