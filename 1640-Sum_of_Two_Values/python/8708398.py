n, x = map(int, input().split())
a = list(map(int, input().split()))

sorted_a = sorted(enumerate(a), key=lambda x: x[1])

left, right = 0, n - 1
while left < right:
    if sorted_a[left][1] + sorted_a[right][1] == x:
        print(sorted_a[left][0] + 1, sorted_a[right][0] + 1)
        break
    elif sorted_a[left][1] + sorted_a[right][1] < x:
        left += 1
    else:
        right -= 1
else:
    print("IMPOSSIBLE")