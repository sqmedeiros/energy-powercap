import java.io.*;
 
public class  entry_15525681 {
 
    static class Node {
        long sum, pref, suff, ans;
 
        Node(long s, long p, long su, long a) {
            sum = s; pref = p; suff = su; ans = a;
        }
    }
 
    static Node makeNode(long x) {
        long v = Math.max(0, x);
        return new Node(x, v, v, v);
    }
 
    static Node merge(Node L, Node R) {
        long sum = L.sum + R.sum;
        long pref = Math.max(L.pref, L.sum + R.pref);
        long suff = Math.max(R.suff, R.sum + L.suff);
        long ans = Math.max(Math.max(L.ans, R.ans), L.suff + R.pref);
        return new Node(sum, pref, suff, ans);
    }
 
    static class SegTree {
        int size;
        Node[] tree;
 
        SegTree(long[] arr, int n) {
            size = 1;
            while (size < n) size <<= 1;
 
            tree = new Node[2 * size];
 
            // fill leaves
            for (int i = 0; i < n; i++)
                tree[size + i] = makeNode(arr[i + 1]);
            for (int i = n; i < size; i++)
                tree[size + i] = makeNode(0);
 
            // build internal nodes
            for (int i = size - 1; i > 0; i--)
                tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
        }
 
        void update(int pos, long val) {
            int i = pos - 1 + size;
            tree[i] = makeNode(val);
 
            while (i > 1) {
                i >>= 1;
                tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
            }
        }
    }
 
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
 
        int n = fs.nextInt();
        int q = fs.nextInt();
 
        long[] arr = new long[n + 1];
        for (int i = 1; i <= n; i++)
            arr[i] = fs.nextInt();
 
        SegTree st = new SegTree(arr, n);
 
        StringBuilder sb = new StringBuilder();
        while (q-- > 0) {
            int k = fs.nextInt();
            long x = fs.nextInt();
            st.update(k, x);
            sb.append(st.tree[1].ans).append("\n");
        }
 
        System.out.print(sb);
    }
 
    // Fast scanner
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
 
        private int read() throws IOException {
            if (ptr >= len) {
                ptr = 0;
                len = in.read(buffer);
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }
 
        int nextInt() throws IOException {
            int c;
            while ((c = read()) <= ' ') if (c == -1) return -1;
            int sign = 1;
            if (c == '-') { sign = -1; c = read(); }
            int val = c - '0';
            while ((c = read()) > ' ')
                val = val * 10 + (c - '0');
            return val * sign;
        }
    }
}