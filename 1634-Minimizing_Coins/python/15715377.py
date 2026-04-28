""" """

import sys


def solve():
    # Đọc dữ liệu
    line1 = sys.stdin.readline().split()
    n, x = map(int, line1)
    c = list(map(int, sys.stdin.readline().split()))

    # Khởi tạo dp với một số lớn (nhưng không quá lớn như float('inf') để tính toán nhanh hơn)
    # 10^6 + 1 là đủ vì tối đa chỉ cần x đồng xu mệnh giá 1
    INF = x + 1
    dp = [INF] * (x + 1)
    dp[0] = 0

    # Thay đổi thứ tự vòng lặp để Python chạy nhanh hơn (Push/Pull lai)
    for coin in c:
        for i in range(coin, x + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    result = dp[x]
    print(result if result <= x else -1)


if __name__ == "__main__":
    solve()