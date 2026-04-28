import sys
sys.setrecursionlimit(2 * (10**5) + 1)
n = int(input())
lst = list(map(int, input().split()))

tree = {}

for child, parent in enumerate(lst, start=2):
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)
    if child not in tree:
        tree[child] = []

answer = [0] * (n + 1)

def dfs(element):
    total = 0
    for sub in tree[element]:
        total += 1 + dfs(sub)
    answer[element] = total
    return total

dfs(1)  

print(*answer[1:])