import sys
import csv
import pandas as pd

def load_file(filename):
	'''
	loads the file with all the tagged tweets.
	'''

	f = open(filename, 'rb')
	df = pd.read_csv(f)
	# print(df.head(3))
	# print(df.tail(3))
	return df

def score_catcher(df):
	'''
	finds out the net positively and negatively tagged tweets for each day.
	'''
	data = []
	dates = []
	record = {}
	for index, row in df.iterrows():
		sys.stdout.write("Working for Date: {}\r".format(str(row['Date'])))
		sys.stdout.flush()
		if not len(dates):
			dates.append(str(row['Date']))
			pos = 0
			neg = 0
		elif len(dates) and row['Date'] not in dates:
			dates.append(str(row))
			# TODO: call func to calculate net sentiment for the day
			# record = {"Date": dates[len(dates)-1], "sentiment": sentiment}
			record = {"Date": dates[len(dates)-1], "pos": pos, "neg": neg}	
			data.append(record) 
			pos = 0
			neg = 0
		
		if row['Date'] in dates:
			if int(row['sentiment']) == 1:
				pos += 1
			elif int(row['sentiment']) == 0:
				neg += 1
	return data


def make_file(data):
	'''
	make a csv file for the processed data.
	'''
	final_df = pd.DataFrame(data)
	pd.to_csv("./daily_twitter_sentiment.csv", columns=('Date', 'Positive', 'Negative'))
	return

def main():
	'''
	the binder of all functions in a meaningful sequence.
	'''
	df = load_file('./TaggedData.csv')
	data = score_catcher(df)
	make_file(data)
	return

if __name__ == '__main__':

	main()


