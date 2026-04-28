import sys
input = sys.stdin.readline
 
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        # cada nodo guarda (suma_total, max_prefijo)
        self.tree = [(0, 0)] * (2 * self.size)
        # cargar hojas
        for i in range(self.n):
            x = arr[i]
            # max prefijo = max(0, x)
            self.tree[self.size + i] = (x, max(0, x))
 
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[2*i], self.tree[2*i+1])
 
    # cómo combinar dos nodos
    def _merge(self, left, right):
        sum_L, pref_L = left
        sum_R, pref_R = right
        total = sum_L + sum_R
        pref = max(pref_L, sum_L + pref_R)
        return (total, pref)
 
    # update puntual
    def update(self, index, value):
        pos = self.size + index
        self.tree[pos] = (value, max(0, value))
 
        pos //= 2
        while pos >= 1:
            self.tree[pos] = self._merge(self.tree[2*pos], self.tree[2*pos+1])
            pos //= 2
 
    def query(self, l, r):
        l += self.size
        r += self.size
 
        # acumuladores neutros
        left_res = (0, 0)   # sum=0, pref=0
        right_res = (0, 0)  # sum=0, pref=0
 
        while l <= r:
            if l % 2 == 1:  # hijo derecho
                left_res = self._merge(left_res, self.tree[l])
                l += 1
            if r % 2 == 0:  # hijo izquierdo
                right_res = self._merge(self.tree[r], right_res)
                r -= 1
            l //= 2
            r //= 2
 
        res = self._merge(left_res, right_res)
        return res[1]  # solo queremos el prefijo máximo
 
def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
 
    st = SegmentTree(arr)
 
    out = []
    for _ in range(q):
        t, a, b = map(int, input().split())
        if t == 1:
            st.update(a - 1, b)
        else:
            out.append(str(st.query(a - 1, b - 1)))
 
    print("\n".join(out))
 
main()