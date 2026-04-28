import sys




n,x = sys.stdin.readline().split()

values = []
for i in (sys.stdin.readline().split()):
    values.append(int(i))
values_ns = values.copy()
values.sort()


check = False
left = 0
right = len(values) -1

while left < right:
    summa = (int(values[left]) + int(values[right]))
    if ((summa) == int(x)):
        eka = (values_ns.index(values[left])+1)
        toka = (values_ns.index(values[right])+1)
        if eka == toka:
            eka = (values_ns.index(values[left])+1)
            toka = (values_ns.index(values[left], eka)+1)
        print (str(eka)  + " " + str(toka))
        check = True
        break
    elif summa > int(x):
        right -= 1
    else:
        left += 1




if not check:
    print("IMPOSSIBLE")