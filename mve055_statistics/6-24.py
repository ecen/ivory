import math
import statistical as stat

d1 = [9.1,10.1,9.0,11.4,10.5,9.5,12.0,9.1,12.2,13.1,10.0,9.3,9.0,9.6,11.1,9.1,13.3,10.7,9.1,9.0,9.0,11.0,9.2,11.6]

def printStat(data):
	print("Mean: " + str(stat.mean(data)))
	print("Var: " + str(stat.variance(data)))
	print("Standard Deviation: " + str(stat.stdDeviation(data)))
	print("Median: " + str(stat.median(data)))
	
printStat(d1)