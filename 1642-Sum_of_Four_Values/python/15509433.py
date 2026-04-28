import sys

def find_four_sum_indices(a, x):
    n = len(a)
    pairs = {}  # sum -> list of (i, j)
    # iterate pairs; for each pair check if complement exists
    for i in range(n):
        for j in range(i + 1, n):
            s = a[i] + a[j]
            need = x - s
            if need in pairs:
                # check any stored pair for disjointness
                for p, q in pairs[need]:
                    if p != i and p != j and q != i and q != j:
                        # return 1-based positions
                        return (p + 1, q + 1, i + 1, j + 1)
            # store current pair for its sum
            if s not in pairs:
                pairs[s] = []
            pairs[s].append((i, j))
    return None

def main():
    data = sys.stdin.read().strip().split()
    n = int(data[0]); x = int(data[1])
    a = list(map(int, data[2:2+n]))
    ans = find_four_sum_indices(a, x)
    if ans is None:
        print("IMPOSSIBLE")
    else:
        print(*ans)

if __name__ == "__main__":
    main()