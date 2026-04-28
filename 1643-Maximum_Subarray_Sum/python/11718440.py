n = int(input())
a = list(map(int,input().split()))

prefix = []

total = 0
for i in range(len(a)):
    total += a[i]
    prefix.append(total)
# print(prefix)

mini = 0
ans = a[0]
for i in range(n):
    # print(prefix,mini)
    ans = max(prefix[i] - mini,ans)
    if prefix[i] < mini:
        mini = prefix[i]
print(ans)