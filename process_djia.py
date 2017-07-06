"""
TODO:

1. fill in interpolated data for missing dates(eg. sundays, holidays etc.)
"""
import csv

with open('DJIA.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print row
