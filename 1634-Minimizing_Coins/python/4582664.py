#import sys
#sys.setrecursionlimit(10**6)


n, s = map(int, input().split())
coins = [int(c) for c in input().split()]
coins.sort()
INF = s + 1
value = [INF]*INF
#ready = [False]*INF


value[0] = 0
for x in range (1,s+1):
    #value[x] = INF
    for c in coins:
        if (x>= c):
            value[x] = min(value[x-c]+1,value[x])

#print(value)
if value[s] < INF:
    print(value[s])
else:
    print(-1)


########## Recursive solution #########

#def solve(x):
#    if x < 0:
#        return INF
#    if x==0:
#        return 0
#    if ready[x]:
#        return value[x]
#    best = INF
#    for c in coins:
#        best = min(best, solve(x-c)+1)
#    value[x] = best
#    ready[x] = True
#    return best
#
#
#
#l = solve(s)
#if l < INF:
#    print(l)
#else:
#    print(-1)
#

