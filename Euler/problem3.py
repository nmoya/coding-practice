

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


number = 600851475143
divide = 2
while True:
    if number % divide ==0:
        number = number / divide
        if number == 1:
            break
    else:
        divide +=1

print divide
