n = int(input())
arr = list(map(int, input().split()))
prefsums = [0] * n
for i in range (n):
    prefsums[i] = prefsums[i-1]+arr[i]
answ = -(1e10)
minprefsum = 0
for i in range (n):
    answ = max(answ, prefsums[i] - minprefsum)
    minprefsum = min(minprefsum, prefsums[i])
print(answ)