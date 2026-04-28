import sys
input = sys.stdin.readline
# concept of General inclusion-exclusion principle
# except when k == 2
# numbers are being counted twice
n, k = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
product = 1
on = lambda mask, bit : (mask & (1 << bit))
for i in range(1, 1 << k):
    count = 0
    product = 1
    for j in range(i.bit_length()):
        if on(i, j):
            count += 1
            product *= nums[j]

    if count & 1:
        ans += (n // product)
    else:
        ans -= (n // product)   
print(ans)