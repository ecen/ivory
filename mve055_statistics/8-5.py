import statistical as stat
import math

data = [0.001, 0.002, 0.003, 0.002, 0.002, 0.007, 0.003, 0.004, 0.003, 0.006, 0.006, 0.003, 0.005, 0.004, 0.004, 0.001, 0.008, 0.001, 0.004, 0.003, 0.001, 0.003, 0.003, 0.005, 0.006]

print("Nr of datapoints: %d" %len(data))
print("Mean: %.4f" %stat.mean(data))        
print("Variance: %.8f" %stat.variance(data))
print("Std Dev: %.4f" %stat.stdDeviation(data))

chi1 = 15.7
#chi2 = 11.2

print("L1: %.6f" %stat.confBoundarySigmaSq(chi1, data))
#print("L2: %.4f" %stat.confBoundarySigmaSq(chi2, data))

print("sqrt(L1): %.6f" %math.sqrt(stat.confBoundarySigmaSq(chi1, data)))
#print("sqrt(L2): %.4f" %math.sqrt(stat.confBoundarySigmaSq(chi2, data)))