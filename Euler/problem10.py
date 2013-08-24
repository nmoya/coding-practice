import math
'''Find the 1001th prime.
'''


#Primes:
    #2,3,5,7
LIMIT = 2000000
candidate = 3
sumPrime = 5
primeList = [2, 3]

while (candidate+2) < LIMIT:
    candidate+=2
    squareroot = math.sqrt(candidate)
    flag = True
    for num in primeList:
        if num > squareroot: break
        if candidate % num == 0:
            flag = False
            break
    if flag:
        sumPrime+= candidate
        primeList.append(candidate)

print sumPrime
