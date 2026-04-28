s = list(input())
t = list(input())
nex = [len(t) - j for j in range(len(t) + 1)]

for i in range(len(s) - 1, -1, -1):
    curr = [0] * (len(t) + 1)
    curr[-1] = len(s) - i
    for j in range(len(t) - 1, -1, -1):
        if s[i] == t[j]:
            curr[j] = nex[j + 1]
        else:
            curr[j] = 1 + min(nex[j], nex[j + 1], curr[j + 1])
    nex = curr
print(nex[0])