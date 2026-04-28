# Author :  //- kibrom Hailu -\\

import dis
import sys
# from collections import Counter, defaultdict, deque
# from math import ceil, floor, gcd, inf, sqrt
# from itertools import permutations, combinations, accumulate
# from bisect import bisect_left, bisect_right
# from heapq imortt heapify , heappop , heappush , heappushpop , heapreplace 

def SI():return sys.stdin.readline().rstrip()
def I():return int(SI())
def M():return map(int, SI().split())
def IL():return list(map(int, SI().split()))
def F():return float(SI())
def FL():return list(map(float, SI().split()))

global big
big = int(1e18)

def main():

    n,m,q = M()
    dist = [[big for i in range(n)] for j in range(n)]

    for _ in range(m):
        a , b, c = M() 
        a -= 1 
        b -= 1
        if c < dist[a][b]:
            dist[a][b] = c 
            dist[b][a] = c

    # floyd - warshall 
    for k in range(n):
        for i in range(n):
            for j in range(i+1,n):
               new_dist = dist[i][k] + dist[k][j]
               if new_dist < dist[i][j]:
                   dist[i][j] = dist[j][i] = new_dist 

    for _ in range(q):
        a,b  = M() 
        a -= 1
        b -= 1

        if a == b:
            dist[a][b] = 0 
        elif dist[a][b] == big :
            dist[a][b] = -1 

        print(dist[a][b])













if __name__ == "__main__":
    main()