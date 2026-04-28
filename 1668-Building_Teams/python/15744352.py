from itertools import combinations, product, permutations
from collections import deque, Counter, defaultdict
from math import inf, gcd, lcm, factorial, sqrt, ceil, floor, log, log2, log10
from heapq import *
import sys, inspect, re
from bisect import bisect_left, bisect_right
import sys


def solve():
    if 1:
        n, m = map(int, input().split())

        adj = defaultdict(set)
        idx = 2
        for _ in range(m):
            u, v = map(int, input().split())
            adj[u].add(v)
            adj[v].add(u)
            idx += 2

        colors = [0] * (n + 1)  # 0: unvisited, 1: team 1, 2: team 2

        # 2. Iterate through all nodes to handle disconnected components
        def bfs(i):
            if colors[i] == 0:
                # Start BFS
                colors[i] = 1  # Start first person on Team 1
                q = [i]
                for curr in q:
                    for neighbor in adj[curr]:
                        if colors[neighbor] == colors[curr]:
                            exit(print("IMPOSSIBLE"))

                        if colors[neighbor] == 0:
                            # Assign opposite team: if 1 -> 2, if 2 -> 1
                            colors[neighbor] = 3 - colors[curr]
                            q.append(neighbor)

        for i in range(1, n + 1):
            if colors[i] == 0:
                bfs(i)
        # 3. Print colors for nodes 1 to n
        print(*(colors[1:]))
        exit()
    if 1:
        pass
        # n, x, y = map(int, first_input.split())
        # n, x, y = map(int, input().split())

    elif first_input != "second":
        for _ in range(
            int(input()) if first_input == "first" else int(first_input)
        ):
            n = int(input())
            # n, k = map(int, input().split())
            # n, k, x = map(int, input().split())

            # a = [e for e in input()]
            # a = input()
            a = list(map(int, input().split()))

    elif first_input == "second":
        for _ in range(int(input())):
            n = int(input())
            # n, k = map(int, input().split())
            # n, k, x = map(int, input().split())

            # a = [e for e in input()]
            # a = input()
            a = list(map(int, input().split()))


# some classes were based on https://github.com/cheran-senthil/PyRival/tree/master/pyrival/data_structures
from bisect import bisect_left, bisect_right


