n, x = map(int, input().split())

lst = list(map(int, input().split()))

h = {}

found = False

for i in range(n):
    if lst[i] >= x:
        continue
    if found:
        break
    for j in range(i+1, n):
        s = lst[i]+lst[j]
        if s >= x:
            continue
        c = x - s
        if c in h:
            if i != h[c][0] and i != h[c][1] and j != h[c][0] and j != h[c][1]:
                print(i+1, j+1, h[c][0]+1, h[c][1]+1)
                found = True
                break
        if s not in h:
            h[s] = (i, j)


if not found:
    print('IMPOSSIBLE')