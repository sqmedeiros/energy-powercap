n, x = map(int, input().split())
a = list(map(int, input().split()))

copy = a[:]
a.sort()

left, right = 0, len(a)-1
saida = []

while left < right:
    current = a[left] + a[right]

    if current == x:
        saida.append(a[left])
        saida.append(a[right])
        break
    elif current < x:
        left += 1
    else:
        right -= 1

if not saida:
    print("IMPOSSIBLE")
else:
    val1, val2 = saida
    pos1 = copy.index(val1)

    if val1 == val2:
        pos2 = copy.index(val2, pos1+1)
    else:
        pos2 = copy.index(val2)

    if pos1 > pos2:
        print(str(pos2 + 1)+ " " + str(pos1 + 1))
    else:
        print(str(pos1 + 1)+ " " + str(pos2 + 1))