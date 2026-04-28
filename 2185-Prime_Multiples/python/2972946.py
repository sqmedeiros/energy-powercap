"""
You are given k distinct prime numbers a1,a2,…,ak and an integer n.
 Your task is to calculate how many of the first n positive integers are divisible by at least one of the given prime numbers.
 Input
 The first input line has two integers n and k.
 The second line has k prime numbers a1,a2,…,ak.
 Output
 Print one integer: the number integers within the interval 1,2,…,n that are divisible by at least one of the prime numbers.
 Constraints
1≤n≤1018
1≤k≤20
2≤a_i≤n
 Input:
20 2
2 5
 Output:
12
 """

import itertools

s = input("").split()
n = int(s[0])
s = input("").split()
primes = [int(i) for i in s]

result = 0

# n ~ 10^18
# len(primes) ~ 20
# Optimize for n
"""
# Naive version
 for i in range(1,n+1):
 for j in primes:
  if i % j == 0:
   result += 1
   break
"""

# https://fr.wikiversity.org/wiki/Formule_du_crible/D%C3%A9finition
# On implémente la formule du crible pour calculer la taille de l'union de k ensembles.

result = 0

for k in range(1,len(primes)+1):
 current = 0
 # add numbers from p to floor(n/p) * p 
 for iks in itertools.combinations(primes,k):
  # card(intersect iks)
  m = 1
  for ik in iks:
   m *= ik
  current += n // m
 result += ((-1) ** (k+1)) * current
# Remove duplicates: multiples of p_i and p_j for example:


print(result)