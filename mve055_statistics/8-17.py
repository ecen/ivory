import statistical as stat
import math

data = [25, 29, 32, 37, 40, 27, 30, 35, 38, 41, 42, 45, 45, 47, 49, 50, 55, 53, 60]

print("Nr of datapoints: %d" %len(data))
print("Mean: %.4f" %stat.mean(data))        
print("Variance: %.4f" %stat.variance(data))
print("Std Dev: %.4f" %stat.stdDeviation(data))

print("Mean conf interval: %s" %(stat.confBoundMean(1.729, data),))