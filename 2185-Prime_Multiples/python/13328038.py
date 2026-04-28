import sys
from collections import defaultdict, Counter

# 2*(a&b) + (a xor b) = a + b
# (a and b) xor (a or b) = a xor b

def prime_numiples(n: int, primes: int, k: int) -> None:
    s = 0
    for prime_subset in range(1, 1 << (k)):
        num = 1
        num_primes = 0
        sub = prime_subset
        for i in range(k):
            if sub & 1 == 1:
                num *= primes[i]
                num_primes += 1
            sub >>= 1

        s_num = n // (num)
        if num_primes % 2 == 0:
            s -= s_num
        else:
            s += s_num

    return s

if __name__ == "__main__": 
    stdin = sys.stdin

    n, k = list(map(int, stdin.readline().split()))

    a = list(map(int, stdin.readline().split()))

    stdout = sys.stdout

    res = prime_numiples(n, a, k)

    stdout.write(str(res) + '\n')
    stdout.flush()


"""
a = 2 7 11 13
s = 2
 s_1 = 2 + 7 - (2*7)
s_2 = 2 + 7 - (7*2) + 11 - (11*2) - (11*7)
s_3 = 2 + 7 - (7*2) + 11 - (11*2) - (11*7) + 17 - (17*2) - (17*7) - (17*11)
  take a number 2*7*11
 +: III
-: III
 incorrect, we have 0, when we should have 1
 say that we have
 s = 2 + 7 + 11 + ...
s = f(a_1) + f(a_2) + f(a_3) ...
 then, for a number
 - that's just k*a_1 , it's being counted correctly
- that's just a_i*a_j, \
    - double counted (a_i, a_j)
    - 0-subtracted: 0
    - sol: subtract a_i*a_j
- that's just a_i*a_j*a_k, it's
    - triple-counted (a_i, a_j, a_k)
    - triple-subtracted (a_i*a_j), (a_j*a_k), (a_i*a_k)
    - solution: add a_i*a_k*a_k
- that's just a_i*a_j*a_k*a_x
    - 8-counted (a_i, a_j, a_k, a_x), 4x(a_i, a_j, a_k)
    - 6-subtracted : ij ik ix jk jx kx
    - sol: subtract a_i*a_j*a_k*a_x
  idea, use PIE (inclusion exclusion)
  S(all items) = SUM_A( P(A) ) - SUM_A_B ( P(A & B) ) + SUM_A_B_C ( (P( A & B & C))) ... 
 so, given primes 2, 5, 11 ... 17
 S = (P(2) + P(5) + P(11) + P(17))
    - (P(2*5) + P(2*11) + P(2*17)...
        P(5*11) + P(5*17)...)
    + (P(2*5*11) + P(2*5*17) ... 
        P(5*11*17)...)
  idea: given k primes, I can use an binary integer a of k length, where if a_i=1,a_j=1, we are considering a number with both p_i and a_j
this is basically iterating through the subsets of primes
     """