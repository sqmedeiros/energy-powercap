from __future__ import annotations
import sys
import typing as tp


def find_indices_adding_to_target(
    numbers: tp.Sequence[int], target: int
) -> tuple[int, int, int] | None:
    """Finds 4 indices in numbers with sum equal to target if they exist."""
    # We iterate over all pairs of numbers that can be the first and last
    # indices and then apply the 'Sum of Two Values' solution to the range
    # between them. However, since this can be too slow, we apply a couple of
    # tricks to skip iterations that are unnecessary.

    numbers = [(x, i) for i, x in enumerate(numbers, 1)]
    numbers = sorted(numbers)

    # The first trick will be to compute in O(n^2) the two largest and smallest
    # numbers in each range of indices.
    max_in_range = [
        [None for _ in range(len(numbers))]
        for _ in range(len(numbers))
    ]
    min_in_range = [
        [None for _ in range(len(numbers))]
        for _ in range(len(numbers))
    ]

    def get_max_in_range(l: int, r: int) -> tuple[int, int]:
        """Finds the two largest values in numbers[l, ..., r]"""
        if max_in_range[l][r] is not None:
            return max_in_range[l][r]
        num_l = numbers[l][0]
        if l + 1 == r:
            num_r = numbers[r][0]
            max_in_range[l][r] = (max(num_l, num_r), min(num_l, num_r))
        else:
            next_max = get_max_in_range(l+1, r)
            if num_l > next_max[0]:
                max_in_range[l][r] = (num_l, next_max[0])
            elif num_l > next_max[1]:
                max_in_range[l][r] = (num_l, next_max[1])
            else:
                max_in_range[l][r] = next_max
        return max_in_range[l][r]

    def get_min_in_range(l: int, r: int) -> tuple[int, int]:
        """Finds the two smallest values in numbers[l, ..., r]"""
        if min_in_range[l][r] is not None:
            return min_in_range[l][r]
        num_l = numbers[l][0]
        if l + 1 == r:
            num_r = numbers[r][0]
            min_in_range[l][r] = (min(num_l, num_r), max(num_l, num_r))
        else:
            next_min = get_min_in_range(l+1, r)
            if num_l < next_min[0]:
                min_in_range[l][r] = (num_l, next_min[0])
            elif num_l < next_min[1]:
                min_in_range[l][r] = (num_l, next_min[1])
            else:
                min_in_range[l][r] = next_min
        return min_in_range[l][r]

    for i, (number1, idx1) in enumerate(numbers):
        # If there are several numbers in a row that are the same, we only try
        # the first of these as idx1.
        if i and numbers[i-1][0] == number1:
            continue
        for j in range(len(numbers)-1, i+2, -1):
            number4, idx4 = numbers[j]
            if (
                # If there are several numbers in a row that are the same, we
                # only try the last of these as idx4.
                (j + 1 < len(numbers) and numbers[j+1][0] == number4)
                # If the range has numbers that are too small to reach the
                # target, we skip it.
                or (
                    number1 + number4 + sum(get_max_in_range(i+1, j-1)) < target
                )
                # If the range has numbers that are too large to reach the
                # target, we skip it.
                or (
                    number1 + number4 + sum(get_min_in_range(i+1, j-1)) > target
                )
            ):
                continue

            # Otherwise, if we have gotten here, we have a range that is worth
            # exploring. We thus apply the 'Sum of Two Values' solution to the
            # range [i+1, ..., j-1] to reach target - number1 - number4.
            low_pointer = i+1
            high_pointer = j-1
            while low_pointer < high_pointer:
                number2, idx2 = numbers[low_pointer]
                number3, idx3 = numbers[high_pointer]
                total = number1 + number2 + number3 + number4
                if total == target:
                    return idx1, idx2, idx3, idx4
                elif total < target:
                    low_pointer += 1
                else:
                    high_pointer -= 1
    return None


num_values, target, *numbers = map(int, sys.stdin.read().strip().split())
indices = find_indices_adding_to_target(numbers, target)

if indices is None:
    print("IMPOSSIBLE")
else:
    print(' '.join(map(str, indices)))