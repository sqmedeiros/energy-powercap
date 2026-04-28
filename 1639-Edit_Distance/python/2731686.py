I=input
R=range
a=I()
b=I()
m=len(a)+1
n=len(b)+1
t=[[i+j for j in R(n)] for i in R(m)]
for i in R(1,m):
    c=i-1
    for j in R(1,n):
        d=j-1
        t[i][j]=min(t[c][j]+1,t[i][d]+1,t[c][d]+(a[c]!=b[d]))
print(t[-1][-1])