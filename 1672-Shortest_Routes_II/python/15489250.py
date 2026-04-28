#from collections import deque
import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())

# xlines = [map(int, line.split()) for line in sys.stdin.readlines()]
# xnums = list(map(int, sys.stdin.read().split())) about 10% slower
# xnums = deque(map(int, sys.stdin.read().split())) about 20% slower
# xnums = list(reversed(list(map(int, sys.stdin.read().split())))) about 15% slower

INF = 2**62
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for r in range(m):
    a, b, c = map(int, input().split()) # xlines[r]
    #a = xnums.pop()
    #b = xnums.pop()
    #c = xnums.pop()

    a -= 1
    b -= 1
    if c < dist[a][b]:
        dist[a][b] = c
        dist[b][a] = c

for k in range(n):
    wk = dist[k]
    for i in range(n):
        wi = dist[i]
        # wik = dist[min(k,i)][max(k,i)]
        wik = wi[k]
        if wik >= INF:
            continue
        for j in range(1,n):
            wij = wi[j]
            wkj = wk[j]
            new_weight = wik + wkj
            if wij > new_weight:
                dist[i][j] = new_weight
        for j in range(0): # range(k,n):
            wij = wi[j]
            wkj = wk[j]
            new_weight = wik + wkj
            if wij > new_weight:
                dist[i][j] = new_weight

finalans = []

#base = 3*m
for r in range(q):
    a, b = map(int, input().split()) # xlines[r+m]
    #a = xnums.pop() # xnums[base]
    #b = xnums.pop() # xnums[base+1]

    a -= 1
    b -= 1
    if a > b:
        a,b = b,a
    ans = dist[a][b]
    if dist[a][b] >= INF:
        ans = -1
    print(ans)
    finalans.append(ans)

#    base += 2

# print("\n".join(map(str,finalans)))




## FIXME Use upper triangle only