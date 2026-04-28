import sys
sys.setrecursionlimit(3 * 10**6)
input = sys.stdin.readline

n = int(input())
parents = list(map(int, input().split()))

# xây danh sách con
children = [[] for _ in range(n)]
for i in range(1, n):
    boss = parents[i-1] - 1
    children[boss].append(i)

res = [0] * n

# iterative DFS (postorder)
stack = [(0, 0)]  # (node, state), state=0 nghĩa là chưa xử lý con
order = []

while stack:
    u, state = stack.pop()
    if state == 0:
        stack.append((u, 1))           # sẽ quay lại node u sau khi xử lý con
        for v in children[u]:
            stack.append((v, 0))
    else:
        # tất cả con đã xử lý xong
        subtotal = 0
        for v in children[u]:
            subtotal += res[v] + 1
        res[u] = subtotal

sys.stdout.write(" ".join(map(str, res)))