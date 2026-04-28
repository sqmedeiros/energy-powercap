import math
import queue

def main():
    n, m = map(int, input().split())

    rotas = [[] for i in range(n)]
    distance = [math.inf for i in range(n)]
    visited = [False for i in range(n)]

    q = queue.PriorityQueue()

    for i in range(m):
        a, b, c = map(int, input().split())

        a = a-1
        b = b-1

        rotas[a].append((b, c))

    q.put((0, 0))

    while(not q.empty()):
        info = q.get()

        if (not visited[info[1]]):
            visited[info[1]] = True

            distance[info[1]] = info[0]

            for edge in rotas[info[1]]:
                q.put((info[0] + edge[1], edge[0]))

    print(' '.join(map(str, distance)))


main()