from collections import defaultdict
from typing import List, Tuple, Optional, Dict, Union
import array

def two_values(lst: List[int], x : int) -> Optional[Tuple[int, int]]:
    # print("two")
    seen_values = {}
    for j, val in enumerate(lst):
        if x - val in seen_values:
            # print(f"returned {(lst.index(x-val), j)} for {lst}, {x}")
            return seen_values[x-val], j
        seen_values[val] = j
    # print(f"returned None for {lst}, {x}")
    return None


def three_values(lst: List[int], x : int) -> Optional[Tuple[int, int, int]]:
    # print("three")
    for i, frst in enumerate(lst):
        # print(i, frst)
        target = x - frst
        # print(target)
        ids = two_values(lst[i+1:], target)
        if ids:
            ids = (ids[0]+i+1, ids[1]+i+1,)
            return (i, ids[0], ids[1])
    return None

def four_values(lst: List[int], x : int) -> Optional[Tuple[int, int, int, int]]:
    # print("four")
    for i, frst in enumerate(lst):
        # print(i, frst)
        target = x - frst
        # print(target)
        ids = three_values(lst[i+1:], target)
        if ids:
            ids = (ids[0]+i+1, ids[1]+i+1, ids[2]+i+1)
            return (i, ids[0], ids[1], ids[2])
    return None



class ValueWithInd:
    """
    acts like an int but with an ind to check for equality
    """
    def __init__(self, val: int, ind: int):
        self.val = val
        self.ind = ind

    def __eq__(self, other):
        return self.val == other.val and self.ind == other.ind

    def __add__(self, other: Union[int, "ValueWithInd"]) -> int:

        if isinstance(other, int):
            return self.val + other

        return self.val + other.val

    def __hash__(self):
        return hash(self.val)


def generate_pairs(lst: List[ValueWithInd]) -> Dict[int, List[Tuple[ValueWithInd, ValueWithInd]]]:
    dct = defaultdict(list)

    for i, first in enumerate(lst):
        for scnd in lst[i+1:]:
            dct[first+scnd].append((first, scnd))

    return dct


n, x = list(map(int, input().split()))

lst = map(int, input().split())
lst = [ValueWithInd(val, i) for i, val in enumerate(lst)]

pairs_dict = generate_pairs(lst)

for i, first in enumerate(lst):
    for scnd in lst[i + 1:]:

        if x - (first + scnd) in pairs_dict:
            pairs = pairs_dict[x - (first + scnd)]

            pairs = [p for p in pairs if not any(elem in (first, scnd) for elem in p)]

            if pairs:
                inds = [elem.ind+1 for elem in (first, scnd, *pairs[0])]
                print(*inds)
                exit(0)



print("IMPOSSIBLE")
exit(0)




a = array.array("l", lst)
m = memoryview(a.tobytes())
out = four_values(m, x)
if out:
    print(*[i+1 for i in out])
else:
    print("IMPOSSIBLE")






















exit(0)
assert False
from typing import List, Tuple, Optional
import array

def two_values(lst: List[int], x : int) -> Optional[Tuple[int, int]]:
    # print("two")
    seen_values = {}
    for j, val in enumerate(lst):
        if x - val in seen_values:
            # print(f"returned {(lst.index(x-val), j)} for {lst}, {x}")
            return seen_values[x-val], j
        seen_values[val] = j
    # print(f"returned None for {lst}, {x}")
    return None


def three_values(lst: List[int], x : int) -> Optional[Tuple[int, int, int]]:
    # print("three")
    for i, frst in enumerate(lst):
        # print(i, frst)
        target = x - frst
        # print(target)
        ids = two_values(lst[i+1:], target)
        if ids:
            ids = (ids[0]+i+1, ids[1]+i+1,)
            return (i, ids[0], ids[1])
    return None

def four_values(lst: List[int], x : int) -> Optional[Tuple[int, int, int, int]]:
    # print("four")
    for i, frst in enumerate(lst):
        # print(i, frst)
        target = x - frst
        # print(target)
        ids = three_values(lst[i+1:], target)
        if ids:
            ids = (ids[0]+i+1, ids[1]+i+1, ids[2]+i+1)
            return (i, ids[0], ids[1], ids[2])
    return None

n, x = list(map(int, input().split()))

lst = list(map(int, input().split()))
a = array.array("l", lst)
m = memoryview(a.tobytes())
out = four_values(m, x)
if out:
    print(*[i+1 for i in out])
else:
    print("IMPOSSIBLE")

