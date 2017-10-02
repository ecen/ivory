import statistical as stat
import math

data = [1.38, 1.26, 1.52, 1.56, 1.48, 1.46, 1.30, 1.28, 1.43, 1.43, 1.55, 1.57, 1.51, 1.53, 1.68, 1.37, 1.47, 1.61, 1.49, 1.43, 1.64, 1.51, 1.60, 1.65, 1.60, 1.64, 1.51, 1.51, 1.53, 1.74]
        
print(stat.sampleVariance(data))
print(stat.stdDeviation(data))

print("d) ---")
print(math.sqrt(0.00833))
print(math.sqrt(0.0233))