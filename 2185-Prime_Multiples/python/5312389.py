#!/Users/xchen5/opt/anaconda3/bin/python3

import sys
input = sys.stdin.readline

def ri(): return int(input())
def rl(v_type=int): return list(map(v_type, input().split()))
def rs(): return input().rstrip()
def out(x, sep=' '): return sep.join(map(str, x))

'''
Inclusion-Exclusion principle. time: O(K*2^K), space O(K)
Considering all subsets of given prime numbers. The count of numbers divisible by the subset of primes would be n/prod, where prod is the product of the subset of primes. The sign would be positive if the size of subset is odd, and negative otherwise.
'''

N, K = rl()
A = rl()

cnt = N

for mask in range(1 << K):
    nums = [A[i] for i in range(K) if mask & (1 << i)]
    prod = 1
    for x in nums:
        if prod > N // x:
            prod = N + 1
            break
        prod *= x
    if len(nums) % 2:
        cnt += N // prod
    else:
        cnt -= N // prod

print(cnt)