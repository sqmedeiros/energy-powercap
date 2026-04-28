from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    pair_sums = defaultdict(list)

    for i in range(n):
        for j in range(i+1, n):
            total = arr[i] + arr[j]
            pair_sums[total].append((i, j))

    for i in range(n):
        for j in range(i+1, n):
            curr_sum = arr[i] + arr[j]
            needed = x - curr_sum

            if needed in pair_sums:
                for k, l in pair_sums[needed]:
                    if len(set([i, j, k, l])) == 4:
                        print(i+1, j+1, k+1, l+1)
                        return

    print("IMPOSSIBLE")

if __name__ == '__main__':
    solve()