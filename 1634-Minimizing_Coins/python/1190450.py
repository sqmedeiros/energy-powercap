I = lambda : map(int, input().split())

n, x = I()
coins = sorted(I())

sol = [0] + [10 ** 9] * x

# for i in range(1, x + 1):
#     sol[i] = min([sol[i - c] + 1 for c in coins if i >= c], default = 10 ** 9)

for c in coins:
    for i in range(c, x + 1):
        sol[i] = min(sol[i], sol[i - c] + 1)


if sol[x] == 10 ** 9: print("-1")
else: print(sol[x])