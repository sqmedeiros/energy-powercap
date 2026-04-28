n, x = list(map(int, input().split()))
ints = list(map(int, input().split()))

l = sorted(enumerate(ints, 1),key=lambda p: p[1])
i, f = 0, len(l)-1
points = []
while i < f:
    if l[i][1] + l[f][1] > x:
        f -= 1
    elif l[i][1] + l[f][1] < x:
        i += 1
    else:
        points = f'{l[i][0]} {l[f][0]}'
        break
if points:
    print(points)
else:
    print('IMPOSSIBLE')





