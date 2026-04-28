 
class SegmentTree:
    def __init__(self, xs):
        n = len(xs)
        N = 1
        while N < n:
            N *= 2
        t = [0] * (2 * N)  # max prefix sum
        s = [0] * (2 * N)  # sum
        t[N:N + n] = [max(x, 0) for x in xs]
        s[N:N + n] = xs
        for i in range(N - 1, 0, -1):
            s[i] = s[i * 2] + s[i * 2 + 1]
            t[i] = max(t[i * 2], s[i * 2] + t[i * 2 + 1])
 
        self.N = N
        self.t = t
        self.s = s
 
    def set(self, i, u):
        i += self.N
        self.s[i] = u
        self.t[i] = max(u, 0)
        i //= 2
        while (i >= 1):
            self.s[i] = self.s[2 * i] + self.s[2 * i + 1]
            self.t[i] = max(self.t[2 * i], self.s[2 * i] + self.t[2 * i + 1])
            i //= 2
 
    def max(self, l, r):
        l += self.N
        r += self.N
        s_l = 0
        t_l = 0
        t_r = 0
        while (l < r):
            if l & 1:
                t_l = max(t_l, s_l + self.t[l])
                s_l += self.s[l]
                l += 1
            if r & 1:
                r -= 1
                t_r = max(self.t[r], self.s[r] + t_r)
            l >>= 1
            r >>= 1
        ans = max(t_l, s_l + t_r)
        return ans
 
n, q = map(int, input().split())
xs = [int(x) for x in input().split()]
 
st = SegmentTree(xs)
for i in range(q):
    cmd = [int(x) for x in input().split()]
    if cmd[0] == 1:
        st.set(cmd[1] - 1, cmd[2])
    else:
        ans = st.max(cmd[1] - 1, cmd[2])
        print(ans)