import sys
 
# Nodo como tupla (sum, pref)
# Identidad para combinar: (0, 0)  porque prefijos vacíos están permitidos
ID = (0, 0)
 
def make_leaf(x):
    # Para un elemento x:
    # sum = x
    # pref = max(0, x) porque se permite prefijo vacío
    if x > 0:
        return (x, x)
    else:
        return (x, 0)
 
def combine(L, R):
    # Combina dos nodos (sum, pref)
    s = L[0] + R[0]
    p = L[1] if L[1] > (L[0] + R[1]) else (L[0] + R[1])
    return (s, p)
 
def build(arr):
    n = len(arr)
    t = [ID] * (2 * n)
    # hojas
    for i in range(n):
        t[n + i] = make_leaf(arr[i])
    # internos
    for i in range(n - 1, 0, -1):
        t[i] = combine(t[i << 1], t[i << 1 | 1])
    return t
 
def update(t, n, p, val):
    # set arr[p] = val
    p += n
    t[p] = make_leaf(val)
    p >>= 1
    while p:
        t[p] = combine(t[p << 1], t[p << 1 | 1])
        p >>= 1
 
def query_prefix_max(t, n, l, r):
    # máximo prefijo en [l, r] inclusivo
    l += n; r += n
    left_acc = ID
    right_acc = ID
    while l <= r:
        if l & 1:
            left_acc = combine(left_acc, t[l])
            l += 1
        if not (r & 1):
            right_acc = combine(t[r], right_acc)
            r -= 1
        l >>= 1; r >>= 1
    res = combine(left_acc, right_acc)
    return res[1]  # el prefijo máximo del rango
 
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n = next(it); q = next(it)
    arr = [next(it) for _ in range(n)]
 
    t = build(arr)
    base = n
 
    out = []
    for _ in range(q):
        typ = next(it); a = next(it); b = next(it)
        if typ == 1:
            # 1 k u  (1-based -> 0-based)
            k = a - 1
            u = b
            update(t, base, k, u)
        else:
            # 2 a b  (1-based -> 0-based)
            L = a - 1
            R = b - 1
            out.append(str(query_prefix_max(t, base, L, R)))
 
    sys.stdout.write("\n".join(out))
 
if __name__ == "__main__":
    main()