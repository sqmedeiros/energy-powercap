from collections import defaultdict
import sys
sys.setrecursionlimit(150000)
n, m = map(int, input().split())
db = [0]*n

d =defaultdict(list)
for _ in range(m):
    i,j = map(int, input().split())
    d[i].append(j)
    d[j].append(i)


cr = [0]*n


def bfs_cr(x,z):
    global d
    sobr = [x]
    cr[x-1] = z
    while sobr:
        pr = []
        for i in sobr:
            for j in d[i]:
                if cr[j-1] == z:
                    return False
                if cr[j-1] == -z:
                    continue
                cr[j-1] = -z
                pr.append(j)
        sobr = pr[:]
        z = -z
    return True



for i in range(1,n):
    if cr[i-1] == 0:
        if bfs_cr(i,1):
            continue
        else:
            print('IMPOSSIBLE')
            break
else:
    print(*list(map(lambda x: 1 if x == 1 else 2, cr)))