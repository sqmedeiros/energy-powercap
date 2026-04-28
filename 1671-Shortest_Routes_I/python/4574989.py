from collections import defaultdict
import sys

ONLINE_JUDGE = True

if not ONLINE_JUDGE:
    sys.stdin = open("test.txt", "r")

############ ---- Input Functions ---- ############

def inp(): # integer
    return(int(input()))
def inlt(): # lists
    return(list(map(int,input().split())))
def insr(): # list of characters
    s = input()
    return(list(s[:len(s) - 1]))
def invr(): # space seperate integers
    return(map(int,input().split()))



############ ---- Solution ---- ############
n, m = inlt()

graph = defaultdict(list)
processed = [False] * (n + 1)

for _ in range(m):
    a, b, w = inlt()
    graph[a].append((b, w))

from heapq import heappush, heappop
def shortest_routes(graph, start, end):
    shortest = [float('inf') for _ in range(end + 1)]
    shortest[start] = 0
    pq = [(0, start)]
    seen_ct = 0
    while pq and seen_ct < end:
        _, node = heappop(pq)
        if processed[node]:
            continue
        processed[node] = True
        for nbr, weight in graph[node]:
            if weight < 0:
                continue
            path_dist = shortest[node] + weight
            if shortest[nbr] > path_dist:
                shortest[nbr] = path_dist
                heappush(pq, (path_dist, nbr))
    return shortest

res = shortest_routes(graph, 1, n)[1:]
sys.stdout.write(" ".join(map(str, res)))
