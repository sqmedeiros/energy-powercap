n, x = [int(x) for x in input().split()]
arr = sorted([(int(x), i + 1) for i, x in enumerate(input().split())])

l = 0
r = len(arr) - 1
sol = None
while l < r:
    s = arr[l][0] + arr[r][0]
    if s == x:
        sol = (arr[l][1], arr[r][1])
        break
    if s < x:
        l += 1
    else:
        r -= 1
if sol is None:
    print("IMPOSSIBLE")
else:
    print(sol[0], sol[1])