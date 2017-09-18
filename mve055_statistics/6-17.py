import math
import statistical as stat

d1 = [1, 3, 2, 2, 5, 4, 4, 3, 3]
d2 = [1, 2, 4, 1, 2, 5, 2, 5, 1, 5, 5, 3]

print("Mean: " + str(stat.mean(d2)))
print("Var: " + str(stat.variance(d2)))
print("Standard Deviation: " + str(stat.stdDeviation(d2)))
print(sorted(d2))