I=input
L=len
R=range
s = I()
t = I()
n,m = L(s),L(t)
d = list(R(n+1))
for i in R(m):
    e = d[:]
    d[0] = i+1
    for j in R(n):
        d[j+1] = min(d[j]+1,e[j+1]+1,e[j]+(s[j] != t[i]))
print(d[-1])