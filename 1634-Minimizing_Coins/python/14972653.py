from sys import stdin, stdout

data = stdin.buffer.read().split()
it = iter(data)
ni = lambda: int(next(it))
na = lambda n: [ni() for _ in range(n)]
nf = lambda: float(next(it))
nw = lambda: next(it).decode()
out = bytearray()
wc = lambda c: out.append(c)
ws = lambda s: out.extend(str(s).encode())
wl = lambda l: ws(str(l) + "\n")

n, x = na(2)
c = sorted(na(n))
dp = [0] * (x + 1)
dp[0] = 0
for i in range(1, x + 1):
    dp[i] = 10**6 + 1
    for j in c:
        if i - j < 0:
            break
        dp[i] = min(dp[i], dp[i - j] + 1)

ws(dp[x] if dp[x] != 10**6 + 1 else "-1")

stdout.buffer.write(out + b"\n")