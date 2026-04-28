#!/usr/bin/env python
# -*- coding: utf-8 -*-


def two_sum(vals, target: int):
    if target == 1:
        return None
    seen: dict[int, int] = {}
    for i, v in enumerate(vals):
        diff = target - v
        if diff in seen:
            return (seen[diff] + 1, i + 1)
        seen[v] = i
    return None


def main() -> None:
    """Main function."""
    n, target = list(map(int, input().split()))
    vals = list(map(int, input().split()))
    if res := two_sum(vals, target):
        a, b = res
        print(f"{a} {b}")
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()