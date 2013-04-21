import math
'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

numbersList = [x*x for x in range (1, 31)]
#numbersList = [9, 2, 3, 4, 8, 5, 6, 10]
numbersList.sort()
i = 0

j = 0
k = len(numbersList)-1
count = 0
for num in numbersList:
    i = count
    count+=1
    while True:
        if j == k:
            break
        
        if numbersList[j] + numbersList[k] < numbersList[i]:
            j+=1
        if numbersList[j] + numbersList[k] > numbersList[i]:
            k-=1

print "I: ", numbersList[i]
print "J: ", numbersList[j]
print "K: ", numbersList[k]
