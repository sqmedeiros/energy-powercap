from collections import defaultdict
n,x = map(int, input().split())
arr = list(map(int, input().split()))
dict = defaultdict(int)
flag = False
for i in range(n):
    if arr[i] in dict:
        print(dict[arr[i]] + 1, i + 1)
        flag = True
        break
    dict[x - arr[i]] = i
if not flag:
    print("IMPOSSIBLE")