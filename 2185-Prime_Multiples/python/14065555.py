n,k = map(int,input().split())
a = list(map(int,input().split()))

res = 0

def backtrack(start, size, c_product):
    global res

    if size == 0:
        if c_product <= n:
            res_add = n // c_product
            res_sign = 1 if c_size % 2 == 1 else -1
            res += res_sign * res_add
        return

    for i in range(start, k):
        p = c_product * a[i]

        if p > n:
            continue

        backtrack(i+1, size - 1, p)

for c_size in range(1, k+1):
    backtrack(0, c_size, 1)

print(res)