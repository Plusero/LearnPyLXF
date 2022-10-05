import random

def FindMax(L):
    max = L[0]
    min = L[0]
    for i in range(len(L)):
        if L[i]>max:
            max = L[i]
        if L[i]<min:
            min = L[i]
    return(min,max)


L = [None]*10
for i in range(10):
    L[i] = random.randint(-5,5)
print((FindMax(L))) 

