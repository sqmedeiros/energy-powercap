# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 23:16:57 2022
 @author: Mohamed Ayman
"""

"""
#Weird Algorithm
 n = int(input())
print(n , end = " ")
 while n != 1:
    if n%2 == 0:
        n //= 2
        print(n , end = " ")
    else:
        n = n*3 + 1
        print(n , end = " ")
                #Missing Number
n = int(input())
numbers = set([int(i) for i in input().split()])
missingNumber = {i for i in range(1 ,n+1 ,1)} - numbers
print(*missingNumber) 
 #better solution
n = int(input())
numbers = set([int(i) for i in input().split()])
trueSum , missingSum = (n*(n+1)) // 2 , 0
for number in numbers:
    missingNumber += number
print(trueSum - missingSum)
 #Repetitions
sequence = input()
pointer = sequence[0]
counts = []
counter = 0
for letter in sequence:
    if letter == pointer:
        counter += 1
    else:
        pointer = letter 
        counts.append(counter)
        counter = 1
else:
    counts.append(counter)
print(max(counts))
 #Increasing Array
n = int(input())
numbers = [int(i) for i in input().split()]
moves = 0
 for i in range(n-1):
    diff = numbers[i] - numbers[i+1]
    if diff > 0:
        moves += diff
        numbers[i+1] = numbers[i]
    else:
        continue
print(moves)
 #Permutations
n = int(input())
if 1< n < 4 :
    print("NO SOLUTION")
else:
    print(*(list(range(2 , n+1 , 2))+list(range(1 , n+1 , 2))))
 #Number Spiral
