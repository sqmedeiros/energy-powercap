import sys
from collections import defaultdict, deque

sys.setrecursionlimit(200000)

def solve(src, par, ans, tree):
    subords = 0
    for child in tree[src]:
        if child != par:
            solve(child, src, ans, tree)
            subords += (1 + ans[child])
    ans[src] = subords

def main():
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = 1  # Number of test cases
    while t > 0:
        t -= 1
        n = int(data[index])
        index += 1
        ans = [0] * (n + 1)
        tree = defaultdict(list)

        for i in range(2, n + 1):
            x = int(data[index])
            index += 1
            tree[x].append(i)
            tree[i].append(x)

        solve(1, 0, ans, tree)

        print(' '.join(map(str, ans[1:n + 1])))

if __name__ == "__main__":
    main()