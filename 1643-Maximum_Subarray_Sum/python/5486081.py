n = int(input())
a = list(map(int, input().split()))
m = a[0]
mn = 0
cur = 0
for i in a:
    cur += i
    m = max(m, cur - mn)
    mn = min(cur, mn)
print(m)