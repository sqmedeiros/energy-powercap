from sys import stdin


class Solution:
    def __init__(self, number_of_nodes, number_of_edges):
        self.number_of_nodes = number_of_nodes
        self.number_of_edges = number_of_edges
        self.graph = [[] for _ in range(self.number_of_nodes + 1)]
        self.parent = [i for i in range(self.number_of_nodes + 1)]
        self.size = [1 for _ in range(self.number_of_nodes + 1)]

    def take_input(self):
        for _ in range(self.number_of_edges):
            u, v = list(map(int, stdin.readline().strip().split()))
            self.graph[u].append(v)
            self.union_by_size(u, v)

    def find_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_parent(self.parent[node])
        return self.parent[node]

    def union_by_size(self, first_node, second_node):
        first_parent = self.find_parent(first_node)
        second_parent = self.find_parent(second_node)

        if first_parent == second_parent:
            return

        if self.size[first_parent] < self.size[second_parent]:
            self.parent[first_parent] = second_parent
            self.size[second_parent] += self.size[first_parent]
        else:
            self.parent[second_parent] = first_parent
            self.size[first_parent] += self.size[second_parent]

    def solve(self):
        self.take_input()
        number_of_roads = 0
        answer = []
        for i in range(1, self.number_of_nodes + 1):
            if self.parent[i] == i:
                number_of_roads += 1
                answer.append(i)

        number_of_roads -= 1
        print(number_of_roads)
        for i in range(1, len(answer)):
            print(f'{answer[i - 1]} {answer[i]}')

if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().strip().split()))
    solution = Solution(n ,m)    
    solution.solve()