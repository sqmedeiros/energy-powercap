n = int(input())
s = [int(i) for i in input().split()]

best = s[0]
suma = 0

for i in range(n):
    suma = max(s[i], suma + s[i])
    best = max(best, suma)

print(best)