import sys

def p_arr(arr):
	# print without spaces such that it matches the storing format in csv
	for i in range(len(arr)):
		print("{},{},{},{}".format(arr[i][0],arr[i][1],arr[i][2],arr[i][3]))

def concave(arr_x, arr_y, n):
	temp_arr = [[] for i in range(n)]
	# the previous approach:
	'''
		empty_list = []
		for i in range(n):
			temp_arr.append(empty_list)
	'''
	# assigns the same pointer to every list that is appened in temp_arr
	# hence any change in one will lead to same change in the rest.

	for i in range(len(arr_x)):
		for j in range(n):
			arr_x[i] = round((arr_x[i]+arr_y[i])/2,2)
			temp_arr[j].append(arr_x[i])
	
	p_arr(temp_arr)
	print "\n"

if __name__ == '__main__':
	x_arr = sys.argv[1].split(',')
	y_arr = sys.argv[2].split(',')


	x_arr = [float(i) for i in x_arr]
	y_arr = [float(i) for i in y_arr]	

	print(x_arr);print(y_arr)
	print("-"*100)
	concave(x_arr, y_arr, int(sys.argv[3]))