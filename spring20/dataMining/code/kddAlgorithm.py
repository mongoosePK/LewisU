import csv

# NEAREST NEIGHBOR ALGORITHM   KNN ALGORITHM
# IF N = 1 THEN FIND THE CLOSEST TRAINING DATA OBJECT FOR EACH TEST DATA OBJECT
# IF N > 1 THEN PICK THE LABEL BASED ON THE CONSENSUS OF THE N NEAREST TRAINING DATA OBJECTS,
# WHERE THE NEAREST DATA OBJECT WILL OVERULE IF THERE IS NO CONSENSUS

import pandas as pd


# Read in the
greScores = []


class DataNode :


	def __init__(self) :
		self.nodeList = None
		self.ul = None
		self.ur = None
		self.ll = None
		self.lr = None
		self.depth = 0
		self.index = -1
		predictedResearch = False
		currentIndex = 0
		return

	def setGRE(self,dataItem) :
		# We assuming the data object is a string , and converting it into an integer
		self.greItem = int(dataItem)

	def setTOEFL(self,dataItem) :
		# We assuming the data object is a string , and converting it into an integer
		self.TOEFL = int(dataItem)

	def setPrediction(self,dataItem) :
		if(dataItem is not None):
			self.prediction = int(dataItem)
		else:
			self.prediction = -1

	def setUnivRating(self,dataItem) :
		self.rating = int(dataItem)

	def setResearch(self,dataItem) :
		# This attribute is what we are prediciting from the test data instances.
		self.research = int(dataItem)



	# Add another member function in order to retrieve the TOEFL score.

headNode = DataNode()

trainingList = []
testList = []




#Load the data into a dataframe.
dataFrame = pd.io.parsers.read_csv('Admission_Predict.csv')

dataFrame.columns = ['Serial No','GRE Score','TOEFL Score','University Rating','SOP','LOR' ,'CGPA','Research','Chance of Admit']
		


greList = dataFrame['GRE Score']
toeflList = dataFrame['TOEFL Score']
researchList = dataFrame['Research']

xMin = greList.min()
xMax = greList.max()
yMin = toeflList.min()
yMax = toeflList.max()

#trainingData isa node and already has its 
# coordinate attributes, unassigned prediction label. This is a recursive function
def findNeighbor(trainingData, currentNode)
	#if currentNode does not have training Data then exit and perform DFS or BFS
	#search to find nearest training data through the euclidian distance formula

	#Find the sector to search for the training data -- 
	#currNode.leftUpperQuadrant, currNode.rightUpperQuadrant
	# currNode.leftLowerQuadrant, currNode.rightLowerQuadrant

def insertNode(xMin,xMax, yMin, yMax, xValue, yValue, depth,  currentNode) :

	if depth == 3 :
		currentNode.trainingList.append([xValue,yValue])
		return

		
	
	# Find the quadrant
	xMid = (xMin + xMax) / 2
	yMid = (yMin + yMax) / 2

	newNode = DataNode()

	if xValue >= xMid and yValue >= yMid :
		# upper right
		currentNode.ur = newNode
		currentNode.trainingList.append([xValue,yValue])
		xMin = xMid
		yMin = yMid
		insertNode(xMin,xMax,yMin,yMax,depth + 1, currentNode.ur)
		return

	if xValue >= xMid and yValue < yMid :
		# lower right
		currentNode.lr = newNode
		currentNode.lr.trainingList.append([xValue,yValue])
		xMin = xMid
		yMin = yMid
		insertNode(xMin,xMax,yMin,yMax,depth + 1, currentNode.lr)
		return


		 


for index in range(len(greList)) :
	xValue = greList[index]
	yValue = greList[index]
	insertNode(xValue,yValue,headNode)
	



print("Column: greScore ---- Min: %10.5f, Max: %10.5f, STD: %10.5f" % (greList.min(), greList.max(), greList.std()))


 


