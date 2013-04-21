

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome (n):
    s = 0
    a = n
    N = n
    while n > 0:
        rem = n % 10
        s = s * 10 + rem
        n = n /10
    if s == N:
        return True
    else:
        return False


factor1 = 999
product = 1
lstPalindromes = []
while factor1 >= 100:
    factor2 = 999
    while factor2 >= 100:
        product = factor1 * factor2
        if (isPalindrome(product)):
            lstPalindromes.append(product)
            break
        factor2 -=1
    factor1-=1

greater = lstPalindromes[0]
for numb in lstPalindromes:
    if numb > greater:
        greater = numb

print greater
