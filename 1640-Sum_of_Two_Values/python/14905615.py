n, x = map(int, input().split())
arr = list(map(int, input().split()))
indexed_arr = [(val, idx) for idx, val in enumerate(arr)]
indexed_arr.sort(key=lambda item: item[0])
low, high = 0, n - 1
found = False
while low < high:
    s = indexed_arr[low][0] + indexed_arr[high][0]
    if s == x:
        print(indexed_arr[low][1] + 1, indexed_arr[high][1] + 1)
        found = True
        break
    elif s > x:
        high -= 1
    else:
        low += 1
if not found:
    print("IMPOSSIBLE")