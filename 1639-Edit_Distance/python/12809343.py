a = input()
b = input()
la, lb = len(a), len(b)

if la < lb:
    a, b = b, a
    la, lb = lb, la

prev = list(range(lb + 1))
curr = [0] * (lb + 1)

for i in range(1, la + 1):
    curr[0] = i
    for j in range(1, lb + 1):
        if a[i - 1] == b[j - 1]:
            curr[j] = prev[j - 1]
        else:
            curr[j] = 1 + min(prev[j - 1], prev[j], curr[j - 1])
    prev, curr = curr, prev

print(prev[lb])
