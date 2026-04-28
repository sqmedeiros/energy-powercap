MIN = float('-inf')
def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    best_sum = MIN
    current_sum = 0
    for x in numbers:
        current_sum = max(x, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

_ = input()
print(max_subarray([int(x) for x in input().split()]))