for _ in range(int(input())):
    y , x = [int(i) for i in input().split()]
    number = 0
    if y >= x:
        if y%2 != 0:
            number = (y-1)*(y-1) + 1 + (x - 1)
        else:
            number = y*y - (x-1)
    else:
        if x%2 == 0:
            number = (x-1)*(x-1) + 1 + (y-1) 
        else:
            number = x*x - (y-1)
    print(number)
    #Two Knights
 for i in range(1,1+int(input()),1):
    print(((i * i * (i*i - 1) ) // 2) - 4 * (i - 2) * (i - 1) )
 #Dice Combinations
n = int(input())
ways = [0] * (n+1)
m = int(1e9 + 7)
ways[0] = 1
for i in range(n+1):
    for j in range(1 , min(n+1 , 7) , 1):
        ways[i] += ways[i - j]
        ways[i] %= m   
 print(ways[n]) 
 #Minimizing Coins
n , money = [int(i) for i in input().split()]
coins = [int(i) for i in input().split()]
 minNumber = [10000000]* (money+1)
 for i in range( 1 , money+1 , 1):
    for j in coins:
        if i - j >= 0 :
            minNumber[i] = min(minNumber[i] , minNumber[i - j ] + 1)
        else: break
 if minNumber[money] == 10000000:
    print(-1)
else: 
    print(minNumber[money])    
 #Removing Digits
n = int(input())
counter = 0
 def maxDigit(n):
    digits = []
    while n != 0:
        digit = n % 10
        digits.append(digit)
        n -= digit
        n //= 10
    return max(digits)
 while n != 0:
    n -= maxDigit(n)
    counter += 1
 print(counter)
 #Grid Paths
n = int(input())
grid = [input() for i in range(n)]
m = int(1e9 + 7)
ways = [[0 for i in range(n)] for j in range(n)]
ways[0][0] = 1
 for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == '*':
            ways[i][j] = 0
        else:
            if i - 1 >= 0 :  
                ways[i][j] += ways[i-1][j]
                ways[i][j] %= m
            if j - 1 >= 0 :  
                ways[i][j] += ways[i][j-1]
                ways[i][j] %= m
            print(ways[n-1][n-1])
 #Two Sets
n = int(input())
numbers = [i for i in range(1,n+1)]
s1 = []
s2 = []
 if (n+1) % 4 == 0:
    print("YES")
    for i in range(1, n+1 , 4):
        s1.append(numbers[i - 1])
        s1.append(numbers[i])
    for i in range(3, n+1 , 4):
        s2.append(numbers[i - 1])
        try:
            s2.append(numbers[i])
        except:
            pass
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)
elif n % 4 == 0:
    print("YES")
    for i in range(2, n+1 , 4):
        s2.append(numbers[i - 1])
        try:
            s2.append(numbers[i])
        except:
            pass
    print(len(s2))
    print(*(set(numbers) - set(s2)))
    print(len(s2))
    print(*s2)
else:
    print("NO")
    #Book Shop
n , money = [int(i) for i in input().split()]
bookPrices = [int(i) for i in input().split()]
bookPages = [ int(i) for i in input().split()]
pages = [0] * (money+1)
used = [[]]
  for cost in range(1 , money+1):
    booksUsed = []
    for i in range(n) :
        if cost - bookPrices[i] >= 0 and i not in used[cost-bookPrices[i]] : 
            if pages[cost] < (pages[cost - bookPrices[i] ]  + bookPages[i]):
                booksUsed = used[cost - bookPrices[i]] + [i]
                            pages[cost] = max(pages[cost] , pages[cost - bookPrices[i]] + bookPages[i])
                used.append(booksUsed)
 print(pages[money])        
     #Array Description
big = int(1e9 + 7)
n , m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
network = []
ways = [[0 for i in range(m)] for i in range(n)]
i = 0
 for number in arr:
    if number == 0:
        network.append([i for i in range(1 , m + 1)])
    else:
        network.append([number])
  for level in network:
    for value in level:
        if i == 0:
            ways[i][value - 1] = 1
        else:
            if value < m :
                ways[i][value - 1] += ways[i-1][value]
            if value - 2 >= 0:
                ways[i][value - 1] += ways[i-1][value - 2]
            ways[i][value - 1] += ways[i-1][value-1]
            ways[i][value-1] %= big
    i += 1
 print(sum(ways[i- 1]) % big)
 #Counting Rooms
n , m = [int(i) for i in input().split() ]
info = [input() for i in range(n)]
movements = [(1,0) , (-1,0) , (0 , 1) , (0 , -1) ]
visited = [[False for i in range(m)] for i in range(n)]
queue = [(info[0][0] , 0 , 0)]
rooms = 0
 def bfs(row , col):
    queue = [(info[row][col] , row , col)]
    while queue != []:
        node = queue.pop()
        for drow , dcol in movements:
            rowf = node[1] + drow
            colf = node[2] + dcol
            if 0 <= rowf < n and 0 <= colf < m:
                if info[rowf][colf] == '.':
                    if visited[rowf][colf]:
                        continue
                    queue.append((info[rowf][colf] , rowf , colf))
                    visited[rowf][colf] = True
                        return 1
 for i in range(n):
    for j in range(m):
        if info[i][j] == '.' and not visited[i][j]:
            rooms += bfs(i , j)
 print(rooms)
 #Josephus Problem I
n = int(input())
numbers = [i for i in range(1,n+1)]
while True:
    if len(numbers) == 1:break
    afterRemoved = []
    removed = []
    for j in range(len(numbers)//2):
        afterRemoved.append(numbers[2*j])
        removed.append(numbers[2*j+1])
    if len(numbers) & 1:
        afterRemoved = [numbers[-1] , *afterRemoved]
    numbers = afterRemoved
    print(*removed , end = " ")
 print(numbers[0])
 #Josephus Queries
  def f(n , k):
    if n == 1: return 1
    if k <= (n+1)//2: 
        if 2*k > n: return (2*k)%n
        else: return 2*k
    sub = f(n//2 , k -((n+1)//2))
    if n & 1: return 2*sub + 1
    else: return 2*sub - 1
 for _ in range(int(input())):
    n , k = [int(i) for i in input().split()]
    print(f(n,k))
        #Building Roads
cities , roads = [int(i) for i in input().split()]
visited = [False] * cities
connections = [[int(i) for i in input().split()] for j in range(roads)]
network = [[] for i in range(cities) ] 
nodes = []
 for connection in connections:
    network[connection[0] - 1 ].append(connection[1])
    network[connection[1] - 1].append(connection[0])
 def dfs(city):
    if visited[city-1]: return
    visited[city-1] = True
    for node in network[city-1]:
        if not visited[node-1]:
            dfs(node)
            for i in range(1 , cities+1):
    if not visited[i-1]:
        nodes.append(i)
        dfs(i)
        print(len(nodes) - 1)      
for i in range(len(nodes)-1):
    print(nodes[i] , nodes[i+1])
     #Exponentiation
 m = int(1e9 + 7)
 def calPow(a,b):
    if b == 0: return 1
    if b & 1:
        return (a * calPow(a, b-1)) % m
    else:
        x = calPow(a, b//2)
        return (x * x) % m
 for _ in range(int(input())):
    a , b = [int(i) for i in input().split()]
    print(calPow(a,b))
""" 
#Prime Multiples
n , k = [int(i) for i in input().split()]
primes = [int(i) for i in input().split()]
nDivisiors = [0] *(k+1)
ans =0

for mask in range(1,1<<k):
    divisors = 0
    temp = n
    for i in range(k):
        if (1<<i) & mask:
            divisors += 1
            temp //= primes[i]

    nDivisiors[divisors] += temp

for i in range(1 , k+1):
    if 1 & i:
        ans += nDivisiors[i]
    else:
        ans -= nDivisiors[i]


print(ans)













