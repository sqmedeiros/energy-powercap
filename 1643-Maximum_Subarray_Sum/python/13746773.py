x = -10000000009
y = 0
n = int(input())
sl = list(map(int, input().split()))
for i in range (n):
    y+=sl[i]
    x = max(x,y)
    if y < 0:
        y = 0
print(x)