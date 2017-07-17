"""
TODO:

-> fill in interpolated data for missing dates(eg. sundays, holidays etc.)

"""

import pandas as pd
import datetime

def load_file(filename):
	'''
	-> loads the files
	-> converts the csv to dataframe
	-> change the date format to match the one required by get_all_dates() function.
	'''
	
	f = open(filename, "rb")
	df = pd.read_csv(f)
	# Now change the date in usable format
	dates = []
	for i in df['Date']:
		n = i.split('/')
		n = "{}-{}-20{}".format(n[2], n[0], n[1])
		dates.append(n)
	df['Date'] = dates
	f.close()

def concave(x, y, n):
	'''
	-> for a given initial value x, final value y and n missing values; calculate the data using a concave function.
	-> The function is (y+preceeding_value)/2
	'''

	prices = []
	prices.append(x)
	print prices
	for i in range(n):
		new_price  = (y+prices[i])/2
		prices.append(new_price)
		print "{}. ----> {:.2f}".format(i+1, new_price)


def get_all_dates(start_date, end_date):
	'''
	-> returns a list of all the dates between two dates passed as strings.
	'''

	dates = []
	start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
	end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
	step = timedelta(days=1)
	while start_date <= end_date:
		dates.append(str(start_date.date()))
		start_date += step

	return dates

def main():
	print("Hello!")

if __name__ == '__main__':
	
	main()
