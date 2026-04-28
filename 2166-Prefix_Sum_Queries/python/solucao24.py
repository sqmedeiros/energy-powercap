# Prefix Sum Queries
# https://cses.fi/problemset/task/2166
 
# Given an array of n integers, your task is to process q queries of the following types:
# 1. update the value at position k to u
# 2. what is the maximum prefix sum in range [a,b]?
 
def read_ints():
    return [int(x) for x in input().split()]
 
# The first input line has two integers n and q: the number of values and queries.
n, q = read_ints()
n2 = 1 << (n - 1).bit_length()  # Round up to the nearest power of two
assert n2 >= n
 
# The second line has n integers x1,x2,…,xn: the array values.
 
# Let's use two segment trees to solve this problem.
# The first segment tree is used to store the sum of values in each range.
# The second segment tree is used to store the maximum prefix sum in each range.
 
sums = [0] * (2 * n2)
sums[n2 : n2 + n] = read_ints()
mps = [0] * (2 * n2)
for i in range(n2, n2 + n):
    mps[i] = max(sums[i], 0)
# mps[n2 : n2 + n] = sums[n2 : n2 + n]
for i in reversed(range(1, n2)):
    lc, rc = 2 * i, 2 * i + 1  # children
    sums[i] = sums[lc] + sums[rc]
    mps[i] = max(mps[lc], sums[lc] + mps[rc])
 
# There are q lines describing the queries. Each line has three integers: either "1 k u" or "2 a b".
for _ in range(q):
    query = read_ints()
    if query[0] == 1:
        k, u = query[1:]
        k += n2 - 1
        sums[k] = u
        mps[k] = max(u, 0)
        while (k := k >> 1) > 0:
            lc, rc = 2 * k, 2 * k + 1
            sums[k] = sums[lc] + sums[rc]
            mps[k] = max(mps[lc], sums[lc] + mps[rc])
    else:
        assert query[0] == 2
        a, b = query[1:]
        a += n2 - 1
        b += n2 - 1
 
        # i = a
        # ps_a = 0 # prefix sum of a
        # while i > 1:
        #     if i & 1:  # this is a right child
        #         ps_a += sums[i ^ 1]  # add the sibling
        #     i >>= 1
        # print("ps_a:", ps_a)
 
        if a == b:
            print(max(0, sums[a]))
            continue
 
        sum_l, mps_l = sums[a], mps[a]
        mps_r = mps[b]
 
        while a + 1 < b:  # a and b are not siblings
            if not a & 1:  # a is a left child
                mps_l = max(mps_l, sum_l + mps[a + 1])
                sum_l += sums[a + 1]
            if b & 1:  # b is a right child
                mps_r = max(mps[b - 1], sums[b - 1] + mps_r)
                # mps_r = max(mps[b - 1], sum_r + mps_r)
                # sum_r += sums[b - 1]
            # print("a, b:", a, b)
            # print("sum_l, mps_l:", sum_l, mps_l)
            # print("mps_r:", mps_r)
            a >>= 1
            b >>= 1
        # print("sum_l, mps_l, mps_r:", sum_l, mps_l, mps_r)
        print(max(mps_l, sum_l + mps_r))