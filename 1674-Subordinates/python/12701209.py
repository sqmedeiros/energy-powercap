import collections
n = int(input())
a = [int(x) - 1 for x in input().split(' ')]
b, s, c = [0] * n, [0] * n, 1
for x in a:
    b[x] += 1
q = collections.deque()
for i in range(n):
    if b[i] == 0:
        q.append(i)
while c:
    c = q.popleft()
    if c == 0:
        break
    u = a[c - 1]
    b[u] -= 1
    s[u] += s[c] + 1
    if b[u] == 0:
        q.append(u)
print(*s)