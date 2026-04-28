'''
Sum of Four Values
https://codeforces.com/gym/102961/problem/Y
'''
import sys

n, s = map(int,input().split())
a = list(map(int,input().split()))
res = {}

for i in range(n):
    for j in range(i+1,n):
        ss = s - a[i] - a[j]
        if ss in res:
            print(i+1,j+1,res[ss][0]+1,res[ss][1]+1)
            sys.exit(0)
    for j in range(i):
        res[a[j]+a[i]] = (i,j)
print('IMPOSSIBLE')
