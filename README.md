# MLND - Stock Prediction Using Twitter Sentiment Analysis


## Problem Statement

This project will use supervised learning to predict the next day's stock price status(i.e, whether it will higher or lower than current day's closing price).

This project is a python and scikit learn based implementation of the paper: (http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.375.4517&rep=rep1&type=pdf)

## Dataset

The dataset includes:
	1. The DJIA stock data from June 2009 to December 2009. It has Open, Close, High and Low values for each day.
	2. A collection of 350k tweets between the above mentioned daterange, tagged via a self-written sentiment analysis classifier.

## Scripts

Several Python scripts are available to train the model:

* ```missing_record.py```: fills in interpolated data for missing dates(eg. sundays, holidays etc.) in the DJIA dataset
* ```SentimentAnalysis.ipynb```: Sentiment analysis project to train on kaggleDataset and prepare classifier which can successfully tag the collected tweets. 

### Report

A final report explaining this project and the surrounding problem domain is available as ```report.pdf```.



