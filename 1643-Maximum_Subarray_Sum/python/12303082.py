#!/usr/bin/env python3

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
# Standard library imports
import sys
import os
# import math

# # Data structure imports
# import heapq
# from collections import (
#     defaultdict,
#     Counter,
#     deque
# )

# Type hints
from typing import (
    List, Set, Dict, Tuple,
    Optional, Union, Any
)

# # Itertools
# from itertools import (
#     permutations,
#     combinations
# )

#------------------------------------------------------------------------------
# Constants
#------------------------------------------------------------------------------
# inf = float('inf')
# mod = 1000000007


#------------------------------------------------------------------------------
# Debug Helper
#------------------------------------------------------------------------------
DEBUG = os.getenv("DEBUG", "0") == "1"

def debug(*args, **kwargs):
    if DEBUG:
        with open("io_files/debug.txt", 'w') as debug_file:
            print(*args, file=debug_file, **kwargs)

#------------------------------------------------------------------------------
# Helper Functions
#------------------------------------------------------------------------------

def sieve(n: int) -> List[int]:
    """
    Optimized Sieve of Eratosthenes to find all prime numbers up to n.
    """
    if n < 2:
        return []

    # Boolean array to track prime status
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # Mark even numbers (except 2) as non-prime
    for i in range(4, n + 1, 2):
        is_prime[i] = False

    # Process only odd numbers from 3 onwards
    for i in range(3, int(n ** 0.5) + 1, 2):
        if is_prime[i]:
            # Start marking from i^2, increment by 2*i (to skip even multiples)
            for j in range(i * i, n + 1, 2 * i):
                is_prime[j] = False

    # Collect primes
    primes = [2] if n >= 2 else []
    primes.extend(i for i in range(3, n + 1, 2) if is_prime[i])

    return primes

#------------------------------------------------------------------------------
# Solution
#------------------------------------------------------------------------------
def solution() -> Union[List[int], int, str]:
    # Write your solution here
    n = int(input())
    arr = list(map(int, input().split()))
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
def main() -> None:
    t = 1
    # t = int(input())
    for _ in range(t):
        result = solution()
        if isinstance(result, (list, tuple, set)):
            sys.stdout.write(' '.join(map(str, result)) + '\n')
        else:
            sys.stdout.write(str(result) + '\n')
        sys.stdout.flush()

if __name__ == "__main__":
    # Local mode 
    if DEBUG:
        sys.stdin = open("io_files/input.txt", "r")
        sys.stdout = open("io_files/output.txt", "w")

    main()