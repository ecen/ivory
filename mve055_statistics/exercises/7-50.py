import statistical as stat

data = [1,1.5,2,2.5,
        1.5,2,2.5,3,
        2,2.5,3,3.5,
        2.5,3,3.5,4]

print("Mean: %.3f" %stat.mean(data))        
print("Variance: %.3f" %stat.variance(data))