import java.io.*;
import java.util.*;
 
public class entry_9811844 {
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
 
        public FastReader() {
            br = new BufferedReader(
                    new InputStreamReader(System.in));
        }
 
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt() {
            return Integer.parseInt(next());
        }
 
        long nextLong() {
            return Long.parseLong(next());
        }
 
        double nextDouble() {
            return Double.parseDouble(next());
        }
 
        String nextLine() {
            String str = "";
            try {
                if (st.hasMoreTokens()) {
                    str = st.nextToken("\n");
                } else {
                    str = br.readLine();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
 
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
 
        public Reader() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public Reader(String file_name) throws IOException {
            din = new DataInputStream(
                    new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public String readLine() throws IOException {
            byte[] buf = new byte[BUFFER_SIZE]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n') {
                    if (cnt != 0) {
                        break;
                    } else {
                        continue;
                    }
                }
                buf[cnt++] = (byte) c;
            }
            return new String(buf, 0, cnt);
        }
 
        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
 
            if (neg)
                return -ret;
            return ret;
        }
 
        public long nextLong() throws IOException {
            long ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg)
                return -ret;
            return ret;
        }
 
        public double nextDouble() throws IOException {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
 
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
 
            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }
 
            if (neg)
                return -ret;
            return ret;
        }
 
        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0,
                    BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }
 
        private byte read() throws IOException {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }
 
        public void close() throws IOException {
            if (din == null)
                return;
            din.close();
        }
    }
 
    static class p implements Comparable<p> {
        long a;
        long b;
        long c;
 
        p(long a, long b) {
            this.a = a;
            this.b = b;
        }
 
        p(long a, long b, long c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }
 
        @Override
        public int compareTo(p other) {
            if (this.a != other.a) {
                return Long.compare(this.a, other.a);
            }
            if (this.b != other.b) {
                return Long.compare(this.b, other.b);
            }
            return Long.compare(this.c, other.c);
        }
 
        @Override
        public boolean equals(Object o) {
            if (this == o)
                return true;
            if (o == null || getClass() != o.getClass())
                return false;
            p pair = (p) o;
            return a == pair.a && b == pair.b && c == pair.c;
        }
 
        @Override
        public int hashCode() {
            return Objects.hash(a, b, c);
        }
    }
 
    static class node {
        long maxSum;
        long totSum;
        long pref;
        long suff;
 
        node(long maxSum, long totSum, long pref, long suff) {
            this.maxSum = maxSum;
            this.totSum = totSum;
            this.pref = pref;
            this.suff = suff;
        }
    }
 
    public static node merge(node left, node right) {
        node root = new node(0, 0, 0, 0);
        root.maxSum = Math.max(left.maxSum, Math.max(right.maxSum, left.suff + right.pref));
        root.totSum = left.totSum + right.totSum;
        root.pref = Math.max(left.pref, left.totSum + right.pref);
        root.suff = Math.max(right.suff, left.suff + right.totSum);
        return root;
    }
 
    public static void build(node[] seg, long[] x, int l, int r, int id) {
        if (l == r) {
            seg[id] = new node(x[l], x[l], x[l], x[l]);
            return;
        }
        int mid = l + (r - l) / 2;
        build(seg, x, l, mid, (2 * id) + 1);
        build(seg, x, mid + 1, r, (2 * id) + 2);
        seg[id] = merge(seg[(2 * id) + 1], seg[(2 * id) + 2]);
    }
 
    public static void update(node[] seg, long val, int tid, int l, int r, int id) {
        if (l == r) {
            seg[id] = new node(val, val, val, val);
            return;
        }
        int mid = l + (r - l) / 2;
        if (tid <= mid) {
            update(seg, val, tid, l, mid, (2 * id) + 1);
        } else {
            update(seg, val, tid, mid + 1, r, (2 * id) + 2);
        }
        seg[id] = merge(seg[(2 * id) + 1], seg[(2 * id) + 2]);
    }
 
    public static void solve(Reader sc, FastReader fs, PrintWriter w, StringBuilder sb) throws Exception {
        int n = sc.nextInt();
        int q = sc.nextInt();
        long[] x = new long[n];
        for (int i = 0; i < n; i++) {
            x[i] = sc.nextLong();
        }
        node[] seg = new node[4 * n];
        for (int i = 0; i < seg.length; i++) {
            seg[i] = new node(Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE);
        }
        build(seg, x, 0, n - 1, 0);
        for (int i = 0; i < q; i++) {
            int k = sc.nextInt() - 1;
            long u = sc.nextLong();
            update(seg, u, k, 0, n - 1, 0);
            // System.out.println(":> " +
            // seg[0].maxSum + " " + seg[0].totSum + " " + seg[0].pref + " " + seg[0].suff);
            sb.append(Math.max(seg[0].maxSum, 0) + "\n");
        }
    }
 
    public static void main(String[] args) throws Exception {
        Reader sc = new Reader();
        FastReader fs = new FastReader();
        PrintWriter w = new PrintWriter(System.out);
        StringBuilder sb = new StringBuilder();
        // long o = sc.nextLong();
        // while (o > 0) {
        solve(sc, fs, w, sb);
        // o--;
        // }
        System.out.print(sb.toString());
        w.close();
    }
}