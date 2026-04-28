# import sys
# zz= __debug__
# if not zz:
#     input=sys.stdin.readline
# else:   
#     sys.stdin=open('input.txt', 'r')
#     sys.stdout=open('output.txt','w')


def divBy(n, arr):
    mul = 1
    for i in arr:
        mul = mul * i
    return n//mul

n, k = map(int, input().split())
arr = list(map(int, input().split()))
total = 0

def rec(primes, i, subset):
    ans = 0
    if i >= len(primes):
        if subset:
            return (-1) **(1 + len(subset)) * divBy(n, subset)
        else:
            return 0
    else:
        ans += rec(primes, i + 1, subset)
        subset.append(primes[i])
        ans += rec(primes, i + 1, subset)
        subset.pop()
    return ans

print(rec(arr, 0, []))