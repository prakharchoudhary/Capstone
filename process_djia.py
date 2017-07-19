"""
TODO:

-> fill in interpolated data for missing dates(eg. sundays, holidays etc.)

"""
import sys
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
		n = "20{}-{}-{}".format(n[2], n[0], n[1])
		dates.append(n)
	df['Date'] = dates
	return df
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
	return prices


def get_all_dates(start_date, end_date):
	'''
	-> returns a list of all the dates between two dates passed as strings.
	'''

	dates = []
	start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
	end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
	print("start date: {} ------------ end date: {}".format(start_date, end_date))
	step = datetime.timedelta(days=1)
	while start_date <= end_date:
		dates.append(str(start_date.date()))
		start_date += step
	
	return dates

def missing_data(start, end, missing_dates, df):
	'''
	-> pass the two dates between which we wish the data is missing.
	-> now use the concave function to obtain a list of missing values for each column.
	-> then group them date-wise to form new fields.
	-> empty the missing_dates array
	'''
	data = []
	n = len(missing_dates)
	open_val = concave(df['Open'][start], df['Open'][end], n)
	close_val = concave(df['Close'][start], df['Close'][end], n)
	high_val = concave(df['High'][start], df['High'][end], n)
	low_val = concave(df['Low'][start], df['Low'][end], n)

	for i in range(n):
		data.append([missing_dates[i], open_val[i], high_val[i], low_val[i], close_val[i]])

	return data

def main():

	if len(sys.argv)>1:
		print(sys.argv[1])
		df = load_file(sys.argv[1])
	else:
		filename = raw_input("Enter the file path: ")
		df = load_file(filename)
	all_dates = get_all_dates(df['Date'][len(df['Date'])-1], df['Date'][0])
	# print(all_dates)	#print all dates
	final_data = []
	missing_dates = []

	'''
	-> if date from complete list is present in raw_file, add the field directly to final_data.
	-> else make flag and keep adding the dates to missing dates to missing dates list.
	-> finally once another similar date appears, make flag = 1 and run the concave function to obtain data for each column for all missing dates.
	-> At last append the new data and write complete data to a new csv.
	'''
	given_dates = [i for i in df['Date']]
	# print(given_dates)	#print given dates
	for i in range(len(all_dates)):
		if all_dates[i] in given_dates:
			flag = 1
			final_data.append(df.iloc[i])
		else:
			flag = 0
			missing_dates.append(all_dates[i])
		
		if flag == 1 and len(missing_dates):
			total = len(final_data)
			# print(final_data)
			missing_info = missing_data(final_data[total-2]['Date'], final_data[total-1]['Date'], missing_dates, df)
			final_data.append(missing_info)
			missing_dates = []

	# print(final_data[:5])
	final_df = pd.DataFrame(final_data)
	final_df.to_csv('./completeData.csv')

if __name__ == '__main__':
	
	main()
