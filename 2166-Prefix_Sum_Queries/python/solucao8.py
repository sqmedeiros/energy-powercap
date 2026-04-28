import sys
 
data = sys.stdin.read().strip().split()
it = iter(data)
 
n = int(next(it))
q = int(next(it))
arr = [int(next(it)) for _ in range(n)]
 
size = 1
while size < n:
    size <<= 1
 
tree = [(0,0)] * (2 * size)
 
 
def merge(left, right):
    sumL, bestL = left
    sumR, bestR = right
    total_sum = sumL + sumR
    best_pref = max(bestL, sumL + bestR)
    return (total_sum, best_pref)
 
for i in range(n):
    tree[size + i] = (arr[i], max(0, arr[i])) # Lleno la parte derecha del vector (las hojas)
 
for i in range(size - 1, 0, -1):
    tree[i] = merge(tree[2 * i], tree[2 * i + 1]) #Lleno la parte izq
 
 
def update_tree(pos, new_value):
    i = size + pos
    tree[i] = (new_value, max(0, new_value))
    i //= 2
    while i >= 1:
       tree[i] = merge(tree[2 * i], tree[2 * i + 1])
       i //= 2
 
def pref_sum(l, r):
    l += size
    r += size
    left_res = (0, 0)   # estos van acumulando la respuesta en cada lado
    right_res = (0, 0)
    while l <= r:   
        # Si l es un hijo derecho, le sumas 1
        if l % 2 == 1:
            left_res = merge(left_res, tree[l])
            l += 1
        # Si r es un hijo izquierdo, le restas 1
        if r % 2 == 0:
            right_res = merge(tree[r], right_res)
            r -= 1
        # Vemos los padres
        l //= 2
        r //= 2
    total_sum, best_pref = merge(left_res, right_res)
    return best_pref
 
 
 
out_lines = []
for _ in range(q):
    c = int(next(it))    
    a = int(next(it)) - 1
    b = int(next(it)) - 1
    if c == 1:
        update_tree(a, b+1)
    if c == 2:
        out_lines.append(str(pref_sum(a, b)))
 
for n in out_lines:
    print(n)