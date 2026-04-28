if __name__ == "__main__":
    n = int(input())
    bosses = list(map(int, input().split()))

    tree = [[] for _ in range(n + 1)]
    for employee, boss in enumerate(bosses, start=2):
        tree[boss].append(employee)

    subordinates = [0] * (n + 1)

    stack = [(1, False)]

    while stack:
        node, processed = stack.pop()
        if processed:
            for child in tree[node]:
                subordinates[node] += 1 + subordinates[child]
        else:
            stack.append((node, True))
            for child in tree[node]:
                stack.append((child, False))

    print(' '.join(map(str, subordinates[1:])))