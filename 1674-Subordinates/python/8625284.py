from collections import defaultdict
import sys, threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
def solve():
    n = int(input())

    a = list(map(int,input().split()))
    tree = defaultdict(list)
    for i in range(len(a)):
        tree[a[i]-1].append(i+1)

    dp = [0]*n
    def dfs(cur,par):
        dp[cur] = 1
        for child in tree[cur]:

            if cur != par:
                dfs(child,cur) 
                dp[cur]+=dp[child] 
    dfs(0,-1)
    for i in range(len(dp)):
        dp[i]-=1
    return dp

def main():
    print(*solve())
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()




