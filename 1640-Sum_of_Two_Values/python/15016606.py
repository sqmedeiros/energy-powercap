import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

formatted_arr = [(arr[i], i) for i in range(n)]
formatted_arr.sort()

left = 0 
right = len(arr) - 1

while left < right:
    current_sum = formatted_arr[left][0] + formatted_arr[right][0]

    if current_sum == x:
        print(formatted_arr[left][1] + 1, formatted_arr[right][1] + 1)
        exit()
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print("IMPOSSIBLE")