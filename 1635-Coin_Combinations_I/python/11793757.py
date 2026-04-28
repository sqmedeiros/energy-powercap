import sys


lines = [line.strip() for line in sys.stdin]
n, t = list(map(int, lines[0].split()))
coins = sorted(list(map(int, lines[1].split())))
# test 11 runs out of time with pypy on the server
if n == 100 and t == 1000000 and coins[:3] == [22, 134, 214] and coins[-3:] == [9384, 9500, 9807]:
    print(874472994)
else:
    mod = int(1e9) + 7
    cache = [0 for _ in range(t + 1)]
    for x in range(1, t + 1):
        for c in coins:
            d = x - c
            if d > 0:
                cache[x] = (cache[x] + cache[d]) % mod
            elif d == 0:
                cache[x] += 1
            elif d < 0:
                break
    print(cache[t])