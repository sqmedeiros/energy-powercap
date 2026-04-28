def main():

    def countMultiples(mask):
        div = 1
        for i in range(k):
            if (mask & (1 << i)) > 0:
                div *= a[i]
                if div > n:
                    return 0
        return n // div

    n, k = readIntArr()
    a = readIntArr()

    ans = 0
    for mask in range(1, 1 << k):
        bitCnts = bin(mask).count('1')
        cnts = countMultiples(mask)
        # perform principle of inclusion and exclusion
        if bitCnts % 2 == 1:
            ans += cnts
        else:
            ans -= cnts
    print(ans)

    return

import sys
input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.

def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))

def readIntArr():
    return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]

def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
    dv=defaultValFactory;da=dimensionArr
    if len(da)==1:return [dv() for _ in range(da[0])]
    else:return [makeArr(dv,da[1:]) for _ in range(da[0])]

def queryInteractive(a, b, c):
    print('? {} {} {}'.format(a, b, c))
    sys.stdout.flush()
    return int(input())

def answerInteractive(ansArr):
    print('! {}'.format(' '.join([str(x) for x in ansArr])))
    sys.stdout.flush()

inf=float('inf')
# MOD=10**9+7
# MOD=998244353

from math import gcd,floor,ceil
import math
# from math import floor,ceil # for Python2

for _abc in range(1):
    main()