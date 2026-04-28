def DFS(tree, start):

    stack = [[start, 0]]
    ans = [0] * (len(tree) + 1)

    while stack:
        node, state = stack.pop()
        if state == 0: 
            stack.append([node, 1])  
            for child in reversed(tree[node]): 
                stack.append([child, 0])
        else:  
            cnt = 0
            for child in tree[node]:
                cnt += 1 + ans[child]
            ans[node] = cnt

    return ans


n = int(input())
tree = {}
arr = list(map(int, input().split()))
for i in range(n):
    tree[i + 1] = []
for i in range(n - 1):
    tree[arr[i]].append(i + 2)

ans = DFS(tree, 1)
print(*ans[1:]) 