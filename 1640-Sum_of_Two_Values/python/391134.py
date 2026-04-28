from sys import *
input = stdin.readline

n,x = map(int,input().split())
a = list(map(int,input().split()))

tp = []
for i in range(n):
    tp.append((a[i],i+1))
tp.sort(key = lambda x : (x[0],x[1]))

i = 0 
j = n - 1

ans = []
ch = 0
while(i<j):
    if(tp[i][0]+tp[j][0] == x):
        ch = 1
        ans.append((tp[i][1],tp[j][1]))
        break
    elif(tp[i][0]+tp[j][0]>x):
        j -= 1
    else:
        i += 1


if(ch):
    p = min(ans[0][0],ans[0][1])
    q = max(ans[0][0],ans[0][1])
    print(p,q)
else:
    print("IMPOSSIBLE")