import math
def solve():
    # t = int(input().strip())
    t = 1  # Assuming t is 1 as the input is commented out in the provided C++ code
    for _ in range(t):
        n, k = map(int, input().strip().split())
        v = list(map(int, input().strip().split()))

        ans = 0
        for i in range(1, 1 << k):
            p = 1
            x = i
            ct = 0
            j = 0
            while x:
                if x & 1:
                    ct += 1
                    p = (p * v[j]) 
                j += 1
                x >>= 1

            if ct & 1:
                ans += n // p
            else:
                ans -= n // p

        print(ans)

if __name__ == "__main__":
    solve()