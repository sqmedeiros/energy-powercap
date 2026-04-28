def solution(n, arr):
    from collections import defaultdict

    tree = defaultdict(list)

    # Build Tree
    for child, parent in enumerate(arr, start=2):
        tree[parent].append(child)

    sol = [0] * (n+1)
    stack = [(1, False)]

    while stack:
        node, visited = stack.pop()
        if not visited:
            stack.append((node, True))
            for child in tree[node]:
                stack.append((child, False))

        else:
            count = 0
            for child in tree[node]:
                count += 1 + sol[child]
            sol[node] = count


    return sol[1:]

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))


    my_sol = solution(n, arr)
    print(*my_sol)