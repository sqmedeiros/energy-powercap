input()
xs = input().split()
m = int(xs[0])
s = 0
for x in xs:
    x = int(x)
    s += x
    if m < s:
        m = s
    if s < 0:
        s = 0
print(m)