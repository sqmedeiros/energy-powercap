import sys 
input = sys.stdin.readline
#print = sys.stdout.write
'''
def is_intersecting(x1, y1, x2, y2):
    return not (y1 < x2 or x1 > y2)
 class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
     def area(self):
        return (self.y2 - self.y1) * (self.x2 - self.x1)
     def get_overlap_rectangle(self, other):
        x_overlap = max(0, min(self.x2, other.x2) - max(self.x1, other.x1))
        y_overlap = max(0, min(self.y2, other.y2) - max(self.y1, other.y1))
         if x_overlap == 0 or y_overlap == 0:
            # No overlap, return None
            return Rect(0,0,0,0)
         overlap_x1 = max(self.x1, other.x1)
        overlap_y1 = max(self.y1, other.y1)
        overlap_x2 = min(self.x2, other.x2)
        overlap_y2 = min(self.y2, other.y2)
         return Rect(overlap_x1, overlap_y1, overlap_x2, overlap_y2)
'''
'''
a << n = a x 2**n 
a >> n = gif(a/2**n)
'''

'''
def highest_exponent(x, y):
    if x <= 0 or y <= 0:
        return "Both x and y must be positive integers."
     exponent = 0
     while x % (y ** (exponent + 1)) == 0:
        exponent += 1
     return exponent
 def highest_exponent_less_than(x, y):
    if x <= 0 or y <= 0:
        return "Both x and y must be positive integers."
     exponent = 0
     while x >= y**exponent:
        exponent += 1
     return exponent
  def index_in_sorted_array(arr):
    # Create a list of tuples where each tuple contains the original element and its index
    indexed_array = list(enumerate(arr))
        # Sort the list of tuples based on the second element (the actual value)
    sorted_array = sorted(indexed_array, key=lambda x: x[1])
        # Extract the indices from the sorted array
    sorted_indices = [index for index, _ in sorted_array]
        return sorted_indices
     def generate_permutations(prefix,suffix):
    if len(suffix) == 0:
        permutations.add(prefix)
        return 
    else:
        for i in range(len(suffix)):
            generate_permutations(prefix + suffix[i],suffix[:i] + suffix[i+1:])   
 def maxSubArraySum(a, size):
    max_so_far = float('-inf')
    max_ending_here = 0
     for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
         if max_ending_here < 0:
            max_ending_here = 0
     return max_so_far
   from functools import reduce
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
 '''
'''
def find_largest_less_than_key(sorted_list, key):
    low, high = 0, len(sorted_list) - 1
    result_index = -1  # Initialize result_index to -1 in case there is no such element
     while low <= high:
        mid = (low + high) // 2
         if sorted_list[mid] < key:
            result_index = mid
            low = mid + 1
        else:
            high = mid - 1
     return result_index
'''
def index_in_sorted_array(arr):
    # Create a list of tuples where each tuple contains the original element and its index
    indexed_array = list(enumerate(arr))

    # Sort the list of tuples based on the second element (the actual value)
    sorted_array = sorted(indexed_array, key=lambda x: x[1])

    # Extract the indices from the sorted array
    sorted_indices = [index for index, _ in sorted_array]

    return sorted_indices

n,x = map(int,input().split())
l = [int(x) for x in input().split()]
l1 = index_in_sorted_array(l)

l.sort()

p = 0
q = n-1
flag = 0
while p < q:
    if l[p] + l[q] > x:
        q = q -1 
    elif l[p] + l[q] < x:
        p = p + 1
    else:
        flag = 1
        break 

if flag == 0:
    print('IMPOSSIBLE')
else:
    print(l1[p] + 1,l1[q] + 1)





























