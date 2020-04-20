import csv

# NEAREST NEIGHBOR ALGORITHM   KNN ALGORITHM
# IF N = 1 THEN FIND THE CLOSEST TRAINING DATA OBJECT FOR EACH TEST DATA OBJECT
# IF N > 1 THEN PICK THE LABEL BASED ON THE CONSENSUS OF THE N NEAREST TRAINING DATA OBJECTS,
# WHERE THE NEAREST DATA OBJECT WILL OVERULE IF THERE IS NO CONSENSUS


# Read in the
greScores = []

class DataObject :


	def __init__(self) :
		self.index = -1
		predictedResearch = False
		currentIndex = 0
		return

	def getGRE(self,dataItem) :
		# We assuming the data object is a string , and converting it into an integer
		self.greItem = int(dataItem)

	def getTOEFL(self,dataItem) :
		# We assuming the data object is a string , and converting it into an integer
		self.TOEFL = int(dataItem)

	def getPrediction(self,dataItem) :
		if(dataItem is not None):
			self.prediction = int(dataItem)
		else:
			self.prediction = -1

	def getUnivRating(self,dataItem) :
		self.rating = int(dataItem)

	def getResearch(self,dataItem) :
		# This attribute is what we are prediciting from the test data instances.
		self.research = int(dataItem)



	# Add another member function in order to retrieve the TOEFL score.


trainingList = []
testList = []

with open('Admission_Predict.csv') as csv_file :
	csv_reader = csv.reader(csv_file,delimiter=',')
	for index,row in enumerate(csv_reader) :
		if (index % 5 == 0) :
			if index == 0 :
				# not reading in the first line
				continue
			# This is my test list
			myDataObject = DataObject()
			myDataObject.getGRE(row[1])
			myDataObject.getTOEFL(row[2])
			# We assuming that we do not know the university rating
			# But we need read this in order to evaluate the predication
			myDataObject.getUnivRating(row[3])
			myDataObject.getResearch(row[7])
			myDataObject.getPrediction(None)
			testList.append(myDataObject)
		else :
			# This is my training list
			myDataObject = DataObject()
			myDataObject.getGRE(row[1])
			myDataObject.getTOEFL(row[2])
			myDataObject.getUnivRating(row[3])
			myDataObject.getResearch(row[7])
			trainingList.append(myDataObject)



#for element in testList :
#	print(element.greItem, element.TOEFL)

for element in trainingList :
	print(element.greItem, element.TOEFL)


for testInstance in testList :
	minValue = float("inf")
	marker = -1
	for index, trainingInstance in enumerate(trainingList) :
		#  Calculate the distance based on the two features TOEFL, ACT
		dist = pow(testInstance.greItem - trainingInstance.greItem, 2) + pow(testInstance.TOEFL - trainingInstance.TOEFL,2)
		if dist < minValue :
			minValue = dist
			marker = index
	testInstance.prediction = trainingList[marker].research
 


correctCount = 0
for index, testInstance in enumerate(testList) :
	if (testInstance.prediction == testInstance.research) :
		correctCount += 1

print(f"number of correct instances: {correctCount} out of {len(testList)}")