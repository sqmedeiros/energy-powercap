import sys

# 假設使用 input() 用於本地測試，sys.stdin.readline() 用於比賽平台
def main():
    # 本地測試時使用 input()，避免 ValueError
    n = int(input())  # 這行可以改成 sys.stdin.readline() 用於比賽平台
    bosses = list(map(int, input().split()))  # 改用 input() 方便測試

    # 初始化樹結構
    tree = [[] for _ in range(n + 1)]
    for i in range(2, n + 1):
        tree[bosses[i - 2]].append(i)

    # 儲存每個節點的下屬數量
    subordinates = [0] * (n + 1)
    visited = [False] * (n + 1)
    stack = [1]
    order = []

    # 後序遍歷，紀錄每個節點的訪問順序
    while stack:
        node = stack.pop()
        order.append(node)
        for child in tree[node]:
            stack.append(child)

    # 根據後序遍歷結果計算每個節點的下屬數量
    for node in reversed(order):
        for child in tree[node]:
            subordinates[node] += 1 + subordinates[child]

    # 輸出每個節點的下屬數量
    print(' '.join(str(subordinates[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()