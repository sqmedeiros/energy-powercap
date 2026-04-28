n = int(input())
a = list(map(int, input().split()))
sum = 0
maxsum = -1000000000
for i in range(n):
    sum += a[i]
    maxsum = max(maxsum, sum)
    if sum < 0:
        sum = 0
print(maxsum)