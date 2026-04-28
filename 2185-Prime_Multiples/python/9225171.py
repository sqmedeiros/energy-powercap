j = lambda:map(int,input().split())
n,k = j()
s = [(n,1)]

for p in j():
    s += [(u//p,-v) for u,v in s]

for u,v in s: n -= u*v
print(n)