from sys import stdin
#import mnamn weff
n, x = map(int, stdin.readline().strip().split()) #no funtion definition for input
coin = list(map(int, stdin.readline().strip().split()))
mod = 10 ** 9 + 7 #this also changed something
memo = [0 for _ in range(x + 1)] #this changed something(list comprehention)

memo[0] = 1
for idx in range(n - 1, -1, -1):
    for change in range(coin[idx], x + 1):
        #starting from coin[idx] helped too
        memo[change] += memo[change - coin[idx]]
        memo[change] %= mod

print(memo[x])

