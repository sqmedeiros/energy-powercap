if __name__ == "__main__":
    I = lambda : map(int, input().split())

    n, x = I()
    coins = sorted(I())

    sol = [1] + [0] * x

    for c in coins:
        for i in range(c, x + 1):
            sol[i] += sol[i - c] % (10 ** 9 + 7)

    print(sol[x] % (10 ** 9 + 7))
