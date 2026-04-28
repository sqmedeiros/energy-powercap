import sys
input = sys.stdin.readline

n, x = map(int, input().split())
a = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.append((a[i], i + 1))

arr.sort()

left = 0
right = n - 1

while left < right:
    summa = arr[left][0] + arr[right][0]

    if summa == x:
        print(arr[left][1], arr[right][1])
        sys.exit(0) 

    elif summa < x:
        left += 1
    else:
        right -= 1

print("IMPOSSIBLE")