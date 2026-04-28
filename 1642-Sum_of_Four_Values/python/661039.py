def sum_four_values(x, n, arr):
    sum_two_interger = {}
    for i in range(n):
        for j in range(i + 1, n):
            _comp = x - arr[i] - arr[j]
            if _comp in sum_two_interger:
                k, l = sum_two_interger[_comp]
                return ' '.join(map(str, [i + 1, j + 1, k + 1, l + 1]))
        for j in range(i):
            if i == j:
                continue
            _sum = arr[i] + arr[j]
            sum_two_interger[_sum] = (i, j)
    return 'IMPOSSIBLE'


n, x = map(int, input().split())
arr = list(map(int, input().split()))

print(sum_four_values(x, n, arr))