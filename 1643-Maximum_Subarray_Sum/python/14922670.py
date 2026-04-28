n = int(input())
l = list(map(int, input().split()))
res = float("-inf")

cur = 0
for el in l:
    cur += el  
    res = max(cur, res)
    if cur < 0:
        cur = 0

print(res)