import sys
sys.setrecursionlimit(10**6)

def dfs(node, adjacency_list, result):
    count = 0
    for child in adjacency_list[node]:
        count += 1 + dfs(child, adjacency_list, result)
    result[node] = count
    return count

def calculate_subordinates(n, supervisor_list):
    result = [0] * n
    dfs(0, supervisor_list, result)
    return result

n = int(input())
supervisor_list = [[] for _ in range(n)]

supervisors = list(map(int, input().split()))
for i in range(1, n):
    supervisor = supervisors[i - 1] - 1
    supervisor_list[supervisor].append(i)
print(*calculate_subordinates(n, supervisor_list))