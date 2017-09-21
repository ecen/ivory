import random as rand

k = 7;

a = [1,1,1,1,1,1,1]
b = [0,1,1,1,0,0,0]
history = []

awins = 0
bwins = 0

for i in range(0, 1000):
    while (True):
        r = rand.randint(0,1)
        history.append(r)
        if (len(history) >= k+1):
            for j in range(1, k+1):
                history[j-1] = history[j]
            history = history[0:k]
        #print(history)
        if (history == a):
            #print("A wins!")
            awins += 1
            break
        if (history == b):
            #print("B wins!")
            bwins += 1
            break
    
print("A: %d" %awins)
print("B: %d" %bwins)