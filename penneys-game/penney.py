import random as rand

k = 4;

a = [0,1,1,0]
b = [1,0,0,1]
history = []

awins = 0
bwins = 0

for i in range(0, 1000000):
    while (True):
        r = rand.randint(0,1)
        history.append(r)
        if (len(history) >= 5):
            history[0] = history[1]
            history[1] = history[2]
            history[2] = history[3]
            history[3] = history[4]
            history = history[0:4]
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