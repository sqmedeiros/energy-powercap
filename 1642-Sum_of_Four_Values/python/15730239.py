import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        parts = list(map(int, line1.split()))
        if not parts:
            line1 = sys.stdin.readline()
            if not line1:
                return
            parts = list(map(int, line1.split()))

        if not parts:
             return

        n, x = parts


        line2 = sys.stdin.readline()
        if not line2:
            return
        a = list(map(int, line2.split()))

        while len(a) < n:
            more_a = list(map(int, sys.stdin.readline().split()))
            a.extend(more_a)

        sums_map = {}

        for i in range(n):
            for j in range(i + 1, n):
                current_sum = a[i] + a[j]
                remaining = x - current_sum

                if remaining in sums_map:
                    k, l = sums_map[remaining]
                    if k != i and k != j and l != i and l != j:
                        # Output 1-based indices and return
                        print(f"{k + 1} {l + 1} {i + 1} {j + 1}")
                        return


            for j in range(i):
                 sums_map[a[i] + a[j]] = (j, i) # Store as (earlier_index, later_index)


        print("IMPOSSIBLE")

    except EOFError:
        pass
    except ValueError:
        pass

if __name__ == "__main__":
    solve()