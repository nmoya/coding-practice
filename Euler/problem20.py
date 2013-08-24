import math
'''
n! means n  (n  1)  ...  3  2  1

For example, 10! = 10  9  ...  3  2  1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def fat (n):
    if n == 1 or n == 0:
        return 1
    else:
        return fat(n-1) * n

result = fat(100)
print sum ([int(x) for x in str(result)])


r = dict()
r[0] = 1
def fat2(num):
    result = r.get(num)
    if result:
        return result
    result = fat2(num-1) * num
    r[num] = result
    return result
