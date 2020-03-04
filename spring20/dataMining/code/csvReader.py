#csvReader.py

import csv

with open('data/PA2_weighted.csv') as csv_file :
	csv_reader = csv.reader(csv_file,delimiter=',')