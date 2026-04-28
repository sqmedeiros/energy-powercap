from collections import defaultdict, OrderedDict, Counter, deque
from itertools import permutations, combinations, product
import math
from pprint import pprint 
# from queue import PriorityQueue
import threading
import sys
from bisect import bisect_left, bisect_right, insort_left
from heapq import heappush, heappop


# MOD = 998244353
MOD = 10**9 + 7

sys.setrecursionlimit(10**5)
threading.stack_size(10**6)
input = sys.stdin.readline
flush = sys.stdout.flush

def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l

def upper_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return r

def find_prime_factors(n):
    factors = defaultdict(int)
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors[divisor] += 1
            n = n / divisor
        else:
            divisor += 1

    return factors

def find_divisors(n):
    sqrt = math.isqrt(n)
    divs = []
    for div in range(1, sqrt+1):
        if n % div == 0:
            divs.append(div)
            if div != n // div:
                divs.append(n // div)

    # divs.sort()        
    return divs

def is_prime(n):
    sq = math.isqrt(n)
    for div in range(2, sq+1):
        if n % div == 0:
            return False
    return True

def soe(start, limit):
    # Initialize a boolean array to mark prime numbers
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Perform Sieve of Eratosthenes
    for i in range(2, math.isqrt(limit) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False

    # Collect primes within the specified range
    primes = []
    for i in range(start, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


def ceil_division(a, b):
    return (a+b-1)//b

def get_triangle_area(x, y):
    area = 0.5 * (x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))
    return area

def prefix_sum(arr):
    prx = []
    cur = 0
    for num in arr:
        cur += num
        # cur %= m
        prx.append(cur)
    return prx

def prefix_max(arr):
    prx = []
    mx = float("-inf")
    for num in arr:
        mx = max(mx, num)
        prx.append(mx)
    return prx

def prefix_min(arr):
    prx = []
    mn = float("inf")
    for num in arr:
        mn = min(mn, num)
        prx.append(mn)
    return prx

def prefixSum2D(a, R, C):
    psa = [[0 for x in range(C)] for y in range(R)]
    psa[0][0] = a[0][0]

    for i in range(1, C):
        psa[0][i] = (psa[0][i - 1] + a[0][i])
    for i in range(1, R):
        psa[i][0] = (psa[i - 1][0] + a[i][0])

    for i in range(1, R):
        for j in range(1, C):
            psa[i][j] = (psa[i - 1][j] + psa[i][j - 1] - psa[i - 1][j - 1] + a[i][j])
    return psa

def sum_interval_2d(prx, row1, col1, row2, col2):
    to_remove_first = prx[row1 - 1][col2] if row1 > 0 else 0
    to_remove_second = prx[row2][col1 - 1] if col1 > 0 else 0
    common = prx[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0
    return prx[row2][col2] - to_remove_first - to_remove_second + common


def sum_interval(prx, start, end):
    if start > end: return 0
    end = min(len(prx) - 1, end)
    start = max(0, start)
    return prx[end] - prx[start-1] if start > 0 else prx[end]

def quadratic_formula(a, b, c):
    ans1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    ans2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return ans1, ans2

def is_between(i1, j1, i2, j2, i3, j3):
    collinear = (j2 - j1) * (i3 - i1) == (j3 - j1) * (i2 - i1)

    if not collinear:
        return False

    within_bounds = (min(i1, i3) <= i2 <= max(i1, i3)) and (min(j1, j3) <= j2 <= max(j1, j3))

    return within_bounds

def slope(x1, y1, x2, y2):
    if x2 == x1: return float("inf")
    x = (y2 - y1) / (x2 - x1)
    return x

def get_counts(arr):
    counts = defaultdict(int)
    for num in arr:
        counts[num] += 1
    return counts

def gcd_arr(arr):
    gcd = arr[0]
    for num in arr:
        gcd = math.gcd(gcd, num)
    return gcd

# CONST = (1 << 31) - 1

def lcm(*integers):
    a = integers[0]
    for b in integers[1:]:
        a = (a * b) // math.gcd (a, b)
    return a

def get_inverse(n):
    global CONST
    return n ^ CONST

def is_palindrome(arr):
    return arr == arr[::-1]

# def is_kalindrome(arr, x, l, r):
#     while l <= r:
#         if arr[l] == arr[r]:
#             l += 1
#             r -= 1
#         else:
#             if arr[l] == x:
#                 l += 1
#             elif arr[r] == x:
#                 r -= 1
#             else:
#                 return False
#     return True

def suffix_sum(arr):
    sm = 0
    ans = []
    rev_arr = arr[::-1]
    for num in rev_arr:
        sm += num
        ans.append(sm)
    return ans[::-1]

def suffix_max(arr):
    mx = float("-inf")
    ans = []
    rev_arr = arr[::-1]
    for num in rev_arr:
        mx = max(mx, num)
        ans.append(mx)

    return ans[::-1]

def kadanes_algo(arr):
    sm = 0
    mx = float("-inf")
    ans = []
    for num in arr:
        sm += num
        if sm < 0:
            sm = 0
        mx = max(mx, sm)
        ans.append(mx)
    return ans

def kadanes_algo_neg(arr):
    sm = 0
    mn = float("inf")
    ans = []
    for num in arr:
        sm += num
        if sm > 0:
            sm = 0
        mn = min(mn, sm)
        ans.append(mn)
    return ans

def arithmitic_seq_sum(a, b, n):
    return (n * (a + b)) // 2

def geometric_seq_sum(a, b, r):
    return (b*r - a) // (r - 1)


def find_diff_char(forbidden_chars):
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in forbidden_chars:
            return char
    return ""

def mod_inverse_euclidean(a, mod):
    g, x, y = extended_gcd(a, mod)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} under mod {mod}")
    else:
        return x % mod

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def sum_law(n):
    if n <= 0: return 0
    return (n * (n + 1)) // 2

def sum_law_diff(l, r):
    return sum_law(r) - sum_law(l-1)

def factorial(start, n, m):
    while n > 1:
        start *= n
        start %= m
        n -= 1

    return start

def lcm_arr(arr):
    ans = 1
    for num in arr:
        ans = lcm(ans, num)

    return ans

def findProductSum(A, n): 

    # calculating array sum (a1 + a2 ... + an) 
    array_sum = 0
    for i in range(0, n, 1): 
        array_sum = array_sum + A[i] 

    # calculating square of array sum 
    # (a1 + a2 + ... + an)^2 
    array_sum_square = array_sum * array_sum 

    # calculating a1^2 + a2^2 + ... + an^2 
    individual_square_sum = 0
    for i in range(0, n, 1): 
        individual_square_sum += A[i] * A[i] 

    # required sum is (array_sum_square - 
    # individual_square_sum) / 2 
    return (array_sum_square - 
            individual_square_sum) // 2


# found = defaultdict(list)

# N = 1001  # Replace with the desired value of N
# d = [N] * N
# d[1] = 0

# for i in range(1, N):
#     for x in range(1, i + 1):
#         j = i + i // x
#         if j < N:
#             d[j] = min(d[j], d[i] + 1)






# print(costs[:20])

# print(costs[:30])


# def knapsack(k, weights, gains):
#     n = len(weights)
#     # Create a DP table with k+1 capacity (0 to k)
#     dp = [[0] * (k + 1) for _ in range(n + 1)]

#     # Iterate through items
#     for i in range(1, n + 1):
#         for w in range(k + 1):
#             if weights[i-1] <= w:  # If the current item can be included
#                 dp[i][w] = max(dp[i-1][w], dp[i-1][w - weights[i-1]] + gains[i-1])
#             else:
#                 dp[i][w] = dp[i-1][w]  # Cannot include the item, carry forward the previous value

#     # The answer will be in dp[n][k], i.e., considering all items and capacity k
#     return dp[n][k]


def knapsack_optimized(k, weights, gains):
    n = len(weights)
    dp = [0] * (k + 1)

    for i in range(n):
        for w in range(k, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + gains[i])

    return dp[k]


def knapsack_optimized_min(k, weights, gains):
    n = len(weights)
    dp = [float("inf")] * (k + 1)

    for i in range(n):
        for w in range(k, weights[i] - 1, -1):
            dp[w] = min(dp[w], dp[w - weights[i]] + gains[i])

    # print(dp)
    return dp[k]


# def power(n, p, m=MOD):
#     if p == 0:
#         return 1
#     if p < 0:
#         return 0

#     if (p & 1 == 0):
#         term = power(n, (p >> 1), m) % m
#         return (term * term) % m
#     else:
#         return ((n % m) * power(n, p - 1, m)) % m


def power(x, y, mod=MOD):
    res = 1
    while y:
        if y & 1:
            res = res * x % mod
        x = x * x % mod
        y //= 2
    return res


def get_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])
    diagonals = []

    # Under and mid
    for j in range(rows):
        diagonal = [matrix[i][i - j] for i in range(j, rows)]
        diagonals.append(diagonal)

    # Above
    for j in range(1, cols):
        diagonal = [matrix[i][i + j] for i in range(rows - j)]
        diagonals.append(diagonal)

    return diagonals

