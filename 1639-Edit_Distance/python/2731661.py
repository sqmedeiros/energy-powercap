a=input()
b=input()
m=len(a)+1
n=len(b)+1
t=[[i+j for j in range(n)] for i in range(m)]
for i in range(1,m):
    c=i-1
    for j in range(1,n):
        d=j-1
        t[i][j]=min(t[c][j]+1,t[i][d]+1,t[c][d]+(a[c]!=b[d]))
print(t[-1][-1])