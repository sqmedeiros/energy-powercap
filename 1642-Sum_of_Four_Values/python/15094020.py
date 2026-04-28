import sys
from bisect import bisect_left, bisect_right


def input_processor():
    input = sys.stdin.readline

    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    return n, x, arr


def solve(n, x, arr):
    dict = {}

    for i in range(n):
        for j in range(i + 1, n):
            key = [i, j]
            val = arr[i] + arr[j]
            if val not in dict:
                dict[val] = key

    # print(dict)

    for i in range(n):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if x - s not in dict:
                continue
            a, b = dict[x - s]
            if a == i or b == j or a == j or b == i:
                continue
            print(f"{i + 1} {j + 1} {a + 1} {b + 1}")
            return

    print("IMPOSSIBLE")


if __name__ == "__main__":
    n, x, arr = input_processor()
    solve(n, x, arr)