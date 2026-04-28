import sys

input = sys.stdin.readline


def dfs(graph, start=0):
    n = len(graph)

    dp = [0] * n
    visited, finished = [False] * n, [False] * n

    stack = [start]
    while stack:
        start = stack[-1]

        # push unvisited children into stack
        if not visited[start]:
            visited[start] = True
            for child in graph[start]:
                if not visited[child]:
                    stack.append(child)
        else:
            stack.pop()

            # base case
            dp[start] += 1

            # update with finished children
            for child in graph[start]:
                if finished[child]:
                    dp[start] += dp[child]

            finished[start] = True

    return visited, dp


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    adjlist = [[] for _ in range(n)]
    for i in range(n - 1):
        adjlist[arr[i] - 1].append(i + 1)
    visited, dp = dfs(adjlist)
    print(*map(lambda x: int(x) - 1, dp))


main()