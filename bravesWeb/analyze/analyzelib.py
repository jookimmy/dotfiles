import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#using pandas to read excel file given
data = pd.read_excel("batData/BattedBallData.xlsx")

#making different functions to call
def histogram(variable1):
	#converting recieved values into a python list
	list1 = data[variable1].values.tolist()
	#matplotlib library to convert data into histogram
	plt.hist(list1)
	plt.title("Frequency of " + variable1)
	plt.ylabel("Frequency")
	plt.xlabel(variable1)
	#saving the figure onto a static file storage
	plt.savefig('bravesWeb/static/graphs/plot.png')
	#clear current figure so that calling another function won't be affected
	plt.clf()

def scatter(variable1, variable2):
	#converting recieved values into a python list
	list1 = data[variable1].values.tolist()
	list2 = data[variable2].values.tolist()
	#plotting x and y variables into scatter plot
	plt.scatter(list1,list2, s= 10, c = (0,0,0), alpha = 0.5)
	plt.ylabel(variable2)
	plt.xlabel(variable1)
	plt.title(variable1 + " vs " + variable2)
	#gridding the graph so that each data point is easier to understand
	plt.grid(True)
	#saving figure onto a statif file storage
	plt.savefig('bravesWeb/static/graphs/plot.png')
	#clear current figure
	plt.clf()

def bar_chart(variable1, variable2):
	#creating variables to utilize for bar chart
	sacrifice_count = 0
	sacrifice_sum = 0.0
	single_count = 0
	single_sum = 0.0
	double_count = 0
	double_sum = 0.0
	triple_count = 0
	triple_sum = 0.0
	homeRun_count = 0
	homeRun_sum = 0.0
	out_count = 0
	out_sum = 0.0
	if variable1 != 'PLAY_OUTCOME':
		return None
	else:
		list1 = data[variable1].values.tolist()
		list2 = data[variable2].values.tolist()
		for i in range(len(list1)):
			if list1[i] == 'Single':
				single_sum += list2[i]
				single_count += 1
			if list1[i] == 'Double':
				double_sum += list2[i]
				double_count += 1
			if list1[i] == 'Triple':
				triple_sum += list2[i]
				triple_count += 1
			if list1[i] == 'Out':
				out_sum += list2[i]
				out_count += 1
			if list1[i] == 'HomeRun':
				homeRun_sum += list2[i]
				homeRun_count += 1
			if list1[i] == 'Sacrifice':
				sacrifice_sum += list2[i]
				sacrifice_count += 1
	x_axis = ['Single', 'Double', 'Triple', 'Home Run', 'Sacrifice', 'Out']
	single_bar = single_sum/single_count
	double_bar = double_sum/double_count
	triple_bar = triple_sum/triple_count
	homeRun_bar = homeRun_sum/homeRun_count
	out_bar = out_sum/out_count
	sacrifice_bar = sacrifice_sum/sacrifice_count
	y_pos = np.arange(len(x_axis))
	averages = [single_bar, double_bar, triple_bar, homeRun_bar, sacrifice_bar, out_bar]
	plt.bar(y_pos, averages, align = 'center', alpha = 0.5)
	plt.xticks(y_pos, x_axis)
	plt.ylabel(variable2)
	plt.title("Average " + variable2 + " per Play Outcome")
	plt.savefig('bravesWeb/static/graphs/plot.png')
	plt.clf()
