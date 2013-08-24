

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
LIMIT = 4000000

sumTotal = 1
previous = 1
current = 1
while True:
    if current > LIMIT:
        break
    if current % 2 == 1:
        sumTotal += current
    copyPrevious = previous
    previous = current
    current = current + copyPrevious
    


print sumTotal
    
