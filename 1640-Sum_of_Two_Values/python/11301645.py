n, x = map(int, input().split())
arr = [int(x) for x in input().split()]
dic = {}

if x == 1:
    print("IMPOSSIBLE")
else:
    for i in range(n):
        if x - arr[i] in dic:
            print(f'{dic[x - arr[i]] + 1} {i + 1}')
            break
        dic[arr[i]] = i
    else:
        print("IMPOSSIBLE")