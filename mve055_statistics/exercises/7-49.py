import math

d1 = [3,2,2,2,2,3,3,3,
      3,3,3,3,4,3,2,3,
      3,2,3,3,3,3,3,1,
      3,3,3,3,3,3,3,3,
      3,3,2,3,3,3,3,3]

def mean(data):
	sum = 0
	for i in data:
		sum += i;
	return sum / len(data)

def sampleVariance(data):
	m = mean(data)
	s2 = 0
	n = len(data)
	for i in range(0, n):
		s2 += ((data[i] - m)**2)/(n-1)
	return s2
	
def stdDeviation(data):
	return math.sqrt(sampleVariance(data))

print("Mean: " + str(mean(d1)))
print("Var: " + str(sampleVariance(d1)))
print("Standard Deviation: " + str(stdDeviation(d1)))
#print(sorted(d1))