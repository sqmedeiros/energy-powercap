def solve():
    n, m = map(int, input().split())

    edges = [list() for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda s: int(s) - 1, input().split())
        edges[a].append(b)
        edges[b].append(a)
    team = [0] * n

    q = []

    for i in range(n):
        if team[i] == 0:
            q.append((i, 1))
        while q:
            x, t = q.pop()
            team[x] = t
            for edge in edges[x]:
                if team[edge] == t:  # conflicting
                    print('IMPOSSIBLE')
                    return
                if team[edge] == 0:  # unassigned
                    q.append((edge, 1 if t == 2 else 2))

    print(' '.join(map(str, team)))


if __name__ == '__main__':
    solve()
