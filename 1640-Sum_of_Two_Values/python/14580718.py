size_arr, target = map(int, input().split())
arr_values = list(map(int, input().split()))


def two_sum(arr, target):
    _arr = sorted(arr)
    left, right = 0, len(_arr) - 1

    while left < right:
        current_sum = _arr[left] + _arr[right]
        if current_sum == target:
            value_a, value_b = _arr[left], _arr[right]
            index_a = arr.index(value_a) + 1
            if value_a == value_b:
                index_b = arr.index(value_b, index_a) + 1
            else:
                index_b = arr.index(value_b) + 1

            _max = max(index_a, index_b)
            _min = min(index_a, index_b)
            return f"{_min} {_max}"
        elif current_sum < target:
            left += 1
        else:
            right -= 1 if right > 0 else 0

    return "IMPOSSIBLE"


print(two_sum(arr_values, target))