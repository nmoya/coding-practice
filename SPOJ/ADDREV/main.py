import itertools

try:
    while True:
        N = int(raw_input())
        for i in range(N):
            num1, num2 = [str(x) for x in raw_input().split(" ")]
            print str(int(num1[::-1]) + int(num2[::-1]))[::-1].strip("0")

except EOFError:
    pass
