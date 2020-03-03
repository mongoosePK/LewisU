#csvReader.py

import csv

with open('Admission_Predict.csv') as csv_file :
	csv_reader = csv.reader(csv_file,delimiter=',')