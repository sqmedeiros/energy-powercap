"""
https://cses.fi/problemset/task/1674
"""


def dfs(start: int, parent: int, adj: list) -> list:
    n = len(adj)
    cnt_lst = [0] * n

    stack = [(start, parent, False)]  # (node, parent, visited?)
    while stack:
        node, par, visited = stack.pop()
        if not visited:
            cnt_lst[node] = 1
            # for post-processing
            stack.append((node, par, True))
            for child in adj[node]:
                if child != par:
                    stack.append((child, node, False))
        else:
            # Post-processing
            for child in adj[node]:
                if child != par:
                    cnt_lst[node] += cnt_lst[child]
    return cnt_lst


def solve(adj: list) -> list:
    cnt_lst = dfs(1, -1, adj)
    for i in range(len(cnt_lst)):
        cnt_lst[i] -= 1  # exclude self
    return cnt_lst[1:]  # 1-indexed


def main():
    n = int(input().strip())
    adj = [[] for _ in range(n + 1)]  # 1-indexed
    for i, x in enumerate(list(map(int, input().strip().split()))):
        person = i + 2  # 1-indexed, start from 2
        adj[x].append(person)

    ans = solve(adj)
    print(*ans)


main()