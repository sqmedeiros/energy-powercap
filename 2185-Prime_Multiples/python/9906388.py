def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for i in range(1, 1 << k):
        cnt = 0
        mul = 1
        for j in range(k):
            if (i >> j) & 1:
                mul *= a[j]
                cnt += 1
            if mul > 1e18:
                break
        if cnt % 2 == 1:
            ans += n // mul
        else:
            ans -= n // mul

    print(ans)

if __name__ == "__main__":
    main()