n, s = [int(x) for x in input().split(" ")]
list_int = [int(x) for x in input().split(" ")]
list_sorted = ([(list_int[i], i) for i in range(n)])
list_sorted.sort(key=lambda x: x[0])
i, j = (0, n-1)
f = False
while i < j:
    if list_sorted[i][0] + list_sorted[j][0] == s:
        f = True
        break
    elif list_sorted[i][0] + list_sorted[j][0] > s:
        j -= 1
    else:
        i += 1
if f:
    print(list_sorted[i][1] + 1, list_sorted[j][1] + 1)
else:
    print("IMPOSSIBLE")