import statistical as stat
import math

data = [-0.1, -0.02, 0.1, -0.03, 0.09, 0.01, -0.05, 0.05, -0.06, 0.01, 0.03, 0.06, 0.02, -0.07, 0.03]

print("Nr of datapoints: %d" %len(data))
print("Mean: %.4f" %stat.mean(data))        
print("sampleVariance: %.4f" %stat.sampleVariance(data))
print("Std Dev: %.4f" %stat.stdDeviation(data))

chi1 = 48.3
chi2 = 11.2

print("Mean conf interval: %s" %(stat.confIntervalMean(1.761, data),))