############################################## Libraries ###########################################################

import sys
from math import gcd,ceil,log
from queue import PriorityQueue
from bisect import bisect_left

############################################## Definitions #########################################################

mod = pow(10,9)+7
e = pow(10,-6)
input = lambda: sys.stdin.readline().rstrip("\r\n")
N = pow(10,6)

# sys.setrecursionlimit(10**6)

############################################## Input forms #########################################################

def imap(): # Multiple numbers input
    return map(int,input().split())

def ilist(): # List input 
    return list(map(int,input().split()))

def ilgraph(n,m): # Graph input as Adjacency List

    l = [[]for i in range(n+1)]
    for i in range(m):
        x,y = imap()
        l[x].append(y)
        l[y].append(x)
    return l

def iagraph(n,m): # Graph input as Adjacency Matrix
    l = [[0 for i in range(n+1)]for i in range(n+1)]
    for i in range(m):
        x,y = imap()
        l[x][y] = 1
        l[y][x] = 1
    return l

############################################## Data Structures #######################################################

class SegmentTree: # //O(logn) for operations and O(n) for building//

    def init(arr): # n shld be a power of 2...hence add extra zeros before itself if needed //O(n)//
        n = len(arr)
        tree = [0]*(2*n) 
        for i in range(n):
            tree[n+i] = arr[i] # The actual array is between indices n to 2*n-1 the first nodes store sums

        for i in range(n-1,-1,-1):
            tree[i] = tree[i<<1]+tree[(i<<1) | 1] # parent node value  = child node's sum i<<1 = 2*i, i<<1 |1 = 2*i+1
        return tree

    def add(tree,i,v): # Sets vertex i to value v (i shld be 0 based indexing) //O(logn)//
        i += len(tree)//2 # As the actual array is between n and 2*n-1, we add n to i (n = len(tree)//2)
        tree[i] = v
        while i>1:
            tree[i>>1] = tree[i]+tree[i^1] 
            i >>=1
            # Calculating the values of prev nodes. (eg if node 9 is changed 9>>1 = 4 takes values of node i(9) and node i^1(8))

    def range_sum(tree,l, r): # calculates the sum of values in the range [l,r-1] (l and r take 0 based indexing) //O(logn)//
        l += len(tree)//2
        r += len(tree)//2
        sum = 0
        while l<r: 
            if l&1:
                sum += tree[l] # If the index is odd, add its value to sum. if the index is even it means there would be a parent 
                l += 1         # of this with odd index
            if r&1:
                r -= 1
                sum += tree[r]
            l >>= 1
            r >>= 1
        return sum

############################################# Common functions #######################################################

def freq(l): # Returns count of a number in a list/string // O(nlog(n)) //
    d = {}
    for i in l:
        d[i] = d.get(i,0)+1
    return d

def prefix_sum_2d(l): #Returns the 2d prefix sum array of size (n+1)*(m+1) with 0 padded on first row and first col for easy calc.
    n = len(l)
    m = len(l[0])
    p = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,m+1):
            p[i][j] = p[i-1][j]+p[i][j-1]+l[i-1][j-1]-p[i-1][j-1]
    return p  

    # //O(nm)//

############################################### Number Theory #########################################################

def is_pow2(x): #Checks if a number is a power of 2 // O(1) //
    return max(1-(x&(x-1)),0)

def lgcd(l): # Returns gcd of a list // O(nlog(n)) //
    a = 0
    for i in l:
        a = gcd(a,i)
    return a

def SieveOfEratosthenes(num): # Returns an array with Prime numbers upto num // O(nlog(log(n))) //
    prime = [True for i in range(num+1)]
    Highest_Prime = [0 for i in range(num+1)] # Returns an array with the highest prime factor of each i between 0 and Num 
    Lowest_Prime = [0 for i in range(num+1)] # Returns an array with the lowest prime factor of each i between 0 and Num
    prime[0] = prime[1] = False
    p = 2
    while (p <= num):
        if (prime[p] == True):
            Lowest_Prime[p] = p
            Highest_Prime[p] = p
            for i in range(2*p, num+1, p):
                prime[i] = False
                Highest_Prime[i] = p
                if Lowest_Prime[i] == 0:
                    Lowest_Prime[i] = p
        p += 1
    # print(prime,'\n',Highest_Prime,'\n',Lowest_Prime)         #Checker
    # return Lowest_Prime #An array containing the lowest prime factors of all numbers till num

    # return Highest_Prime # An array containing the highest prime factors of all numbers till num

    # return prime # An array with boolean values indicating if the number is prime/not prime
    p = []
    for i in range(num+1):
        if prime[i]:
            p.append(i)
    return p # An array with just prime numbers till the given number

