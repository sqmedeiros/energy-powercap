n, x = map(int, input().split())
arr = list(map(int, input().split()))
indexArray = list(enumerate(arr))
indexArray.sort(key = lambda it: it[1])
i = 0
j = n-1
while i < j:
    if indexArray[i][1] + indexArray[j][1] == x:
        print(min(indexArray[i][0]+1, indexArray[j][0]+1), max(indexArray[i][0]+1, indexArray[j][0]+1))
        break
    elif indexArray[i][1] + indexArray[j][1] > x:
        j -= 1
    else:
        i += 1
else:
    print("IMPOSSIBLE")