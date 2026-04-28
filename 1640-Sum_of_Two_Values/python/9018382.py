from bisect import bisect_right as br, bisect_left as bl
from collections import defaultdict

n, target = [int(n) for n in input().split()]
array = [int(n) for n in input().split()]

sorted_array = sorted(array)
sorted_array = sorted_array[: bl(sorted_array, target)]

if not sorted_array:
    print("IMPOSSIBLE")

else:
    loc = defaultdict(list)
    for i, v in enumerate(array):
        loc[v].append(i)

    prev = None
    for index, elm in enumerate(sorted_array):
        if elm == prev:
            continue

        other_index = br(sorted_array, target - elm, lo=index + 1) - 1
        if other_index > index:
            other_elm = sorted_array[other_index]
            if elm + other_elm == target:
                pair = (loc[elm].pop() + 1, loc[other_elm].pop() + 1)
                print(" ".join(str(p) for p in pair))
                break

        prev = elm

    else:
        print("IMPOSSIBLE")