def PrimeFactors(num,Prime_array):# Returns a dictionary with prime factors mapped with their respective powers // O(nlogn) //

    # COmplexity is O(logn) for this code, but this requires that u have a Prime array which could be highest or lowest prime which can be calculated from the prev Sieve of Erastothenes) hence over complexity is O(nlogn)

    d = {}
    while num != 1: 
        x = Prime_array[num]
        d[x] = d.get(x,0)+1
        num//=x
    return d

def facotrization(n):  #returns a dict with prime factors and their powers for a given number in // O(sqrt(n)) // 
    #Use this approach if you don't have a prime array

    d = {}
    x = 2
    while x*x<=n:
        while n%x == 0:
            d[x] = d.get(x,0)+1
            n//=x
        x += 1
    if n>1:
        d[n] = d.get(n,0)+1
    return d

def ETF(d):
    #d is the dict contaiing prime factors
    s = 0
    for i in d:
        s += pow(i,d[i]-1)*(i-1)
    return s

################################################## Combinatorics ############################################################

def fact(n,mod):  #Returns the factorial of all numvers from 1 to  n % mod
    f = [1]
    for i in range(1,n+1):
        f.append((f[i-1]*i%mod)%mod)
    return f

def dearrange(n,mod): #Returns an array containing the dearragements of all numbers from 1 to n % mod
    if mod == -1:
        dearr = [1,0]
        for i in range(2,n+1):
            dearr.append((i-1)*(dearr[i-1]+dearr[i-2]))
    else:
        dearr = [1,0]
        for i in range(2,n+1):
            dearr.append(((i-1)%mod*(dearr[i-1]+dearr[i-2])%mod)%mod)
    return dearr

################################################ Binary Arithmetic ##########################################################

def bin_search(p,x): #Returns -1 if the element doesn't exist in the list and its index if it does. //O(logn)//
    i = bisect_left(p, x)
    if i != len(p) and p[i] == x:
        return i
    else:
        return -1

def bin_left(p,x): #Returns the index of max element less than x and -1 if all elements r greater than x // O(logn) //
    n = len(p)
    l,r = 0,n-1
    if p[0]>x:
        return -1
    while l<=r:
        mid = (l+r)//2
        if p[mid] <= x:
            if mid != n-1:
                if p[mid+1]>x:
                    break
                else:
                    l = mid+1
            else:
                mid = n-1
                break
        else:
            r = mid-1
    return mid

def bin_right(p,x): #Returns the index of min element greater than x and n if all elements r less than x // O(logn) //
    n = len(p)
    l,r = 0,n-1
    if p[-1]<x:
        return n

    while l<=r:
        mid = (l+r)//2
        if p[mid] >= x:
            if mid != 0:
                if p[mid-1]<x:
                    break
                else:
                    r = mid-1
            else:
                mid = 0
                break
        else:
            l = mid+1
    return mid

def bin_sqrt(x): # Returns floor of sqrt // O(logx) //
    if x == 0 or x == 1:
        return x
    l = 1
    r = x
    while l<=r:
        mid = (l+r)/2
        y = mid*mid
        if y>x:
            r = mid-1
        elif y == x:
            return mid
        else:
            if ((mid+1)*(mid+1))>x:
                return mid
            else:
                l = mid+1

def bin_exp(a,b,mod): #Returns (a^b) mod m where 0 <= a,b <= 10^18 // O(log(b)) //
    ans = 1
    a %= mod
    while b:
        if b&1:
            ans = (ans*a)% mod
        a = (a*a)%mod
        b >>= 1
    return ans
############################################################ DP #############################################################

def lcs(a, b): # Returns the longest common subsequence of two strings in //O(n^2)//
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    i,j = len(a),len(b)
    l = []
    while i!=0 and j!=0:
        if dp[i][j] == dp[i][j-1]:
            j-=1
        elif dp[i][j] == dp[i-1][j]:
            i-=1
        else:
            i-=1
            j-=1
            l.append(a[i])
    s = ''.join(l)
    # return len(s) 
    return s[::-1]

def lis(arr): # Returns the length of longest increasing subsequence in an array of intigers/characters. // O(nlogn) //
    l = []
    for i in arr:
        pos = bisect_left(l,i)
        if pos == len(l): 
            l.append(i) # we can have a new, longer increasing subsequence!
        else:
            l[pos] = i # At least we can make the ending element smaller
    return len(l)

######################################################## Graph Algos ########################################################

def dfs(adj,s,visited):
    stack = []
    stack.append(s)

    while (len(stack)):
        s = stack.pop()

        if (not visited[s]):
            # print(s,end=' ')
            visited[s] = True

        for node in adj[s]:
            if (not visited[node]):
                stack.append(node)

######################################################## Starting off #######################################################

n,m = imap()
l = []
adj = ilgraph(n,m)
# print(adj)
visited = [False for i in range(n+1)]

for i in range(1,n+1):
    if visited[i] == False:
        l.append(i)
        dfs(adj,i,visited)

print(len(l)-1)
for i in range(len(l)-1):
    print(l[i],l[i+1])





########################################################## By Shri ##########################################################