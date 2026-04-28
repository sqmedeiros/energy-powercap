n = int(input())
l = [int(i) for i in input().split()]

t = 0
ans = 0

for i in l:
    if t + i >= 0:
        t += i
    else:
        t = 0
    ans = max(t, ans)

if max(l) < 0:
    ans = max(l)

print(ans)