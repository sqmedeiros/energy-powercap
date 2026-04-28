n = int(input())
a = list(map(int, input().split()))

cb = a[0]
inc = a[0]
for i in range(1, n):
    inc = max(inc + a[i], a[i]) 
    cb = max(cb, inc)

print(cb)