import os
 
def main():
    data = os.read(0, 2**26).split()
    it = iter(map(int, data))
    n = next(it)
    q = next(it)
    m = 1 << (n - 1).bit_length()
    s = [0] * (2 * m)
    p = [0] * (2 * m)
    
    for i in range(n):
        v = next(it)
        s[m + i] = v
        p[m + i] = v
    for i in range(m - 1, 0, -1):
        l, r = i << 1, i << 1 | 1
        sl = s[l]
        s[i] = sl + s[r]
        pl, pr = p[l], sl + p[r]
        p[i] = pl if pl > pr else pr
        
    ans = []
    _s, _p = s, p
    for _ in range(q):
        t = next(it)
        if t == 1:
            k, v = next(it), next(it)
            i = k + m - 1
            _s[i] = _p[i] = v
            while i > 1:
                i >>= 1
                l, r = i << 1, i << 1 | 1
                sl = _s[l]
                _s[i] = sl + _s[r]
                pl, pr = _p[l], sl + _p[r]
                _p[i] = pl if pl > pr else pr
        else:
            u, v = next(it), next(it)
            l, r = u + m - 1, v + m
            lx, lsm, rx = 0, 0, 0
            while l < r:
                if l & 1:
                    sl, pl = _s[l], _p[l]
                    v_l = lsm + pl
                    if v_l > lx: lx = v_l
                    lsm += sl
                    l += 1
                if r & 1:
                    r -= 1
                    sr, pr = _s[r], _p[r]
                    v_r = sr + rx
                    rx = pr if pr > v_r else v_r
                l >>= 1
                r >>= 1
            res = lx if lx > lsm + rx else lsm + rx
            ans.append(str(res))
    os.write(1, ('\n'.join(ans)).encode())
 
if __name__ == '__main__':
    main()