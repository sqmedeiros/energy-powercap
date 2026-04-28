
def main():
    n, x = map(int, input().split())
    t = [int(i) for i in input().split()]
    a = []
    for i in range(n):
        a.append((t[i], i + 1))
    a.sort()

    l, r = 0, n - 1
    while l < r:
        s = a[l][0] + a[r][0]
        if s == x:
            p = [a[l][1], a[r][1]]
            print(min(p), max(p))
            return
        elif s < x:
            l += 1
        else:
            r -= 1
    print("IMPOSSIBLE")

main()