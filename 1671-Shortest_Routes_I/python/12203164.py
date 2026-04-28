import sys
import heapq

settings = list(map(int, sys.stdin.readline().split()))
import time
#print(time.time())
num_cities = settings[0]
num_flights = settings[1]

flights = [[] for _ in range(num_cities)]
lowest_cost_parent = [None] * num_cities
lowest_cost_parent_cost = [None] * num_cities
visited = [False] * num_cities
# Read the roads input
for _ in range(num_flights):
 numbers = list(map(int, sys.stdin.readline().split()))

 flights[numbers[0] - 1].append((numbers[1] - 1, numbers[2]))

# for city in flights:
#  city.sort(key=lambda x: x[1])

heap = []

lowest_cost_parent_cost[0] = 0

heapq.heappush(heap, (0, 0))

#print(time.time())

i = 0 



while heap:
 cost, city = heapq.heappop(heap)

 if visited[city]:
  continue

 visited[city] = True

 for neighbor, connection_cost in flights[city]:
  ncost = cost + connection_cost
  i+=1
  if (a := lowest_cost_parent_cost[neighbor]) is None or a > ncost:
   lowest_cost_parent_cost[neighbor] = ncost
   heapq.heappush(heap, (ncost, neighbor))

print(' '.join([str(cost) for cost in lowest_cost_parent_cost]))