import sys

def find_four_indices(n, x, a):
    sums = {}  # sum -> list of pairs (i, j) (0-based indices)
    for i in range(n):
        for j in range(i+1, n):
            s = a[i] + a[j]
            need = x - s
            if need in sums:
                # try all stored pairs for 'need' to find disjoint indices
                for (p, q) in sums[need]:
                    if p != i and p != j and q != i and q != j:
                        # return 1-based positions
                        return (p+1, q+1, i+1, j+1)
            # store this pair for sum s
            if s not in sums:
                sums[s] = []
            sums[s].append((i, j))
    return None

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0]); x = int(data[1])
    a = list(map(int, data[2:]))

    ans = find_four_indices(n, x, a)
    if ans is None:
        print("IMPOSSIBLE")
    else:
        print(*ans)

if __name__ == "__main__":
    main()