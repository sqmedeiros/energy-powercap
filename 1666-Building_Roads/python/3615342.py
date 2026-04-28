# https://cses.fi/problemset/task/1666

from sys import stdin
from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.visited = [False] * (self.nodes + 2)
        self.graph = defaultdict(list)

    def take_input(self):
        for _ in range(self.edges):
            a, b = list(map(int, stdin.readline().strip().split()))
            self.graph[a].append(b)
            self.graph[b].append(a)

    def bfs(self, start_node):
        queue = deque()
        queue.appendleft(start_node)
        self.visited[start_node] = True

        while len(queue) > 0:
            current_node = queue.pop()
            for child in self.graph[current_node]:
                if not self.visited[child]:
                    queue.appendleft(child)
                    self.visited[child] = True

    def solve(self):            
        root_components = []
        connected_components = 0

        for i in range(1, self.nodes + 1):
            if not self.visited[i]:
                self.bfs(i)
                connected_components += 1
                root_components.append(i)            

        print(connected_components - 1)

        if len(root_components) > 1:
            for i in range(1, len(root_components)):
                print(f'{root_components[i-1]} {root_components[i]}')


if __name__ == '__main__':
    nodes, edges = list(map(int, stdin.readline().strip().split()))
    graph = Graph(nodes, edges)
    graph.take_input()
    graph.solve()