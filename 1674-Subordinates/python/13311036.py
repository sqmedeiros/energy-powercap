from collections import *
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tree = defaultdict(list)

# 1 1 2 3
# {1: [2, 3], 2: [4], 3: [5]}

for i, parent in enumerate(arr):
    c = i+2
    tree[parent].append(c)
# print(tree)

height = [0]*(n+1)
order = [1]


#5
#3 4 5 1
# 1 -> 5 -> 4 -> 3 -> 2
q = deque([1])
# print(tree)
while q:
    cur = q.popleft()
    for node in tree[cur]:
        order.append(node)
        q.append(node)

# print(order)

for node in order[::-1]:
    if node in tree:
        for child in tree[node]:
            height[node] += 1 + height[child]

print(*height[1:])