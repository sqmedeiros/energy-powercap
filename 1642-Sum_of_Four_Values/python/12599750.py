from collections import defaultdict
import sys

def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    x = int(data[1])
    a = list(map(int, data[2:]))

    sum_map = defaultdict(list)

    # Lưu các cặp (i, j) theo tổng của chúng
    for i in range(n):
        for j in range(i + 1, n):
            s = a[i] + a[j]
            sum_map[s].append((i, j))

    # Tìm 2 cặp (i, j) và (k, l) sao cho tổng 4 phần tử là x và chỉ số khác nhau
    for i in range(n):
        for j in range(i + 1, n):
            s = a[i] + a[j]
            target = x - s
            if target in sum_map:
                for k, l in sum_map[target]:
                    # Đảm bảo 4 chỉ số đều khác nhau
                    if len({i, j, k, l}) == 4:
                        # In ra các chỉ số từ 1
                        print(i + 1, j + 1, k + 1, l + 1)
                        return
    print("IMPOSSIBLE")

if __name__ == "__main__":
    main()