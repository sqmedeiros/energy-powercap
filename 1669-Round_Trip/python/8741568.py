import sys
sys.setrecursionlimit(1000000)

from collections import defaultdict


UNPROCESSED = 0
PROCESSING = 1
PROCESSED = 2

def find_round_trip(adj):
    status = {node: UNPROCESSED for node in adj.keys()}
    parent = {node: None for node in adj.keys()}
    def find_cycle(node): # None if no cycle is found, start, end
        status[node] = PROCESSING
        for next_node in adj[node]:
            if status[next_node] == PROCESSING and parent[node] != next_node:
                return node, next_node

            if status[next_node] == UNPROCESSED:
                parent[next_node] = node
                result = find_cycle(next_node) 
                if result is not None:
                    return result

        status[node] = PROCESSED
        return None

    def make_cycle(start, end):
        cycle = [end]
        node = start
        while node != end:
            cycle.append(node)
            node = parent[node]
        cycle.append(end)
        return cycle

    for node in adj:
        if status[node] == UNPROCESSED:
            result = find_cycle(node)
            if result is None:
                continue
            return make_cycle(*result)
    return [] 



n, m = [int(i) for i in input().split()]
adj = defaultdict(list)
for i in range(m):
    u, v = [int(i) for i in input().split()]
    adj[u].append(v)
    adj[v].append(u)

trip = find_round_trip(adj)
if trip == []:
    print("IMPOSSIBLE")
else:
    print(len(trip))
    print(*trip, sep=" ")