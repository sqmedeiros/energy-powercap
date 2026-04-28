n, sum_x = map(int, input().split())
vals = list(map(int, input().split()))
def sum_x_2_vals(n, sum_x, vals):
    if n == 1 or sum_x == 1:
        return "IMPOSSIBLE"
    def binary_in(num, vals):
        left, right = 0, k - 1
        mid = (left + right) // 2
        while right - left > 1:
            if vals[mid] > num:
                right = mid
            elif vals[mid] < num:
                left = mid
            else:
                return True
            mid = (left + right) // 2
        if vals[left] == num or vals[right] == num:
            return True
        else:
            return False
    half_sum_x = sum_x // 2
    if sum_x % 2 == 0:
        if vals.count(half_sum_x) >= 2:
            k = vals.index(half_sum_x)
            return (k + 1, k + 2 + vals[k + 1:].index(half_sum_x))
    index_vals = {}
    for i in range(n):
        index_vals[vals[i]] = i + 1
    vals = sorted(set(vals))
    k = len(vals)
    for num in vals:
        if (sum_x % 2 == 0) and (num == half_sum_x):
            pass
        elif binary_in(sum_x - num, vals):
            return (index_vals[num], index_vals[sum_x - num])
    return "IMPOSSIBLE"    
output = sum_x_2_vals(n, sum_x, vals)
if output != "IMPOSSIBLE":
    print(*output)
else:
    print("IMPOSSIBLE")
