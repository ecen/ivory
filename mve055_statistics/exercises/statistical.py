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
	

def sampleVariance(data):
	m = mean(data)
	s2 = 0
	n = len(data)
	for i in range(0, n):
		s2 += ((data[i] - m)**2)/(n-1)
	return s2

def variance(data):
	m = mean(data)
	s2 = 0
	n = len(data)
	for i in range(0, n):
		s2 += ((data[i] - m)**2)/n
	return s2
	
def stdDeviation(data):
	return math.sqrt(sampleVariance(data))
	
# Get chi from Table IV for gamma = n - 1. The distribution has n - 1 degrees of freedom.
def confBoundarySigmaSq(chi, data):
	n = len(data)
	return ((n-1) * sampleVariance(data)) / chi
	
# Get t from T distribution (Table VI) for gamma = n - 1.
def confIntervalMean(t, data):
	n = len(data)
	x = mean(data)
	return (x - (t * stdDeviation(data)) / math.sqrt(n), x + (t * stdDeviation(data)) / math.sqrt(n))
	
def confBoundMean(t, data):
	n = len(data)
	x = mean(data)
	return (x - (t * stdDeviation(data)) / math.sqrt(n), x + (t * stdDeviation(data)) / math.sqrt(n))