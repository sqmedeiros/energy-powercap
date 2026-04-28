import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
""" Single Integer """
def inp():
    return(int(input()))

""" List (NOT STRING) input"""
def inlt():
    return(list(map(int,input().split())))

""" String Input -> List of Chars """
def insr():
    s = input()
    return(list(s[:len(s) - 1]))

""" Spaced-Separated Integer Input """
def invr():
    return(map(int,input().split()))
############ ---- \Input Functions ---- ############

############ ---- Helper Functions ---- ############

class Node:
    def __init__(self, key):
        self.key = key
        self.unreachable_w = None
        self.cum_w = self.unreachable_w
        self.is_finished = False

    def has_leq_w_than(self, other_w):
        return (
            self.cum_w is not None and
            # If want MAX_HEAP -> -self.cum_w <= -other_w
            self.cum_w <= other_w 
        )

    def heap_key(self):
        return (self.cum_w, self.key)

def bfs(weighted_adj_graph, source, update_w_f, identity): # -> node_map
    import heapq
    min_heap = []   # [Node(), ...]

    node_map = {key: Node(key) for key in weighted_adj_graph}
    node_map[source].cum_w = identity
    heapq.heappush(min_heap, node_map[source].heap_key())

    while min_heap:
        w, key = heapq.heappop(min_heap)
        node = node_map[key]

        if node.is_finished:
            continue
        node.is_finished = True

        for next_key, next_w in weighted_adj_graph[node.key]:
            potential_w = update_w_f(node.cum_w, next_w)

            if not node_map[next_key].has_leq_w_than(potential_w):
                node_map[next_key].cum_w = potential_w
                heapq.heappush(min_heap, node_map[next_key].heap_key())

    return node_map

def solve(adj_graph):
    node_map = bfs(adj_graph, 1, lambda a, b: a + b, 0)
    cum_dists = [node_map[key].cum_w for key in node_map]
    return cum_dists

############ ---- \Helper Functions ---- ############

############ ---- Main ---- ############
def main():
    n, m = invr()

    from collections import defaultdict
    adj_graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        a, b, c = invr()
        adj_graph[a].append([b, c])

    ans = solve(adj_graph)

    for sub_ans in ans:
        print(sub_ans, end = " ")

main()
############ ---- \Main ---- ############