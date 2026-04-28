import sys
 
# each element in the tree has (sum, pre) elements.
def build(arr):
    n = len(arr)
    t = [None] * n + [(x, max(x, 0)) for x in arr]
    for i in range(n-1, 0, -1):
        left, right = t[i << 1], t[(i << 1) + 1]
        t[i] = (left[0] + right[0], max(left[1], left[0] + right[1]))
    return t
 
def range_query(t, l, r):
    n = len(t) // 2
    l += n; r += n
    left_sum, left_pre, right_sum, right_pre = 0, 0, 0, 0
    while l < r:
        if l & 1:
            left_pre = max(left_pre, left_sum + t[l][1])
            left_sum += t[l][0]
            l += 1
        if r & 1 == 0:
            right_pre = max(t[r][1], t[r][0] + right_pre)
            right_sum += t[r][0]
            r -= 1
        l >>= 1
        r >>= 1
    if l == r:
        left_pre = max(left_pre, left_sum + t[l][1])
        left_sum += t[l][0]
        left_pre = max(left_pre, left_sum + right_pre)
        return left_pre
    else:
        left_pre = max(left_pre, left_sum + right_pre)
        return left_pre
    
def update(t, i, u):
    i += len(t)//2
    t[i] = (u, max(0, u))
    i >>= 1
    while i > 0:
        left, right = t[i << 1], t[(i << 1) + 1]
        t[i] = (left[0] + right[0], max(left[1], left[0] + right[1]))
        i >>= 1
    
def solve():
    n, q = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))
 
    queries = []
    for _ in range(q):
        queries.append(tuple(map(int, sys.stdin.readline().split())))
 
    t = build(nums)
 
    response = []
    for query in queries:
        if query[0] == 1:
            update(t, query[1] - 1, query[2])
        elif query[0] == 2:
            response.append(str(range_query(t, query[1] - 1, query[2] - 1)))
    
    sys.stdout.write('\n'.join(response) + '\n')
 
solve()