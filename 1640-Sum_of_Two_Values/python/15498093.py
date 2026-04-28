n, x = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append((a[i], i+1))
b.sort()
l = 0
r = n - 1
kt = False
while l < r:
    s = b[l][0] + b[r][0]
    if s == x:
        print(b[l][1], b[r][1])
        kt = True
        break
    elif s < x:
        l += 1
    else:
        r -= 1
if not kt:
    print("IMPOSSIBLE")