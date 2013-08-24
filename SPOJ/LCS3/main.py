import itertools


def LCSubstr(str1, str2):
    L = [[] for x in range(len(str1))]
    for i in range(len(str1)):
        L[i] = [0 for x in range(len(str2))]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if i == 0 or j == 0:
                L[i][j] == 0
            if str1[i] == str2[j]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])

    return L[i][j]


try:
    while True:
        S1 = raw_input()
        S2 = raw_input()
        print LCSubstr(S1, S2)

except EOFError:
    pass
