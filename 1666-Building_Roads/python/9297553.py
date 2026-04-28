import math
from collections import deque

class DSU:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 != parent2:
            if self.rank[parent1] > self.rank[parent2]:
                self.parent[parent2] = parent1
            elif self.rank[parent1] < self.rank[parent2]:
                self.parent[parent1] = parent2
            else:
                self.parent[parent2] = parent1
                self.rank[parent1] += 1

    def getParents(self):
        parents = []
        for i, node in enumerate(self.parent):
            if node == i:
                parents.append((node))
        return parents

def solve():
    n, m = [int(num) for num in input().split(" ")]
    #nums = [int(num) for num in input().split(" ")]
    connections = []
    i = 0
    while i<m:
        connections.append([int(num)-1 for num in input().split(" ")])
        i+=1

    graph = DSU(n)

    for frm, to in connections:
        graph.union(frm, to)

    parents = graph.getParents()
    print(len(parents) - 1)
    for i in range(len(parents)-1):
        print(parents[i]+1, parents[i+1]+1)


solve()