class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        iterable = sorted(iterable)
        self.micros = [
            iterable[i : i + self.block_size - 1]
            for i in range(0, len(iterable), self.block_size - 1)
        ] or [[]]
        self.macro = [i[0] for i in self.micros[1:]]
        self.micro_size = [len(i) for i in self.micros]
        self.fenwick = FenwickTree(self.micro_size)
        self.size = len(iterable)

    def add(self, x):
        i = bisect_left(self.macro, x)
        j = bisect_right(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i : i + 1] = (
                self.micros[i][: self.block_size >> 1],
                self.micros[i][self.block_size >> 1 :],
            )
            self.micro_size[i : i + 1] = (
                self.block_size >> 1,
                self.block_size >> 1,
            )
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def _delete(self, i, j):
        self.micros[i].pop(j)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        if len(self.micros[i]) == 0 and len(self.micros) > 1:
            del self.micros[i]
            del self.micro_size[i]
            self.macro = [m[0] for m in self.micros[1:]]
            self.fenwick = FenwickTree(self.micro_size)

    def remove(self, x):
        # Find the block where x 'should' be
        i = bisect_right(self.macro, x)

        # Check block i (Standard case)
        if i < len(self.micros):
            j = bisect_left(self.micros[i], x)
            if j < len(self.micros[i]) and self.micros[i][j] == x:
                self._delete(i, j)
                return

        # Check block i-1 (Boundary/Duplicate case)
        # This is the fix for "1 not in list" error
        if i > 0:
            j = bisect_left(self.micros[i - 1], x)
            if j < len(self.micros[i - 1]) and self.micros[i - 1][j] == x:
                self._delete(i - 1, j)
                return

        raise ValueError(f"{x} not in list")

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        val = self.micros[i][j]  # Capture value before delete
        self._delete(i, j)
        return val

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.bisect_right(x) - self.bisect_left(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def bisect_left(self, x):
        i = bisect_left(self.macro, x)
        return self.fenwick(i) + bisect_left(self.micros[i], x)

    def bisect_right(self, x):
        i = bisect_right(self.macro, x)
        return self.fenwick(i) + bisect_right(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.bisect_right(x) - self.bisect_left(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def bisect_left(self, x):
        i = bisect_left(self.macro, x)
        return self.fenwick(i) + bisect_left(self.micros[i], x)

    def bisect_right(self, x):
        i = bisect_right(self.macro, x)
        return self.fenwick(i) + bisect_right(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        return self.__class__.__name__ + (
            "({})".format(self.value) if self else "()"
        )


class LinkedList:
    def __init__(self, iterable=None):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.__len = 0
        if iterable is not None:
            self += iterable

    def get_node(self, index):
        node = self.sentinel
        i = 0
        while i <= index:
            node = node.next
            if node == self.sentinel:
                break
            i += 1
        if node == self.sentinel:
            node = None
        return node

    def __getitem__(self, index):
        node = self.get_node(index)
        return node.value

    def __len__(self):
        return self.__len

    def __setitem__(self, index, value):
        node = self.get_node(index)
        node.value = value

    def __delitem__(self, index):
        node = self.get_node(index)
        if node:
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            node.prev = None
            node.next = None
            node.value = None
            self.__len -= 1

    def __repr__(self):
        return str(self.to_list())

    def to_list(self):
        elts = []
        curr = self.sentinel.next
        while curr != self.sentinel:
            elts.append(curr.value)
            curr = curr.next
        return elts

    def append_node(self, node):
        self.insert_between(node, self.sentinel.prev, self.sentinel)

    def append(self, value):
        node = Node(value)
        self.insert_between(node, self.sentinel.prev, self.sentinel)

    def appendleft(self, value):
        node = Node(value)
        self.insert_between(node, self.sentinel, self.sentinel.next)

    def insert(self, index, value):
        new_node = Node(value)
        len_ = len(self)
        if len_ == 0:
            self.insert_between(new_node, self.sentinel, self.sentinel)
        elif index >= 0 and index < len_:
            node = self.get_node(index)
            self.insert_between(new_node, node.prev, node)
        elif index == len_:
            self.insert_between(new_node, self.sentinel.prev, self.sentinel)
        else:
            raise IndexError

    def insert_between(self, node, left_node, right_node):
        if node and left_node and right_node:
            node.prev = left_node
            node.next = right_node
            left_node.next = node
            right_node.prev = node
            self.__len += 1
        else:
            raise IndexError

    def insert_after(self, node, value):
        new_node = Node(value)
        node.next.prev = new_node
        new_node.next = node.next
        node.next = new_node
        new_node.prev = node
        self.__len += 1

    def merge_left(self, other):
        self.sentinel.next.prev = other.sentinel.prev
        other.sentinel.prev.next = self.sentinel.next
        self.sentinel.next = other.sentinel.next
        self.sentinel.next.prev = self.sentinel
        self.__len += other.__len

    def merge_right(self, other):
        self.sentinel.prev.next = other.sentinel.next
        other.sentinel.next.prev = self.sentinel.prev
        self.sentinel.prev = other.sentinel.prev
        self.sentinel.prev.next = self.sentinel
        self.__len += other.__len

    def pop(self, node=None):
        if node is None:
            node = self.sentinel.prev
        if self.__len < 1:
            raise IndexError
        node.prev.next = node.next
        node.next.prev = node.prev
        self.__len -= 1
        return node.value

    def before(self, node):
        return node.prev.prev if node.prev == self.sentinel else node.prev

    left = before
    prev = before

    def after(self, node):
        return node.next.next if node.next == self.sentinel else node.next

    right = after
    next = after

    def get_min_node(self):
        if self.__len == 0:
            return None
        curr = self.sentinel.next
        min_node = curr
        while curr != self.sentinel:
            if curr.value < min_node.value:
                min_node = curr
            curr = curr.next

        return min_node

    def get_max_node(self):
        if self.__len == 0:
            return None
        curr = self.sentinel.next
        min_node = curr
        while curr != self.sentinel:
            if curr.value > min_node.value:
                min_node = curr
            curr = curr.next

        return min_node


def input():
    return sys.stdin.readline().strip()


def p(*args):
    if args and isinstance(args[0], bool):
        sys.stdout.write("YES\n" if args[0] else "NO\n")
    else:
        sys.stdout.write(" ".join(str(e) for e in args) + "\n")


def p2(*args):
    if args and isinstance(args[0], bool):
        sys.stdout.write("Yes\n" if args[0] else "No\n")
    else:
        sys.stdout.write(" ".join(str(e) for e in args) + "\n")


def YES():
    sys.stdout.write("YES\n")


def NO():
    sys.stdout.write("NO\n")


def Yes():
    sys.stdout.write("Yes\n")


def No():
    sys.stdout.write("No\n")


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def debug(*args):
    frame = inspect.currentframe()
    try:
        prev_frame = frame.f_back

        call_info = inspect.getframeinfo(prev_frame)
        code_context = call_info.code_context[0].strip()

        match = re.search(r"debug\((.*)\)", code_context)

        if match:
            arg_names = [name.strip() for name in match.group(1).split(",")]

            for name, value in zip(arg_names, args):
                print(f"{name} = {value}", file=sys.stderr)
        else:
            print("Could not parse variable names:", args, file=sys.stderr)

    finally:
        del frame


from random import getrandbits

RANDOM = getrandbits(32)


class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)

    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


if __name__ == "__main__":
    solve()