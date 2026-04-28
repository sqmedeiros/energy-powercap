def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))


    pair_sums = {}

    for i in range(n):
        for j in range(i + 1, n):
            pair_sum1 = arr[i] + arr[j]


            complement = x - pair_sum1

            if complement in pair_sums:

                for prev_i, prev_j in pair_sums[complement]:
                    if prev_i != i and prev_i != j and prev_j != i and prev_j != j:
                        print(prev_i + 1, prev_j + 1, i + 1, j + 1)
                        return


            if pair_sum1 not in pair_sums:
                pair_sums[pair_sum1] = []
            pair_sums[pair_sum1].append((i, j))

    print("IMPOSSIBLE")

solve()