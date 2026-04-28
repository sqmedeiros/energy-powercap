def solve(arr, x):
  mp = {}

  for i in range(len(arr)):
    d = x - arr[i]
    if arr[i] not in mp:
      mp[d] = i
    else:
      print(mp[arr[i]] + 1, i + 1)
      return

  print('IMPOSSIBLE')

n, x = map(int, input().split())
arr = list(map(int, input().split()))
solve(arr, x)