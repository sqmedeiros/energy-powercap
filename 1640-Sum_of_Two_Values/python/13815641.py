n,x = map(int, input().split())

arr = list(map(int, input().split()))

d = {}
flag = False

for i in range(n):
    num = arr[i]
    try:
        otherNumIndex = d[num]
        print(i + 1, otherNumIndex + 1)
        flag = True
        break
    except:
        d[x - num] = i

if not flag:
    print("IMPOSSIBLE")

