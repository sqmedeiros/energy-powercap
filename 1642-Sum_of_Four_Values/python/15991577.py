import sys

input = sys.stdin.buffer.readline

n,s = map(int,input().split())
a = list(map(int,input().split()))

d = {}
for i in range(2,n-1):
    for j in range(i-1): #ONE SIDE: list all the sums from the left (before i)
        d[a[j] + a[i-1]] = (j+1,i) #to 1-index
    for j in range(i+1,n): #SECOND SIDE: check for every pair from the right
        #since the dictionary is accumulated before, every four point solution is guaranteed to be checked
        if d.get(s - a[i] - a[j],0):
            print(*d[s - a[i] - a[j]],i+1,j+1)
            sys.exit(0)

print('IMPOSSIBLE')