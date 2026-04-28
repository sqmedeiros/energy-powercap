n, x = map(int, input().split())
arr = [*map(int, input().split())]


d = [0] * (x+1)

d[0] = 1

for j in arr:
    for i in range(0, x+1):
        if(i+j >= x+1):
            continue
        d[i+j] += d[i] 
        d[i+j] %= 1000000007

print(d[x])