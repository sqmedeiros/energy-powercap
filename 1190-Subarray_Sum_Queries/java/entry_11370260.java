import java.io.*;
 
public class entry_11370260 {
 
    static InputReader sc;
    static int n;
    static long[] arr;
 
    public static void main(String[] args) throws IOException {
        sc = new InputReader();
        n = sc.nextInt();
        int q = sc.nextInt();
        arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLong();
        }
        SegmentTree st = new SegmentTree();
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < q; i++) {
 
            int idx = sc.nextInt();
            long val = sc.nextLong();
            st.update(idx - 1, val);
 
            res.append(st.get(0, n - 1)).append("\n");
 
        }
        System.out.println(res.toString());
    }
 
    static final class SegmentTree {
        Node[] nodes;
 
        public SegmentTree() {
            nodes = new Node[4 * n];
            build(1, 0, n - 1);
        }
 
        void build(int idx, int l, int r) {
            if (l == r) {
                nodes[idx] = new Node(arr[l]);
                return;
            }
 
            int m = (l + r) / 2;
            build(2 * idx, l, m);
            build(2 * idx + 1, m + 1, r);
            nodes[idx] = Node.merge(nodes[2 * idx], nodes[2 * idx + 1]);
        }
 
        void update(int idx, long val) {
            updateCore(1, 0, n - 1, idx, val);
        }
 
        void updateCore(int node, int l, int r, int idx, long val) {
            if (l == r) {
                arr[idx] = val;
                nodes[node] = new Node(val);
                return;
            }
            int m = (l + r) / 2;
            if (idx <= m) {
                updateCore(2 * node, l, m, idx, val);
            } else {
                updateCore(2 * node + 1, m + 1, r, idx, val);
            }
            nodes[node] = Node.merge(nodes[2 * node], nodes[2 * node + 1]);
        }
 
        long get(long from, long to) {
            return getCore(1, 0, n - 1, from, to).maxSum;
        }
 
        Node getCore(int node, int l, int r, long from, long to) {
            if (l >= from && r <= to)
                return nodes[node];
            if (r < from || l > to)
                return new Node(0);
            int m = (l + r) / 2;
            Node maxSumLeft = getCore(2 * node, l, m, from, to);
            Node maxSumRight = getCore(2 * node + 1, m + 1, r, from, to);
            // if (maxSumLeft == null)
            // return maxSumRight;
            // if (maxSumRight == null)
            // return maxSumLeft;
            return Node.merge(maxSumLeft, maxSumRight);
        }
    }
 
    static class Node {
        long prefix;
        long suffix;
        long totalSum;
        long maxSum;
 
        Node(long val) {
            prefix = val;
            suffix = val;
            totalSum = val;
            maxSum = Math.max(val, 0);
        }
 
        static Node merge(Node a, Node b) {
            Node parent = new Node(0);
            parent.totalSum = a.totalSum + b.totalSum;
            parent.prefix = Math.max(a.prefix, a.totalSum + b.prefix);
            parent.suffix = Math.max(b.suffix, b.totalSum + a.suffix);
            parent.maxSum = Math.max(Math.max(a.maxSum, b.maxSum), a.suffix + b.prefix);
            return parent;
        }
    }
 
    static class InputReader {
        private int BUFFER_SIZE = 1 << 16;
        private byte[] buffer = new byte[BUFFER_SIZE];
        private int bufferPointer = 0,
                bytesRead = 0;
        private InputStream rd;
 
        public InputReader() {
            this.rd = System.in;
        }
 
        private int read() throws IOException {
            if (bufferPointer == bytesRead) {
                bufferPointer = 0;
                bytesRead = rd.read(buffer, bufferPointer, BUFFER_SIZE);
                if (bytesRead == -1) {
                    return -1;
                }
            }
            return buffer[bufferPointer++];
        }
 
        public String nextLine() throws IOException {
            StringBuilder line = new StringBuilder();
            int c = read();
            while (c == '\n' || c == '\r') {
                c = read();
            }
            while (c != '\n' && c != '\r' && c != -1) {
                line.append((char) c);
                c = read();
            }
            return line.toString();
        }
 
        public int nextInt() throws IOException {
            int number = 0;
            int c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean negative = (c == '-');
            if (negative) {
                c = read();
            }
            do {
                number = number * 10 + (c - '0');
                c = read();
            } while (c >= '0' && c <= '9');
            return negative ? -number : number;
        }
 
        public long nextLong() throws IOException {
            long number = 0L;
            int c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean negative = (c == '-');
            if (negative) {
                c = read();
            }
            do {
                number = number * 10 + (c - '0');
                c = read();
            } while (c >= '0' && c <= '9');
            return negative ? -number : number;
        }
 
        public String next() throws IOException {
            int c = read();
            while (c <= ' ') {
                c = read();
            }
            StringBuilder t = new StringBuilder();
            do {
                t.append((char) c);
                c = read();
            } while (c > ' ');
            return t.toString();
        }
 
        public double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }
 
        public char nextChar() throws IOException {
            int c = read();
            while (c <= ' ') {
                c = read();
            }
            return (char) c;
        }
    }
}