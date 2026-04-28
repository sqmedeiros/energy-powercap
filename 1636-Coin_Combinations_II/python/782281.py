def coinCombination(coins, sum, size):
    count = [0] * (sum + 1)
    count[0] = 1
    for coin in range(size):
        for sub_sum in range(coins[coin], sum + 1):
            count[sub_sum] = (
                count[sub_sum] % ((10 ** 9) + 7)
                + count[sub_sum - coins[coin]] % ((10 ** 9) + 7)
            ) % ((10 ** 9) + 7)

    return count[sum]


def main():
    size, sum1 = map(int, input().split())
    coins = list(map(int, input().split()))
    print(coinCombination(coins, sum1, size) % ((10 ** 9) + 7))


if __name__ == "__main__":
    main()