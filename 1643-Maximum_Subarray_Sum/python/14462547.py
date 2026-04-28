n = int(input())
arr = list(map(int, input().split()))
max_here, max_so_far = arr[0], arr[0]
for i in range(1, n):
    max_here = max(arr[i], arr[i]+max_here)
    max_so_far = max(max_here, max_so_far)
print(max_so_far)
