from collections import deque, defaultdict
# import sys
# sys.stdin, sys.stdout = open("input.txt", "r"), open("output.txt", "w")

graph = defaultdict(list)
visited = []
n, m = -1, -1
cc = []
cc_count = 0
stack = deque()

def is_valid(x, y):
    if not (0 <= x < n and 0 <= y < m):
        return False
    if visited[x][y] or graph[x][y] == "#":
        return False
    return True

def dfs(node):
    stack.append(node)
    while stack:
        node = stack.pop()
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            stack.append(child)

def main():
    global visited, n, m, cc_count
    n, m = map(int, input().split(" "))
    visited = [False for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split(" "))
        graph[a].append(b)
        graph[b].append(a)
    for node in range(1, n + 1):
        if not visited[node]:
            visited[node] = True
            cc_count += 1
            cc.append(node)
            dfs(node)
    print(cc_count - 1)
    for i in range(1, len(cc)):
        print(cc[i - 1], cc[i])

if __name__ == "__main__":
    main()