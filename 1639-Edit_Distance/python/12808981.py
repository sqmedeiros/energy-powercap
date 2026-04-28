from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def edit_distance(a: str, b: str) -> int:
    # Ensure b is the shorter
    if len(a) < len(b):
        a, b = b, a
    n, m = len(a), len(b)
    # Build peq (pattern equality) bitmasks for b
    peq = {}
    for i, ch in enumerate(b):
        peq[ch] = peq.get(ch, 0) | (1 << i)
    # Initial state
    VP = (1 << m) - 1
    VN = 0
    curr = m

    for ch in a:
        # 1) Character mask for this text char
        PM = peq.get(ch, 0)
        # 2) Compute intermediate
        X  = PM | VN
        D0 = (((X & VP) + VP) ^ VP) | X
        # 3) HP and HN
        HP = VN | ~(D0 | VP)
        HN = VP & D0
        # 4) Update distance
        if (HP >> (m-1)) & 1:
            curr += 1
        elif (HN >> (m-1)) & 1:
            curr -= 1
        # 5) Shift and recalc VP, VN
        HP = (HP << 1) | 1
        HN = HN << 1
        VP = (HN) | ~(D0 | HP)
        VN = HP & D0

    return curr

def main():
    a = input().rstrip('\n')
    b = input().rstrip('\n')
    print(str(edit_distance(a, b)))

if __name__ == "__main__":
    main()