from collections import defaultdict, deque

def print_path(path, pred, s, d): 
    if s == d: 
        path.append(str(s))
        return True 
    elif d == None: 
        print("IMPOSSIBLE")
        return False 
    else: 
        val = print_path(path, pred, s, pred[d])
        path.append(str(d))
        return val and True 


def print_path_modified(path, pred, s, d): 
    if pred[d] == None:
        return False 
    curr = d 
    path.append(str(d))
    while curr != s: 
        curr = pred[curr]
        if curr is None: 
            print("IMPOSSIBLE")
            return False 
        path.insert(0, str(curr))
    return True 

def solve(g, n, m): 
    s = 1 
    q = deque([(0, s)])
    visited = set()
    visited.add(s)
    pred = defaultdict(int)
    for i in range(n): 
        pred[i] = None 
    while q: 
        dist, curr = q.popleft()
        if curr == n: 
            break 
        for nei in g[curr]: 
            if nei not in visited: 
                visited.add(nei)
                pred[nei] = curr 
                q.append((dist + 1, nei))

    found = False 
    path = []
    found = print_path_modified(path, pred, s, n)
    if found: 
        print(dist + 1)
        print(" ".join(path))

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    g = defaultdict(list)
    for _ in range(m): 
        i, j = list(map(int, input().split()))
        g[i].append(j)
        g[j].append(i)
    # print(g)
    solve(g, n, m)