import math

def mean(data):
	sum = 0
	for i in data:
		sum += i;
	return sum / len(data)
	
def median(data):
	halfi = 0
	setMean = False
	if (len(data) % 2 != 0):
		halfi = int(len(data) / 2)
		return sorted(data)[halfi]
	else:
		halfi = int((len(data) - 1) / 2)
		return (sorted(data)[halfi] + sorted(data)[halfi+1]) / 2
	

def variance(data):
	m = mean(data)
	s2 = 0
	n = len(data)
	for i in range(0, n):
		s2 += ((data[i] - m)**2)/(n-1)
	return s2
	
def stdDeviation(data):
	return math.sqrt(variance(data))