from collections import deque, defaultdict
import sys
sys.setrecursionlimit(200000)
# Use sys.stdin.readline for fast I/O
input = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, input().split(" "))

adj_list = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split(" "))
    adj_list[v].append(u)
    adj_list[u].append(v)

parents = [-1]*(n+1)

def DFS(curr, parent):
    Q = deque([(curr ,parent)])
    while Q:
        curr, parent = Q.pop()
        parents[curr] = parent
        for next in adj_list[curr]:
            if next != parent:
                if parents[next] != -1:
                    path = []
                    while curr != next:
                        path.append(str(curr))
                        curr = parents[curr]
                    path.append(str(next))
                    path.append(path[0])
                    return path
                Q.append((next, curr))
    return False

flag = False

for v in range(n+1):
    if parents[v] == -1:
        if answer:=DFS(v, 0):
            write(str(len(answer)) + "\n")
            write(" ".join(answer) + "\n")
            flag = True 
            break

if not flag:
    write("IMPOSSIBLE\n")





# def DFS(curr, prev):
#     parents[curr] = prev
#     for next in adj_list[curr]:
#         if next != prev:
#             if parents[next] != -1:
#                 path = []
#                 while curr != next:
#                     path.append(str(curr))
#                     curr = parents[curr]
#                 path.append(str(next))
#                 path.append(path[0])
#                 return path
#             elif path := DFS(next, curr):return path
#     return False