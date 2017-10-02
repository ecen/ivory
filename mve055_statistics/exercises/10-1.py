import statistical as stat
import math

d1 = [3, 8, 5, 7, 2, 3, 8, 1, 5, 0, 6, 2]
d2 = [0, 2, 3, 1, 3, 1, 1, 5, 4, 0]

print("--- Supplier 1 ---")
print("Nr of datapoints: %d" %len(d1))
print("Mean: %.2f" %stat.mean(d1))

print("--- Supplier 2 ---")
print("Nr of datapoints: %d" %len(d2))
print("Mean: %.2f" %stat.mean(d2))

print("--- Supplier 1 - Supplier 2 ---")
print("Nr of datapoints: %d" %len(d2))
print("Mean: %.2f" %(stat.mean(d1)-stat.mean(d2)))