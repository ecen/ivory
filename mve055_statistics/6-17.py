import math

d1 = [1, 3, 2, 2, 5, 4, 4, 3, 3]
d2 = [1, 2, 4, 1, 2, 5, 2, 5, 1, 5, 5, 3]

def mean(data):
	sum = 0
	for i in data:
		sum += i;
	return sum / len(data)

def variance(data):
	m = mean(data)
	s2 = 0
	n = len(data)
	for i in range(0, n):
		s2 += ((data[i] - m)**2)/(n-1)
	return s2
	
def stdDeviation(data):
	return math.sqrt(variance(data))

print("Mean: " + str(mean(d2)))
print("Var: " + str(variance(d2)))
print("Standard Deviation: " + str(stdDeviation(d2)))
print(sorted(d2))