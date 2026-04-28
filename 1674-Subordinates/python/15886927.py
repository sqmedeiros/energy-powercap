import sys

input = sys.stdin.readline

N = int(input())

line = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for i in range(1, N):
    par_i = line[i-1] - 1 # index for parent
    adj[i] += [par_i]
    adj[par_i] += [i]


size = [1]*N

def dfs_subtree_size(root):
    stack = [(root, None, 0)] # node, parent, processing status

    while stack != []:
        node, par, status = stack.pop()

        if status == 0:
            # start processing
            stack.append((node, par, 1))

            for c in adj[node]:

                if c == par:
                    continue

                stack.append((c, node, 0))

        else:
            # done processing children

            for c in adj[node]:
                if c == par:
                    continue

                size[node] += size[c]

dfs_subtree_size(0)

for i in range(N):
    size[i] -= 1

print(*size)