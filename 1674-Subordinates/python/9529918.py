#JAI MATA DI
##### binary and decimal #####
#  way to convert number to binary ------->  bin(Number)[2:] 
# way to convert binary to number ------->  int(n,2)
#########################
#to get permutations of a string
from itertools import permutations
def allPermutations(str):
    permList = permutations(str)
    return permList
#######################
# TO GET FlCTORS OF l NUMBER:
def factors(x):
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x//i != i: 
                result.append(x//i)
        i += 1
    return result
#####################################
def fast_expo(val, power):
    result = pow(val, power//2)
    result = result * result

    if power % 2 != 0:
        result = result * val
    return result
######################################
# xeck if prime or not
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
########################################
def transpose(l1, l2):

    for i in range(len(l1[0])):
        # print(i)
        row =[]
        for item in l1:

            row.append(item[i])
        l2.append(row)
    return l2

######################################
def primeFactor(x):
    l=[]
    while x%2==0:
        l.append(2)
        x=x//2
    for i in range(3,int(math.sqrt(x)+1),2):
        while x%i==0:
            l.append(i)
            x=x/i
    if x>2:
        l.append(x)
    return l
################################################
from math import gcd as bltin_gcd

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

#####################################################

#   Sieve of Eratosthenes to precompute primes up to a certain limit,
# and then check if a number is prime using the precomputed list.

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes
#################################################################################
# MEX FINDER
def find_mex(arr):
    return min(set(range(len(arr) + 1)) - set(arr))

################################################################################
# KADANES ALGORITHM
# helps to find the subarray with the largest sum

def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        curSum = max(curSum, 0)
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

################################################################################

# ONE COUNTER IN BINARY REPRESENTATION

def count_ones(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

###########################################################################



################################################################################
## IMPORTSSS ##

import math
from collections import *
from itertools import groupby
import heapq

from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

##NOTES NOTES NOTES NOTES NOTES!!!!!!
##
# 1) To find maximum element and its index efficiently use heapq like this========>
#          max_heap = [(-value, index) for index, value in enumerate(arr)]
#          heapq.heapify(max_heap) 
#          val, a = heapq.heappop(max_heap)


#  2) if you see a question that invovle parentheses checking pattern use STACKS.

# 3) if question gives cost of something and ask max number kitne le skte ya bna skte
#    like hamburger ques or magic powder  use BINARY SEARCH

# 4) GOLDEN RATIO
#     int(round((golden_ratio ** n)/ 5 ** 0.5))
# gives any particular element of fibonacci series



 ################################################################################
def range_subset(range1, range2):
    """Whether range1 is a subset of range2."""
    if not range1:
        return True  # empty range is subset of anything
    if not range2:
        return False  # non-empty range can't be subset of empty range
    if len(range1) > 1 and range1.step % range2.step:
        return False  # must have a single value or integer multiple step
    return range1.start in range2 and range1[-1] in range2

#>>> range_subset(range(0, 1), range(0, 4))
#################################################################################################################

n = int(input())
arr = list(map(int, input().split()))


tree = {i: [] for i in range(1, n + 1)}
for x in range(n - 1):
    tree[arr[x]].append(x + 2)


ans = [0] * (n + 1)


stack = [(1, 0)]

count_stack = []

while stack:
    node, visit = stack.pop()
    if visit == 0: 
        stack.append((node, 1))  
        count_stack.append(node)
        for sub in tree[node]:
            stack.append((sub, 0))
    else:  
        count = 0
        for sub in tree[node]:
            count += 1 + ans[sub]
        ans[node] = count


print(*ans[1:])

