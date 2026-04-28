import sys

input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

ans = [0 for i in range(x+1)]

for c in arr:
    if c<=x:
        ans[c] = 1

for i in range(min(arr), x):
    for c in arr:
        if i+c<=x:
            ans[i+c] += ans[i]
            ans[i+c] = ans[i+c] % (10**9+7)


print(ans[x])
