n, target = map(int, input().split())
array = list(map(int, input().split()))
#keep track of origianl string
MapArray = [[k, i] for i, k in enumerate(array)]

#Approch 1 - Two Pointer
MapArray.sort(key= lambda x : x[0])
def solve(n, array):
    i = 0
    j = n  - 1
    while j > i:
        temp  = MapArray[i][0] + MapArray[j][0]
        if temp == target:
            print(MapArray[i][1] + 1, MapArray[j][1] + 1)
            return
        elif temp > target:
            j -= 1
        else:
            i += 1
    print("IMPOSSIBLE")
    return
solve(n,array)