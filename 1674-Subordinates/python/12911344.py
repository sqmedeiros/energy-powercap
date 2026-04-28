from collections import deque
n = int (input())
employee = list(map(int,input().split()))
tree = [[]for _ in range (n+1)]
for i in range (2, n+1) : 
    bos = employee[i-2]
    tree[bos].append(i)
stack = deque ()
stack.append(1)
postorder = []
while stack : 
    node = stack.pop()
    postorder.append(node)
    for child in tree[node] :
        stack.append(child)

bawahan = [0] * (n + 1)

for node in reversed(postorder): 
    for anak in tree[node]:
        bawahan[node] += 1 + bawahan[anak]
print(" ".join (map(str,bawahan[1:])))