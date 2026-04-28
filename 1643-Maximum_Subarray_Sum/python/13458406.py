from math import comb, inf

if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    ans = -inf
    s = -inf
    for i in arr:
        s += i
        if s < i:
            s = i
        ans = max(ans, s)
    print(ans)