def get_mode(arr):
    arr.sort()
    mode = arr[0]
    h_freq = 1
    cur_freq = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            cur_freq += 1
            if cur_freq > h_freq:
                h_freq = cur_freq
                mode = arr[i]
        else:
            cur_freq = 1

    return mode

def loop_spiral(matrix, n, m):

    rows, cols = n, m
    top, bottom, left, right = 0, rows - 1, 0, cols - 1
    spiral_order = []
    # print(n, m)

    layers = []
    num_layers = min(n, m) // 2
    for _ in range(num_layers):
        layer = []
        # print(spiral_order)
        # TOP ROW
        for i in range(left, right + 1):
            # print(top, i, matrix)
            layer.append(matrix[top][i])

        top += 1

        # print(spiral_order)

        # RIGHT COLUMN
        for i in range(top, bottom + 1):
            layer.append(matrix[i][right])

        right -= 1

        # print(spiral_order)

        # BOTTOM ROW
        for i in range(right, left - 1, -1):
            layer.append(matrix[bottom][i])


        bottom -= 1

        # print(spiral_order)

        # LEFT COLUMN
        for i in range(bottom, top - 1, -1):
            layer.append(matrix[i][left])


        left += 1
        layers.append(layer.copy())



    return layers

def xor_upto(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

def xor_range(l, r):
    return xor_upto(r) ^ xor_upto(l - 1)

def read_numbers(infile=None):
    return list(map(int, input().strip().split())) if infile == None else list(map(int, infile.readline().strip().split()))

def read_int(infile=None):
    return int(eval(input().strip())) if infile == None else int(eval(infile.readline().strip()))

def read_str(infile=None):
    return input().strip() if infile == None else infile.readline().strip()

def get_median(numbers):
    if not numbers:
        return None  # Handle the empty list case

    numbers = sorted(numbers)  # Sort the list
    n = len(numbers)

    # If the list length is odd, return the middle element
    if n % 2 == 1:
        return numbers[n // 2]
    # If the list length is even, return the average of the two middle elements
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return mid1

def factorial_mod(n, m):
    """Calculates n! % m iteratively."""
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % m
    return result

def mod_inverse_euclidean(a, m):
    """Calculates modular inverse of a under modulo m using Extended Euclidean algorithm."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def extended_gcd(a, b):
    """Helper function to find gcd and coefficients of Bezout's identity."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def comb_optimized(n, r, m):
    if n == r or r == 0:
        return 1
    if r > n:
        return 0
    # Calculate n!, r!, and (n-r)! % m
    n_fact = factorial_mod(n, m)
    r_fact = factorial_mod(r, m)
    nr_fact = factorial_mod(n - r, m)

    # Calculate modular inverse of r! and (n-r)! modulo m
    r_fact_inv = mod_inverse_euclidean(r_fact, m)
    nr_fact_inv = mod_inverse_euclidean(nr_fact, m)

    # Calculate the result
    return (n_fact * r_fact_inv % m) * nr_fact_inv % m

def build_full_ones(limit):
    full_ones = []
    cur = 1
    for _ in range(limit):
        full_ones.append(cur)
        cur |= (cur << 1)

    return full_ones


# three_powers = []
# cur = 1
# limit = 10**24
# while cur <= limit:
#     three_powers.append(cur)
#     cur *= 3


# ans = []
# i = 0
# limit = 1000000
# # print("da")
# while True:
#     b = bin(i)
#     s = str(b)[2:]
#     cur = 0
#     # print("la")
#     for j in range(len(s) - 1, -1, -1):
#         if s[j] == "1":
#             cur += (three_powers[len(s) - 1 - j])

#     # print(cur)
#     if cur > limit: break
#     ans.append(cur)
#     # print(cur)
#     i += 1
# m = 10**18
# print(ans)

# print(divs)




def log2_ceil(x):
    if x <= 1:
        return 0 


    bits = x.bit_length() - 1

    if x == (1 << bits):
        return bits
    return bits + 1




# powers = [1]
# cur = 1
# last = 1
# limit = 10**12
# while True:
#     cur += last
#     powers.append(cur)
#     if cur >= limit: break
#     last *= 2

# print(powers[:10])

# MOD = 10**9 + 7
# limit = 10**6 + 1
# dp = [0] * limit
# for num in range(1, limit):
#     if 1 <= num <= 6:
#         dp[num] += 1

#     for dec in range(1, 6 + 1):
#         if num - dec >= 0:
#             dp[num] += dp[num - dec]

#     dp[num] %= MOD

# print(dp[:10])

# factorials = [1]
# cur = 1
# for num in range(1, 200000 + 7):
#     cur *= num
#     factorials.append(cur)
#     cur %= MOD


def common(xl1, xl2, xr1, xr2, yl1, yl2, yr1, yr2):
    xlc = max(xl1, xl2)
    xrc = min(xr1, xr2)
    ylc = max(yl1, yl2)
    yrc = min(yr1, yr2)

    return xlc, ylc, xrc, yrc

def mex(arr):
    n = len(arr)
    present = [False] * (n + 1) 

    for num in arr:
        if 0 <= num <= n:  
            present[num] = True

    for i in range(n + 1):
        if not present[i]:
            return i

    return n + 1

def prefix_xor(arr):
    xor_res = 0
    res = []
    for num in arr:
        xor_res ^= num
        res.append(xor_res)

    return res

def xor_interval(prx, start, end):
    if start > end: return 0
    end = min(len(prx) - 1, end)
    start = max(0, start)
    return prx[end] ^ prx[start-1] if start > 0 else prx[end]


def add(a, b, m):
    h = a + b
    if h >= m:
        h -= m

    if h < 0:
        h += m

    return h

# int mul(int a, int b) {
#     return (a * 1LL * b) % MOD;
# }

def mul(a, b, m):
    return ((a % m) * (b % m)) % m

def count_children(adj, n, parents):
    num_children = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            if v != parents[u]:  # Only count actual children, not back edges
                num_children[u] += 1
    return num_children


# def multinomial_coefficient(n, *groups):
#     """
#     Computes the multinomial coefficient:
#     C(n; k1, k2, ..., km) = n! / (k1! * k2! * ... * km!)

#     using an optimized iterative approach to avoid large factorial computations.
#     """
#     result = 1
#     k_sum = 0  # Tracks the cumulative sum of k1, k2, ...

#     for k in groups:
#         for i in range(k):
#             result *= (n - k_sum)  # Multiply numerator step by step
#             result //= (i + 1)  # Divide denominator step by step
#             k_sum += 1  # Keep track of how many elements are processed

#     return result

def compute_factorial_ratio(n, *groups):
    """ Computes (n!) / (k1! * k2! * ... * km!) efficiently. """
    result = 1
    k_sum = 0  # Tracks cumulative sum of k1, k2, ..., km

    for k in groups:
        for i in range(k):
            if n - k_sum > 0:  # Ensure numerator doesn't go negative
                result *= (n - k_sum)
            result //= (i + 1)  # Integer division to keep precision
            k_sum += 1  # Update processed elements

    return result


# class SegmentTreeXORMax:
#     def __init__(self, arr):
#         self.n = len(arr)
#         self.xor_tree = [0] * (4 * self.n)  # XOR segment tree
#         self.max_tree = [0] * (4 * self.n)  # Max segment tree
#         self.lazy = [0] * (4 * self.n)  # Lazy array for XOR updates
#         self.build(0, 0, self.n - 1, arr)

#     def build(self, idx, L, R, arr):
#         """Build both XOR and MAX segment trees"""
#         if L == R:
#             self.xor_tree[idx] = arr[L]
#             self.max_tree[idx] = arr[L]
#             return
#         mid = (L + R) // 2
#         self.build(2 * idx + 1, L, mid, arr)
#         self.build(2 * idx + 2, mid + 1, R, arr)
#         self.xor_tree[idx] = self.xor_tree[2 * idx + 1] ^ self.xor_tree[2 * idx + 2]
#         self.max_tree[idx] = max(self.max_tree[2 * idx + 1], self.max_tree[2 * idx + 2])

#     def propagate(self, idx, L, R):
#         """ Apply lazy XOR updates """
#         if self.lazy[idx]:  # If there's a pending XOR operation
#             self.xor_tree[idx] ^= self.lazy[idx] * ((R - L + 1) % 2)  # XOR affects only odd-length ranges
#             self.max_tree[idx] ^= self.lazy[idx]  # XOR update for max tree

#             if L != R:  # Propagate to children
#                 self.lazy[2 * idx + 1] ^= self.lazy[idx]
#                 self.lazy[2 * idx + 2] ^= self.lazy[idx]

#             self.lazy[idx] = 0  # Clear lazy value

#     def update_range(self, idx, L, R, ql, qr, x):
#         """XOR a range [ql, qr] with x"""
#         self.propagate(idx, L, R)  # Apply pending updates

#         if qr < L or ql > R:  # Out of range
#             return
#         if ql <= L and R <= qr:  # Fully inside range
#             self.lazy[idx] ^= x
#             self.propagate(idx, L, R)
#             return

#         # Partial overlap
#         mid = (L + R) // 2
#         self.update_range(2 * idx + 1, L, mid, ql, qr, x)
#         self.update_range(2 * idx + 2, mid + 1, R, ql, qr, x)

#         # Merge results
#         self.xor_tree[idx] = self.xor_tree[2 * idx + 1] ^ self.xor_tree[2 * idx + 2]
#         self.max_tree[idx] = max(self.max_tree[2 * idx + 1], self.max_tree[2 * idx + 2])

#     def query_xor(self, idx, L, R, ql, qr):
#         """Get XOR from range [ql, qr]"""
#         self.propagate(idx, L, R)  # Apply pending updates

#         if qr < L or ql > R:  # Out of range
#             return 0
#         if ql <= L and R <= qr:  # Fully inside range
#             return self.xor_tree[idx]

#         # Partial overlap
#         mid = (L + R) // 2
#         left = self.query_xor(2 * idx + 1, L, mid, ql, qr)
#         right = self.query_xor(2 * idx + 2, mid + 1, R, ql, qr)
#         return left ^ right

#     def query_max(self, idx, L, R, ql, qr):
#         """Get maximum value from range [ql, qr]"""
#         self.propagate(idx, L, R)  # Apply pending updates

#         if qr < L or ql > R:  # Out of range
#             return float('-inf')
#         if ql <= L and R <= qr:  # Fully inside range
#             return self.max_tree[idx]

#         # Partial overlap
#         mid = (L + R) // 2
#         left = self.query_max(2 * idx + 1, L, mid, ql, qr)
#         right = self.query_max(2 * idx + 2, mid + 1, R, ql, qr)
#         return max(left, right)



class SparseTable:

    '''
    This is a custom SparseTable that I made :)  mostafa_alaa99
    '''

    def __init__(self, a, n, f):
        self._f = f
        self._table = self._make_sparse_table(a, n, f)

    def _make_sparse_table(self, a, n, f):

        mx_2p = int(math.log2(n))
        matrix = [[0 for _ in range(n)] for _ in range(mx_2p + 1)]
        for j in range(n):
            matrix[0][j] = a[j]

        for j in range(1, mx_2p + 1):
            for i in range(n - (1 << j) + 1):
                left = matrix[j - 1][i]
                right = matrix[j - 1][i + (1 << (j - 1))]
                matrix[j][i] = f(left, right)

        return matrix

    def query(self, l, r):
        length = r - l + 1
        mx_2p = int(math.log2(length))
        left = self._table[mx_2p][l]
        right = self._table[mx_2p][r - (1 << mx_2p) + 1]
        return self._f(left, right)


class FenwickTreeNonIdempotent:


    '''
    This is a custom FenwickTree that I made :)  mostafa_alaa99
    '''

    def __init__(self, a, n, f, inv_f):
        self._n = n
        self._a = a
        self._f = f
        self._inv_f = inv_f
        self._fenwick_tree = self._construct_fenwick_tree(a, n, f, inv_f)

    def largest_2power_factor(k):
        return k & (-k)

    def _construct_fenwick_tree(self, a, n, f, inv_f):


        tree = [0] * n
        prx = []
        cur = 0
        for i in range(n):
            cur = f(cur, a[i])
            prx.append(cur)

        for i in range(n):
            length = FenwickTreeNonIdempotent.largest_2power_factor(i + 1)
            tree[i] = prx[i]
            start_interval = i - length + 1
            if start_interval > 0:
                tree[i] = inv_f(tree[i], prx[start_interval - 1])

        return tree

    def update(self, k, u):

        # All of them refer to the intervals that will be affected by this update

        prev = self._a[k]
        # First thing remove prev from all of them
        i = k
        while i < self._n:
            self._fenwick_tree[i] = self._inv_f(self._fenwick_tree[i], prev)
            i += FenwickTreeNonIdempotent.largest_2power_factor(i + 1)



        # Second thing add u to all of them
        i = k
        while i < self._n:
            self._fenwick_tree[i] = self._f(self._fenwick_tree[i], u)
            i += FenwickTreeNonIdempotent.largest_2power_factor(i + 1)

        self._a[k] = u

    def _query_helper(self, n):
        """
        Calculate the answer from 1 to n both inclusive
        """
        length = n + 1
        ans = 0
        i = 0
        while length > 0:
            max_p2 = int(math.log2(length))
            i += ((1 << max_p2) - 1)
            ans = self._f(ans, self._fenwick_tree[i])
            i += 1
            length -= (1 << max_p2)

        return ans

    def query(self, l, r): 
        ans = self._query_helper(r)
        if l > 0:
            ans = self._inv_f(ans, self._query_helper(l - 1))

        return ans


class SegmentTree:
    def __init__(self, arr, f):
        self._f = f
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)

        # Build the tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self._f(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        idx += self.n  # Move to leaf node
        self.tree[idx] = value  # Update value
        while idx > 1:
            idx //= 2
            self.tree[idx] = self._f(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, l, r):
        l += self.n  # Convert to leaf index
        r += self.n  # Convert to leaf index
        best = None

        while l <= r:
            if l % 2 == 1:  # If `l` is a right child
                if best == None:
                    best = self.tree[l]
                best = self._f(best, self.tree[l])
                l += 1
            if r % 2 == 0:  # If `r` is a left child
                if best == None:
                    best = self.tree[r]
                best = self._f(best, self.tree[r])
                r -= 1
            l //= 2
            r //= 2

        return best


def solve(file=False, infile=None, outfile=None):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    # n = read_int(infile=infile)
    # n = read_int(file=True, infile=infile)
    n, m = read_numbers(infile=infile)
    # s = read_str()
    # b = read_str()
    # t = input().strip()
    # pos = int(input())
    # n = len(s)
    # k = min(k, 12*n)
    # a = read_numbers()
    # b = read_numbers()
    # s = read_str()
    # b = read_str()
    # c = read_str()

    # a = read_numbers()

    # ------- Graph -------
    adj = [[] for _ in range(n+1)]
    # adj = defaultdict(list)
    for _ in range(m):
        u, v = list(map(int, input().split()))
        # u, v = arr[i - 2], i
        adj[u].append(v)
        adj[v].append(u)


    # ------- Weighted Graph ------
    # adj = [[] for _ in range(n+1)]
    # adj = defaultdict(list)
    # for _ in range(m):
    #     u, v, w = list(map(int, input().split()))
    #     # u, v = arr[i - 2], i
    #     adj[u].append((w, v))
    #     # adj[v].append((w, u))


    # s = read_str()


    # -------- Matrix -------
    # size = n
    # matrix = []
    # for _ in range(size):
    #     # row = read_numbers(infile=infile)
    #     row = read_str()
    #     # row = [0] * (size)
    #     matrix.append(row)


    # ------ Tree --------

    # adj = [[] for _ in range(n + 2)]
    # parents = [None] * (n + 2)
    # ans = [0] * (n + 2)
    # for node in range(2, n + 1):
    #     adj[node].append(a[node - 2])
    #     adj[a[node - 2]].append(node)
    #     parents[node] = a[node - 2]

    # Key Observations


    # Actions


    # Thinking



    vis = [0] * (n + 1)
    queue = deque()
    queue.append((1, 1))
    vis[1] = 1
    parents = [-1] * (n + 1)

    path = []
    found = False

    while queue:
        dist, node = queue.popleft()

        for ch in adj[node]:
            if not vis[ch]:
                vis[ch] = 1
                parents[ch] = node
                queue.append((dist + 1, ch))

                if ch == n:
                    found = True
                    break

        if found: break

    if found:
        cur = n
        while cur != -1:
            path.append(cur)
            cur = parents[cur]

        print(len(path))
        print(*path[::-1])
    else:
        print("IMPOSSIBLE")
















t = 1
# t = int(input())
for _ in range(t):
    solve()
#     # threading.Thread(target=solve).start()