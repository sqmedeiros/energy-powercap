def dist(c1, c2):
    n = len(c1)
    m = len(c2)

    anterior = [m - j for j in range(m + 1)]
    actual = [0] * (m + 1)

    for i in range(n - 1, -1, -1):
        actual[m] = n - i
        for j in range(m - 1, -1, -1):
            if c2[j] == c1[i]:
                actual[j] = anterior[j + 1]
            else:
                actual[j] = 1 + min(anterior[j], actual[j + 1], anterior[j + 1])
        anterior, actual = actual, anterior

    return anterior[0]

def main():
    c1 = input().strip()
    c2 = input().strip()
    print(dist(c1, c2))

main()