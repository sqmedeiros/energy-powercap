def count_subordinates(count, boss_arr):
    tree = {}
    for i in range(count):
        tree[i + 1] = []

    # O(n)
    for i in range(len(boss_arr)):
        boss = boss_arr[i]
        child = i + 2
        tree[boss].append(child)

    memo = [0 for _ in range(count)]
    added = set()

    stack = [1]

    # O(n) -- each node is visited once or twice
    while len(stack) > 0:
        current = stack[-1]

        if current in added:
            if current != 1:
                parent = boss_arr[current - 2]
                memo[parent - 1] += memo[current - 1] + 1
                stack.pop()
                continue
            else:
                stack.pop()
                continue

        if len(tree[current]) == 0:
            memo[current - 1] = 0
            parent = boss_arr[current - 2]
            memo[parent - 1] += 1
            stack.pop()
            continue

        for child in tree[current]:
            stack.append(child)
        added.add(current)

    return memo


if __name__ == "__main__":
    count = int(input())
    arr = [int(x) for x in input().strip().split()]
    result = count_subordinates(count, arr)
    print(" ".join([str(x) for x in result]))