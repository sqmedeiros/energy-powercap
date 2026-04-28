from queue import PriorityQueue

def djikstra(num_cities):
    result = [-1 for i in range(num_cities + 1)]
    visited = [False for _ in range(num_cities + 1)]
    q = PriorityQueue()
    q.put((0, 1)) # 0 = cost, 1 = node
    while (q.qsize() != 0):
        v = q.get()
        cost = v[0]
        row = v[1]
        if (visited[row]):
            continue
        result[row] = cost
        visited[row] = True
        for dest in adj_list[row]:
            if (result[dest[0]] == -1):
                q.put((cost + dest[1], dest[0]))
    result.pop(0)
    return result


line = input().split()
num_cities, num_connections = int(line[0]), int(line[1])
lines = []
for i in range(num_connections):
    lines.append(input())
#matrix = [[0 for i in range(num_cities + 1)] for j in range(num_cities + 1)]
adj_list = [[] for j in range(num_cities + 1)]
for line in lines:
    flight = line.split()
    origin = int(flight[0])
    dest = int(flight[1])
    length = int(flight[2])
    temp = True
    # for tup in adj_list[origin]:
    #     if tup[0] == dest:
    #         if tup[1] < length:
    #             temp = False
    # if (temp):
    adj_list[origin].append((dest, length))
    #matrix[origin][dest] = length if (matrix[origin][dest] > length or matrix[origin][dest] == 0) else matrix[origin][dest]
#print(adj_list)
ret = djikstra(num_cities)
print(*ret)