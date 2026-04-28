from collections import deque

n, x = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

for i in range(n):
    arr[i] = (arr[i], i)

arr.sort(key = lambda x: x[0])
pl, pr = 0, n-1

while pl < pr:
    s = arr[pl][0] + arr[pr][0]
    if s == x:
       print(arr[pl][1]+1, arr[pr][1]+1)
       exit()
    elif s < x:
        pl += 1
    else:
        pr -= 1

print("IMPOSSIBLE")