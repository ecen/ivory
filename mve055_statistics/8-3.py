import statistical as stat
import math

data = [21.9, 23.4, 22.1, 22.1, 24.7, 24.6,
        24.0, 24.1, 24.2, 26.5, 23.8, 25.3,
        24.8, 24.8, 24.5, 27.8, 24.9,
        27.2, 25.1, 25.5, 23.7, 26.5,
        22.0, 26.7, 25.2, 23.1, 25.4]

print("Nr of datapoints: %d" %len(data))
print("Mean: %.4f" %stat.mean(data))        
print("Variance: %.4f" %stat.variance(data))
print("Std Dev: %.4f" %stat.stdDeviation(data))

chi1 = 48.3
chi2 = 11.2

print("L1: %.4f" %stat.confBoundarySigmaSq(chi1, data))
print("L2: %.4f" %stat.confBoundarySigmaSq(chi2, data))

print("sqrt(L1): %.4f" %math.sqrt(stat.confBoundarySigmaSq(chi1, data)))
print("sqrt(L2): %.4f" %math.sqrt(stat.confBoundarySigmaSq(chi2, data)))