# from queue import PriorityQueue

# N, E = [int(i) for i in input().split()]
# # (distance, node) tutar
# adj = [[] for i in range(N+1)]
# for i in range(E):
#     a,b, d = [int(i) for i in input().split()]
#     adj[a].append((d, b))

#     #ONE WAY TICKET
#     adj[b].append((d, a))

# # Graphimi oluşturdum

# INF = 10**15
# # Sıfırdan diğer noktalara olan uzaklık
# distance = [INF for i in range(N + 1)]

# # Tuplelar tutacak, (distance, node)
# pq = PriorityQueue()
# pq.put((0, 1))
# distance[1] = 0

# q_size = 1
# while (q_size > 0):

#     # Tuple (distance, node)
#     curr = pq.get()
#     q_size -= 1

#     # curr[0] : şu an incelediğim path ne kadar uzun
#     # distance[curr[1]] : şu ana kadar bulduğum en kısa path
#     if (curr[0] > distance[curr[1]]):
#         continue



#     # adjleri queue'ya ekle
#     for a in adj[curr[1]]:
#         if (distance[a[1]] > curr[0] + a[0]): # unutmuştum
#             pq.put( (curr[0] + a[0], a[1] ) )
#             distance[a[1]] = curr[0] + a[0]
#             q_size += 1


# for i in range(1,N+1):
#     print(distance[i], end=" ")



from queue import PriorityQueue

N, E = [int(i) for i in input().split()]
# (distance, node) tutar
adj = [[] for i in range(N+1)]
for i in range(E):
    a,b, d_ = [int(i) for i in input().split()]
    adj[a].append((d_, b))

    #if it's a ONE WAY TICKET comment this line
    # adj[b].append((d_, a))

# Graphimi oluşturdum



INF = 10**17
# S'ten diğer noktalara olan uzaklık
distance1 = [INF for i in range(N + 1)]

# Tuplelar tutacak, (distance, node)
pq1 = PriorityQueue()
pq1.put((0, 1))
distance1[1] = 0


q_size = 1
while (q_size > 0):

    # Tuple (distance, node)
    curr = pq1.get()
    q_size -= 1

    # curr[0] : şu an incelediğim path ne kadar uzun
    # distance[curr[1]] : şu ana kadar bulduğum en kısa path
    if (curr[0] > distance1[curr[1]]):
        continue



    # adjleri queue'ya ekle
    for a in adj[curr[1]]:
        if (distance1[a[1]] > curr[0] + a[0]): # unutmuştum
            distance1[a[1]] = curr[0] + a[0]
            pq1.put( (curr[0] + a[0], a[1] ) )
            q_size += 1


for i in range(1,N+1):
    print(distance1[i])