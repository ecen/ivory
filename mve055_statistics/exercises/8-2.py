import statistical as stat
import math

data = [10.9, 1.7, 9.5, 2.9, 9.1, 3.2,
        9.1, 7.4, 13.3, 13.1, 6.6, 13.7,
        1.5, 6.3, 7.4, 9.9, 13.6, 17.3,
        3.6, 4.9, 13.1, 7.8, 10.3, 10.3,
        9.6, 5.7, 2.6, 15.1, 2.9, 16.2]

print("Mean: %.4f" %stat.mean(data))        
print("sampleVariance: %.4f" %stat.sampleVariance(data))
print("Std Dev: %.4f" %stat.stdDeviation(data))

print("L1: %.4f" %stat.confBoundarySigmaSq(43.8, data))
print("L2: %.4f" %stat.confBoundarySigmaSq(18.5, data))

print("sqrt(L1): %.4f" %math.sqrt(stat.confBoundarySigmaSq(43.8, data)))
print("sqrt(L2): %.4f" %math.sqrt(stat.confBoundarySigmaSq(18.5, data)))