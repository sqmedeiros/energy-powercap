def coin(m, n):
    tabel = [0 for _ in range(m+1)]
    tabel[0] = 1

    for i in range(m+1):
        if tabel[i] != 0:
            for j in n:
                if i + j <= m:
                    tabel[i + j] = (tabel[i] + tabel[i+j]) % ((10**9 + 7))
    return tabel[m]


_, m = map(int, input().split())
n = list(map(int, input().split()))

print(coin(m, n))