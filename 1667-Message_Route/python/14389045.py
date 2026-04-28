#!/usr/bin/env python3
# ---------- CP / CSES Python Template (fast & flexible) ----------
# Usage:
#   - Put problem-specific logic inside solve() (or solve_one() + T loop).
#   - Keep helpers here; remove ones you don't need to shrink code before submit.
#   - Works with: single case, multiple test cases, graphs, grids, etc.

import sys
from collections import deque, defaultdict
import math
import heapq
from typing import List, Tuple, Iterable

# ---------- FAST INPUT ----------
# Read-all-at-once token scanner (best for typical CSES)
_tokens = sys.stdin.buffer.read().split()
_it = iter(_tokens)

def ni() -> int:
    """next int"""
    return int(next(_it))
def ns() -> str:
    """next token as str (decoding once)"""
    return next(_it).decode()
def nb() -> bytes:
    """next token as raw bytes"""
    return next(_it)
def nf() -> float:
    """next float"""
    return float(next(_it))

# If you need streaming-by-line (rare on CSES), replace the block above with:
# for line in sys.stdin.buffer: ...   (keep this template but don't use ni/ns).

# ---------- FAST OUTPUT ----------
out_lines: List[str] = []
def out(*args, sep=" ", end="\n"):
    """buffered printing"""
    out_lines.append(sep.join(map(str, args)) + ("" if end == "" else end))

def flush():
    if out_lines:
        sys.stdout.write("".join(out_lines))

# ---------- COMMON PARSING HELPERS ----------
def read_list_int(n: int) -> List[int]:
    """read n integers"""
    return [ni() for _ in range(n)]

def read_matrix_int(n: int, m: int) -> List[List[int]]:
    """read n x m matrix of ints"""
    return [[ni() for _ in range(m)] for __ in range(n)]





def inb(r, c, n, m) -> bool:
    return 0 <= r < n and 0 <= c < m

# ---------- COMMON ALGO SNIPPETS (keep what you use) ----------




# ---------- ANSWER FORMAT HELPERS ----------
def yesno(flag: bool):
    out("YES" if flag else "NO")

# ---------- SOLVE ----------
def solve() -> None:
    """
    Pattern 1: single test case
    --------------------------------
    # Example: read N and N ints, print sum
    # N = ni()
    # arr = read_list_int(N)
    # out(sum(arr))
     Pattern 2: multiple test cases (T first)
    --------------------------------
    # T = ni()
    # for _ in range(T):
    #     # parse one case
    #     n = ni()
    #     arr = read_list_int(n)
    #     out(process(arr))
     Pattern 3: graph
    --------------------------------
    # n, m = ni(), ni()
    # g = read_graph_unweighted(n, m, directed=False, one_indexed=True)
    # # do BFS/DFS, etc.
     Pattern 4: grid of chars
    --------------------------------
    # n, m = ni(), ni()
    # grid = [list(ns()) for _ in range(n)]
    # # BFS on grid using DIR4, inb()
     Replace the block below with the specific problem.
    """
    n, m = read_list_int(2)

    adj_list = defaultdict(list) 
    for _ in range(m):
        a, b = read_list_int(2)
        adj_list[a].append(b)
        adj_list[b].append(a)

    parents = [-1] * (n + 1)
    Q = deque()
    seen = [0] * (n + 1)
    Q.append(1)
    seen[1] = 1
    found = False
    while Q:
        u = Q.popleft()
        if u == n:
            found = True
            break
        for v in adj_list[u]:
            if not seen[v]:
                Q.append(v)
                seen[v] = 1
                parents[v] = u    

    if not found:
        print('IMPOSSIBLE')
        return
    cur = n
    path = []

    while cur != 1:
        #print(cur)
        path.append(cur)
        cur = parents[cur]
    path.append(cur)
    print(len(path))
    print(*path[::-1])





# ---------- MAIN ----------
if __name__ == "__main__":
    # For quick local testing without files, set _TEST to a bytes string:
    # _TEST = b"""\
    # 5
    # """
    _TEST = None
    if _TEST is not None:
        data = _TEST.split()
        _it = iter(data)  # rebind scanner
    solve()
    flush()