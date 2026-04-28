# def solve(n: int):
#   arr, m = [], n // 2
#   for i in range(m):
#     arr.append(2*(i + 1))
#   for i in range(n - m):
#     arr.append(2*i + 1)
#   print(*arr)

# def solve():
#   n, m = list(map(int, input().split()))
#   o = max(n, m)
#   p = o*(o - 1) + 1
#   if n == m:
#     print(p)
#     return

#   if o%2 == 0:
#     if o == n:
#       print(p + (o - m))
#     else:
#       print(p - (o - n))
#   else:
#     if o == n:
#       print(p - (o - m))
#     else:
#       print(p + (o - n))

# def solve():
#   n, m, k = list(map(int, input().split()))
#   a = list(map(int, input().split()))
#   b = list(map(int, input().split()))

#   ans = 0;
#   a.sort()
#   b.sort()

#   i = j = ans = 0
#   while i < n and j < m:
#     l = a[i] - k
#     r = a[i] + k

#     if l > b[j]:
#       j += 1
#     elif r < b[j]:
#       i += 1
#     else:
#       ans += 1
#       i += 1
#       j += 1

#   print(ans)

# solve()

# 4 3 5
# 60 45 80 60
# 30 60 75

# def solve():
#   n, x = list(map(int, input().split()))
#   nums = list(map(int, input().split()))

#   nums.sort();

#   ans, l, r = 0, 0, len(nums) - 1
#   while (r >= l):
#     if l == r and nums[l] <= x:
#       ans += 1
#       break

#     s = nums[l] + nums[r]
#     if s <= x:
#       l += 1
#     r -= 1
#     ans += 1

#   print(ans)

# solve()

# 4 10
# 7 2 3 9

# def solve():
#   n = int(input())
#   print(len(set(list(map(int, input().split())))))

# solve()

def solve():
  n, t = list(map(int, input().split()))
  a = list(map(int, input().split()))

  p = [(val, i + 1) for i, val in enumerate(a)]
  p.sort()

  l, r = 0, n - 1
  while r > l:
    s = p[l][0] + p[r][0]
    if s == t:
      print(p[l][1], p[r][1])
      return

    elif s > t:
      r -= 1
    else:
      l += 1

  print('IMPOSSIBLE')


solve()