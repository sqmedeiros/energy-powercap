def main():
    n, x = map(int, input().split())

    a: list[int] = list(map(int, input().split()))

    idx: list[list[int]] = []

    for i, ai in enumerate(a):
        idx.append([ai, i + 1])

    idx = sorted(idx)


    l, r = 0, n - 1


    while l < r:
        if idx[l][0] + idx[r][0] == x:
            print(idx[l][1], idx[r][1])
            return
        elif idx[l][0] + idx[r][0] > x:
            r -= 1
        else:
            l += 1



    print("IMPOSSIBLE")


if __name__ == "__main__":
    main()