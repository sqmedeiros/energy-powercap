from sys import stdin
input=stdin.readline
n,=map(int,input().split())
a=[int(i) for i in input().split()]
s=0
mx=-10**19
for i in a:
    s=max(s+i,i)
    mx=max(mx,s)
print(mx)



