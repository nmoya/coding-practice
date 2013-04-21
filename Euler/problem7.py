import math
'''Find the 1001th prime.
'''


#Primes:
    #1,2,3,5,7
LIMIT = 10001
primeList = [2, 3]
number = 3
while len(primeList) < LIMIT:
    number+=2
    squareroot = math.sqrt(number)
    flag = True
    for num in primeList:
        if num > squareroot: break
        if number % num == 0:
            flag = False
            break
    if flag: primeList.append(number)

print primeList[-1]
