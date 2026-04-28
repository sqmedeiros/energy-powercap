import sys
input = sys.stdin.read
 
INF = 10**18
 
class SegmentTree:
    def __init__(self, data):
        n = len(data)
        self.n = n
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.tot = [0] * (2 * self.size)
        self.pref = [0] * (2 * self.size)
        for i in range(n):
            self.tot[self.size + i] = data[i]
            self.pref[self.size + i] = max(0, data[i])
        for i in range(self.size - 1, 0, -1):
            self.pull(i)
 
    def pull(self, i):
        left = i * 2
        right = i * 2 + 1
        self.tot[i] = self.tot[left] + self.tot[right]
        self.pref[i] = max(self.pref[left], self.tot[left] + self.pref[right])
 
    def update(self, idx, val):
        i = self.size + idx - 1  # 1-based index in the tree
        self.tot[i] = val
        self.pref[i] = max(0, val)
        i //= 2
        while i:
            self.pull(i)
            i //= 2
 
    def query(self, l, r):
        l += self.size - 1
        r += self.size - 1
        resL = (0, 0)  # (total, max_prefix)
        resR = (0, 0)
        while l <= r:
            if l % 2 == 1:
                totalL, prefL = resL
                totalCur = self.tot[l]
                prefCur = self.pref[l]
                resL = (totalL + totalCur, max(prefL, totalL + prefCur))
                l += 1
            if r % 2 == 0:
                totalR, prefR = resR
                totalCur = self.tot[r]
                prefCur = self.pref[r]
                resR = (totalCur + totalR, max(prefCur, totalCur + prefR))
                r -= 1
            l //= 2
            r //= 2
        totalL, prefL = resL
        totalR, prefR = resR
        return max(prefL, totalL + prefR)
 
def main():
    data = input().split()
    idx = 0
    n, q = int(data[idx]), int(data[idx+1])
    idx += 2
    arr = []
    for _ in range(n):
        arr.append(int(data[idx]))
        idx += 1
    seg = SegmentTree(arr)
    out_lines = []
    for _ in range(q):
        t = int(data[idx]); idx += 1
        if t == 1:
            k = int(data[idx]); idx += 1
            u = int(data[idx]); idx += 1
            seg.update(k, u)
        else:
            a = int(data[idx]); idx += 1
            b = int(data[idx]); idx += 1
            res = seg.query(a, b)
            out_lines.append(str(res))
    print("\n".join(out_lines))
 
if __name__ == "__main__":
    main()