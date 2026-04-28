n = int(input())
a = list(map(int, input().split()))

adj_list = {
}

for i in range(0, n - 1):
    if a[i] not in adj_list:
        adj_list[a[i]] = []
    adj_list[a[i]].append(i + 2)


ans = [0 for i in range(0, n + 2)]

stack = [1]

pivot = [0 if x not in adj_list else len(adj_list[x]) for x in range(0, n + 1)]

# print(pivot)

while len(stack) > 0:
    u = stack[len(stack) - 1]
    if u in adj_list and pivot[u] > 0:
        stack.append(adj_list[u][pivot[u] - 1])
        pivot[u] -= 1
    else:
        stack.pop()
        if u in adj_list:
            for v in adj_list[u]:
                ans[u] += ans[v] + 1

for i in range(0, n):
    print(ans[i + 1], end=' ')