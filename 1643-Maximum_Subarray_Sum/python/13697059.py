n = int(input())
arr = list(map(int, input().split()))
ans = -1000000005
cur = 0
for i in arr:
    cur += i
    ans = max(ans, cur)
    if cur < 0:
        cur = 0
print(ans)