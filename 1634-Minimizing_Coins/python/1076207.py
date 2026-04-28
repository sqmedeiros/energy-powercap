n, s = map(int, input().split())
c = [int(x) for x in input().split()]

d = [-1] * (s + 1)
d[0] = 0
q, head, tail = [0] * (s + 1), 0, 0

while d[s] == -1 and head <= tail:
    x = q[head]
    head += 1

    for y in c:
        if x + y <= s and d[x + y] == -1:
            d[x + y] = d[x] + 1
            tail += 1
            q[tail] = x + y

print(d[s])