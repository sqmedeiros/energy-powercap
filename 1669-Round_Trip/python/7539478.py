import sys

input = sys.stdin.readline


# We dfs while checking for whether we have visited a child before, and if so,
# check whether depth > 1 (to prevent cycles of length 2). Qn can be modified for length 3 cycles
# and so on by changing depth.
def solve(n, adjlist):
    visited = [False] * n
    parents = [0] * n
    depths = [0] * n

    def dfs(node):
        st = [node]
        while st:
            node = st.pop()
            visited[node] = True
            for child in adjlist[node]:
                if not visited[child]:  # means lets continue
                    parents[child] = node
                    depths[child] = depths[node] + 1
                    st.append(child)
                else:  # check if we found the node.
                    if abs(depths[child] - depths[node]) > 1:
                        parents[child] = node
                        return child
                    # else ignore, dont need set parent or do anything.
        return -1

    idx = -1
    for i in range(n):
        if not visited[i]:
            idx = dfs(i)
            if idx != -1:
                break

    if idx != -1:
        ans = [idx, parents[idx]]
        while ans[-1] != idx:
            ans.append(parents[ans[-1]])
        print(len(ans))
        print(*map(lambda x: x + 1, ans))
    else:
        print("IMPOSSIBLE")


def main():
    n, m = list(map(int, input().split()))
    edges = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    adjlist = [[] for _ in range(n)]
    for u, v in edges:
        adjlist[u].append(v)
        adjlist[v].append(u)
    solve(n, adjlist)


main()