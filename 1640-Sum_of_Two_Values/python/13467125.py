n, x = map(int, input().split())
arr = list(map(int, input().split()))

indexed_arr = [(arr[i], i + 1) for i in range(n)]
indexed_arr.sort()

left, right = 0, n - 1

while left < right:
    current_sum = indexed_arr[left][0] + indexed_arr[right][0]

    if current_sum == x:
        pos1, pos2 = indexed_arr[left][1], indexed_arr[right][1]
        if pos1 > pos2:
            pos1, pos2 = pos2, pos1
        print(pos1, pos2)
        exit()
    elif current_sum < x:
        left += 1
    else:
        right -= 1

print("IMPOSSIBLE")