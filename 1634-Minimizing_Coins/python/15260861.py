def read_datas():
    n, x = map(int, input().split())
    coins = sorted(map(int, input().split()))
    return x, coins


def solve(x, coins):

    placeholder = x + 1
    num_of_coins = [placeholder] * (x + 1)
    num_of_coins[0] = 0
    curr_num = 0

    for curr_num in range(x):
        curr_num_of_coins = num_of_coins[curr_num]
        for other in coins:
            new_num = curr_num + other
            if new_num > x:
                break
            num_of_coins[new_num] = min(num_of_coins[new_num], curr_num_of_coins + 1)

    return -1 if num_of_coins[x] == placeholder else num_of_coins[x]


def main():

    x, coins = read_datas()

    min_number_of_coins = solve(x, coins)
    print(min_number_of_coins)


main()