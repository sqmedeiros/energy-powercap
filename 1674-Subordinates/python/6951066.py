import sys
sys.setrecursionlimit(10**6)

def solve(curr, prev, count, tree):
    count[curr] = 1
    for nbr in tree[curr]:
        solve(nbr, curr, count, tree)
        count[curr] += count[nbr]

if __name__ == '__main__':
 n = int(input())
 tree = dict()
 for i in range(1, n + 1):
  tree[i] = []
 sub = list(map(int, input().split()))
 for i in range(n - 1):
  tree[sub[i]].append(i + 2)
 count = [0] * (n + 1)
 solve(1, 0, count, tree)
 for i in range(1, n + 1):
     print(count[i] - 1, end = " ")

