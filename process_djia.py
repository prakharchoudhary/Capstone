"""
TODO:

-> fill in interpolated data for missing dates(eg. sundays, holidays etc.)

"""

import pandas as pd
import datetime

def load_file(filename):
	
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

	prices = []
	prices.append(x)
	print prices
	for i in range(n):
		new_price  = (y+prices[i])/2
		prices.append(new_price)
		print "{}. ----> {:.2f}".format(i+1, new_price)


def get_all_dates(start_date, end_date):
	
	dates = []
	start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
	end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
	step = timedelta(days=1)
	while start_date <= end_date:
		dates.append(str(start_date.date()))
		start_date += step

	return dates

def dates_iter(df):

	l = len(df.Date)
	all_dates = get_all_dates(df.Date[0], df.Date[l-1])


if __name__ == '__main__':
	
	main()
