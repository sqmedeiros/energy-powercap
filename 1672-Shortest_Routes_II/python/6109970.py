from sys import stdin, stdout

def go():
    n, m, q = map(int,stdin.buffer.readline().split())
    inf = 1<<40
    D = [inf]* 250000

    for i in range(n): D[i*501] = 0
    for _ in range(m):
        a, b, c = map(int,stdin.buffer.readline().split())
        a -= 1; b -= 1
        if c < D[a+500*b]:
            D[a+500*b] = D[b+500*a] = c

    for k in range(n):
        for i in range(n):
            if k == i or D[i+500*k] == inf: continue
            for j in range(i):
                if D[i+500*k] + D[k+500*j] < D[i+500*j]:
                    D[i+500*j] = D[j+500*i] = D[i+500*k] + D[k+500*j]

    ans = []
    for _ in range(q):
        a, b = map(int,stdin.buffer.readline().split())
        d = D[(a - 1)+500*(b - 1)]
        ans.append(str(d) if d != inf else '-1')
    stdout.write('\n'.join(ans) + '\n')

go()