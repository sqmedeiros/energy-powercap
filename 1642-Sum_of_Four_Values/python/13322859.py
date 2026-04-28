def four_sum(n, target, nums):
    arr = [(nums[i], i) for i in range(n)]
    arr.sort(key = lambda x: x[0])

    for i in range(n - 3):
        if i > 0 and arr[i - 1][0] == arr[i][0]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and arr[j - 1][0] == arr[j][0]:
                continue
            k, l = j + 1, n - 1
            diff = target - (arr[i][0] + arr[j][0])
            while k < l:
                if arr[k][0] + arr[l][0] < diff:
                    k += 1
                elif arr[k][0] + arr[l][0] > diff:
                    l -= 1
                else:
                    return f"{arr[i][1] + 1} {arr[j][1] + 1} {arr[k][1] + 1} {arr[l][1] + 1}"

    return "IMPOSSIBLE"

n, x = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
print(four_sum(n, x, arr))