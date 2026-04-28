import sys

class Solution:
    def __init__(self):
        self.len, self.target = map(int, input().split())
        self.inp = sorted(map(int, input().split()))  # sort for early pruning

    def solve(self):
        dp = [float('inf')] * (self.target + 1)
        dp[0] = 0  # base case

        for i in range(1, self.target + 1):
            for coin in self.inp:
                if coin > i:
                    break  # early pruning
                dp[i] = min(dp[i], 1 + dp[i - coin])

        print(dp[self.target] if dp[self.target] != float('inf') else -1)

if __name__ == "__main__":
    #sys.stdin = open("input.txt", "r")
    input = sys.stdin.readline
    obj = Solution(); obj.solve()
    # for test_case in range(int(input())): obj = Solution(); obj.solve(test_case+1)