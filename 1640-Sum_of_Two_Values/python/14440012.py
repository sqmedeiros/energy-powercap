import sys


def solve():
    it = map(int, sys.stdin.buffer.read().split())
    out = []

    n, x = next(it), next(it)

    values = {}
    for i in range(1, n + 1):
        ai = next(it)
        if ai in values:
            out.append(f"{values[ai]} {i}")
            sys.stdout.write("\n".join(out))
            return

        values[x - ai] = i

    sys.stdout.write("IMPOSSIBLE")


if __name__ == "__main__":
    solve()
