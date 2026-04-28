import io,os,sys
from collections import deque 
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline





n = int(input())
parent = list(map(int,input().split()))
children = [[] for _ in range(n)]
for i in range(n-1):  
    parent[i] -= 1
    children[parent[i]].append(i+1)
parent = [-1] + parent

queue = deque([0])
seq = []
while queue:
    index = queue.popleft()
    seq.append(index)
    for nextindex in children[index]:
        queue.append(nextindex)


ans = [0]*n

for index in seq[::-1]:
    for nextindex in children[index]:   
        ans[index] += ans[nextindex] + 1

print(*ans) 

