import sys
from collections import defaultdict, deque

data = sys.stdin.read().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1

graph = defaultdict(list)
for i in range(m):
    u = int(data[index])
    index += 1
    v = int(data[index])
    index += 1
    graph[u].append(v)
    graph[v].append(u)

used = [False] * (n + 1)
prev_list = [-1] * (n + 1)

def find_cycle(start):
    stack = [(start, -1, 0)]  # (current, parent, neighbor_index)
    used[start] = True
    prev_list[start] = -1

    while stack:
        v, forbidden, idx = stack[-1]

        if idx == len(graph[v]):
            stack.pop()
            continue

        stack[-1] = (v, forbidden, idx + 1)  # increment index
        u = graph[v][idx]

        if u == forbidden:
            continue

        if used[u]:
            # Cycle detected via back edge to u
            # Overwrite prev_list[u] = v to form cycle pointer (matching your original logic)
            prev_list[u] = v
            return u

        used[u] = True
        prev_list[u] = v
        stack.append((u, v, 0))

    return -1

def main():
    for v in range(1, n + 1):
        if not used[v]:
            node = find_cycle(v)
            if node != -1:
                length, trip = 1, [str(node)]
                current = prev_list[node]
                while current != node:
                    length += 1
                    trip.append(str(current))
                    current = prev_list[current]
                length += 1
                trip.append(str(node))
                print(length)
                print(' '.join(trip))
                return

    print("IMPOSSIBLE")

if __name__ == "__main__":
    main()