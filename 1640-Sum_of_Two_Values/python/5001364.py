n, x = map(int, input().split())
a = list(map(int, input().split()))
s = dict()
ans = ("IMPOSSIBLE", "")
for i in range(n):
    num = a[i]
    if num in s:
        ans = i + 1, 1 + s[ num] 
        break 
    s[x - num] = i

print(*ans)
