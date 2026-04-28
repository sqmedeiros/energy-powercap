import sys

def edit_distance(s, t):
    n, m = len(s), len(t)
    # Usamos solo dos filas para ahorrar memoria
    prev = list(range(m + 1))
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        curr[0] = i
        si = s[i - 1]
        for j in range(1, m + 1):
            if si == t[j - 1]:
                curr[j] = prev[j - 1]
            else:
                # reemplazar, insertar o borrar
                curr[j] = min(
                    prev[j - 1] + 1,  # reemplazar
                    prev[j] + 1,      # borrar de s
                    curr[j - 1] + 1   # insertar en s
                )
        prev, curr = curr, prev

    return prev[m]

def main():
    input = sys.stdin.readline
    s = input().strip()
    t = input().strip()
    print(edit_distance(s, t))

if __name__ == "__main__":
    main()