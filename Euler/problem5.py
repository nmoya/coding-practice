

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
LIMIT = 20


number = 1
'''while True:
    found = 0
    for i in range(LIMIT):
        i = i+1
        if number % i == 0:
            found+=1
        else:
            break
    if found == LIMIT:
        break
    number+=20

print number
    '''

i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            if (i*j) % k == 0:
                i *= j
                break
print i
