import collections
import functools
import heapq
import bisect
import itertools
import math
import os
from io import BytesIO, IOBase
from sys import setrecursionlimit, stderr, stdin, stdout
from collections import defaultdict

setrecursionlimit(20000)


def get_ints():
    return list(map(int, input().split()))


def get_int():
    return int(input())


def get_string():
    return "".join(list(input().rstrip()))


def get_chars():
    return list(input().rstrip())


def eprint(*args):
    print(*args, sep=", ", file=stderr)


def main():
    n, m = get_ints()
    graph = defaultdict(list)
    parents = [0] * n
    visited = [False] * n
    for _ in range(m):
        s, d = get_ints()
        s -= 1
        d -= 1
        graph[s].append(d)
        graph[d].append(s)

    answer = []
    for i in range(n):
        if not visited[i]:
            stack = [(i, -1, iter(graph[i]))]
            visited[i] = True
            parents[i] = -1
            while stack:
                node, parent, neighs = stack[-1]
                nei = next(neighs, None)
                if nei is not None:
                    if nei == parent:
                        continue

                    if visited[nei]:
                        answer.append(nei + 1)
                        while node != nei:
                            answer.append(node + 1)
                            node = parents[node]
                        answer.append(nei + 1)
                        print(len(answer))
                        print(*answer, sep=" ")
                        return
                    else:
                        visited[nei] = True
                        parents[nei] = node
                        stack.append((nei, node, iter(graph[nei])))
                else:
                    stack.pop()

    print("IMPOSSIBLE")


# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


stdin = IOWrapper(stdin)  # type: ignore
stdout = IOWrapper(stdout)  # type: ignore
input = lambda: stdin.readline().rstrip("\r\n")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


# endregion

if __name__ == "__main__":
    main()