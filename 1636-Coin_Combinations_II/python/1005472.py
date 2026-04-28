from sys import stdin, stdout

def input():
    return stdin.readline().rstrip()
M=10**9+7
n,x=map(int,input().split())
a=[int(i) for i in input().split()]
c=[0]*(x+1)
c[0]=1
for i in a:
    for j in range(i,x+1):
        c[j]=(c[j]+c[j-i])%M
print(c[-1])