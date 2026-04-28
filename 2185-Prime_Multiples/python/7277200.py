import math

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    root = int(math.sqrt(n))
    while root * root < n:
        root += 1

    while root * root > n:
        root -= 1

    ans1 = 0
    ans2 = 0

    def f(pos, taken, prod, canTakeGreater):
        nonlocal ans1, ans2

        if prod > n:
            return

        if pos == k:
            if taken % 2 == 1:
                ans1 += n // prod
            elif taken:
                ans2 += n // prod
            return

        f(pos + 1, taken, prod, canTakeGreater)
        if canTakeGreater or a[pos] < root:
            f(pos + 1, taken + 1, prod * a[pos], canTakeGreater or a[pos] >= root)

    f(0, 0, 1, True)
    print(ans1 - ans2)

if __name__ == "__main__":
    t = 1
    multipleTestCases = False
    if multipleTestCases:
        t = int(input())
    for i in range(1, t + 1):
        solve()