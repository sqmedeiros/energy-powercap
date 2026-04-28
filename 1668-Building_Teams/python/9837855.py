def solve(n,adj):
    # we begin at the first friend (1) and assign them to team (1). All of team (1)'s friends will go to team (2). All of team (2)'s friends (if not visited) will go to team 1. This process continues
    teams = [0]*(n+1)
    visit = set()
    # naturally, we will do BFS, let team (1) be 1 (True) and Team 2 be (0) False, we will reassign the proper labels at the end, easier to keep track of this way
    from collections import deque
    def bfs(node):
        q = deque([node])
        team = 1
        visit.add(node)
        teams[node] = 1
        while q:
            size = len(q)
            for _ in range(size):
                person = q.popleft()
                for friend in adj[person]:
                    if teams[friend] == teams[person]:
                        return False
                    if friend in visit: continue
                    teams[friend] = 1 if team == 2 else 2
                    visit.add(friend)
                    q.append(friend)
            if team == 1:
                team = 2
            else:
                team = 1
        return True
    res = []   
    for i in range(1, n+1):
        if i not in visit:
            if not bfs(i):
                break
        res.append(teams[i])
    return res if len(res) == n else []

if __name__ == "__main__":
    n,m = [int(s) for s in input().split()]
    adj = {i:[] for i in range(1,n+1)}
    for _ in range(m):
        line = [int(s) for s in input().split()]
        a,b = line[0],line[1]
        adj[a].append(b)
        adj[b].append(a)
    res = solve(n, adj)
    if res:
        for p in res:
            print(p, end=" ")
    else:
        print("IMPOSSIBLE")