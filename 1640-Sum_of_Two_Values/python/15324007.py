import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    x = int(data[1])

    a = []
    for i in range(n):
        value = int(data[2 + i])
        a.append((value, i + 1))  # Orijinal indeksi (1-based) sakla

    a.sort()

    i, j = 0, n - 1
    while i < j:
        total = a[i][0] + a[j][0]
        if total == x:
            print(f"{a[i][1]} {a[j][1]}")
            return
        elif total < x:
            i += 1
        else:
            j -= 1

    print("IMPOSSIBLE")

if __name__ == "__main__":
    main()