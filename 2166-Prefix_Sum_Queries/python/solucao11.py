# Given an array of n integers, your task is to process q queries of the following types:
 
# update the value at position k to u
# what is the maximum prefix sum in range [a,b]?
 
# Empty prefixes (with sum 0) are allowed.
# Input
# The first input line has two integers n and q: the number of values and queries.
# The second line has n integers x_1,x_2,\dots,x_n: the array values.
# Finally, there are q lines describing the queries. Each line has three integers: either "1 k u" or "2 a b".
 
 
# Output
# Print the result of each query of type 2.
 
import sys
input = sys.stdin.readline
 
# Tupla: (sum, max_prefix)
def combine(left, right):
    total_sum = left[0] + right[0]
    max_prefix = max(left[1], left[0] + right[1])
    return (total_sum, max_prefix)
 
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [(0, 0)] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = (data[i], max(0, data[i]))
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = combine(self.tree[i << 1], self.tree[i << 1 | 1])
 
    def query(self, L, R):
        L += self.n
        R += self.n
        left_node = (0, 0)
        right_node = (0, 0)
        
        while L <= R:
            if L & 1:
                left_node = combine(left_node, self.tree[L])
                L += 1
            if not (R & 1):
                right_node = combine(self.tree[R], right_node)
                R -= 1
            L >>= 1
            R >>= 1
        
        result = combine(left_node, right_node)
        return result[1]
    
    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = (value, max(0, value))
        while pos > 1:
            pos >>= 1
            self.tree[pos] = combine(self.tree[pos << 1], self.tree[pos << 1 | 1])
 
n, q = map(int, input().split())
data = list(map(int, input().split()))
seg_tree = SegmentTree(data)
results = []
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, k, u = query
        seg_tree.update(k - 1, u)
    else:
        _, a, b = query
        results.append(str(seg_tree.query(a - 1, b - 1)))
 
print('\n'.join(results))