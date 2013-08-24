import itertools


def LIS(sequence):
    maxium = max(sequence)
    output = [1 for x in range(len(sequence))]
    for i, current in enumerate(sequence):
        minimumDifference = 999999
        for others in sequence:
            if current == others:
                continue
            if others > current:
                difference = others - current
                if difference > minimumDifference:
                    output[i] -= 1
                    print "Errado:", others
                if difference < minimumDifference:
                    print "Certo: ", others
                    minimumDifference = difference
                    output[i] += 1

    return max(output)

#1 4 2 4 3

try:
    while True:
        S = raw_input()
        SEQ = [int(x) for x in raw_input().split(" ")]
        print LIS(SEQ)

except EOFError:
    pass
