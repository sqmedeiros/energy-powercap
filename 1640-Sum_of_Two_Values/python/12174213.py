def solve():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arrs = set(arr)
    f = False
    for i in range(n):
        if (x - arr[i]) in arrs:
            index = arr.index((x - arr[i]))
            if index != i:
                res = [i + 1, index + 1]
                f = True
                break
    if f:
        print(res[0], res[1])
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    solve()