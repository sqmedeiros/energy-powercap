n,m = map(int,input().split())

P = list(range(n))
S = [1]*n

def F(x):
    if P[x] != x:
        P[x] = F(P[x])
    return P[x]

def U(x,y):
    u,v = F(x),F(y)
    if S[u] > S[v]:
        S[u] += S[v]
    P[v] = u

for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    U(a,b)

G = list(set(F(x) for x in range(n)))
l = len(G)
print(l-1)
for i in range(l-1):
    print(G[i]+1, G[i+1]+1)