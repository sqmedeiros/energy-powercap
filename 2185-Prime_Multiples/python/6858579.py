def solve(i, cnt, curr):
    for j in range(i, k):
        if cnt & 1:
            res[0] -= n // (curr * arr[j])
        else:
            res[0] += n // (curr * arr[j])
        solve(j + 1, cnt + 1, curr * arr[j])


n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = [0]
solve(0, 0, 1)
print(res[0])