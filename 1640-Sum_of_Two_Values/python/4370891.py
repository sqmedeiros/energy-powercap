import math


def maxPeople(array, length, target):
    start = 0
    end = length-1
    while(start < end):
        if array[start][0]+array[end][0] == target:
            return array[start][1], array[end][1]
        elif array[start][0]+array[end][0] < target:
            start += 1
        else:
            end -= 1
    return None, None


if __name__ == "__main__":
    totalLength, target = (int(x) for x in (input().split()))
    array = [[int(y), x] for x, y in enumerate(input().split())]
    pendings = dict()
    array.sort(key=lambda x: x[0])

    # if not found:
    x, y = maxPeople(array, totalLength, target)
    if x == None:
        print("IMPOSSIBLE")
    else:
        print(x+1, y+1)