/**
 * author: derrick20
 * created: 8/22/21 5:06 PM
 */
 
import java.io.*;
import java.util.*;
 
import static java.lang.Math.*;
 
public class entry_2732592 {
    static FastScanner sc = new FastScanner();
    static PrintWriter out = new PrintWriter(System.out);
 
    public static void main(String[] args) {
        int N = sc.nextInt();
        int Q = sc.nextInt();
        long[] init = new long[N];
        Arrays.setAll(init, i -> sc.nextLong());
        SegmentTree st = new SegmentTree(init);
        while (Q-->0) {
            int i = sc.nextInt() - 1;
            long value = sc.nextLong();
            st.update(i, value);
            long maxSum = st.query(0, N - 1);
            out.println(maxSum);
        }
        out.close();
    }
 
    static class Node {
        long prefix, suffix, sum, maxSum;
 
        public Node() {}
 
        public Node(long prefix, long suffix, long sum, long maxSum) {
            this.prefix = prefix;
            this.suffix = suffix;
            this.sum = sum;
            this.maxSum = maxSum;
        }
    }
 
    static class SegmentTree {
        Node[] tree;
        int N;
        public SegmentTree(long[] init) {
            N = init.length;
            tree = new Node[2 * N];
            for (int i = 2 * N - 1; i >= 1; i--) {
                if (i >= N) {
                    tree[i] = makeSingleNode(init[i - N]);
                } else {
                    tree[i] = combine(tree[i << 1], tree[i << 1 | 1]);
                }
            }
        }
 
        Node makeSingleNode(long amt) {
            long selected = max(0, amt);
            return new Node(selected, selected, amt, selected);
        }
 
        long query(int l, int r) {
            Node left = new Node(), right = new Node();
            for (l += N, r += N; l <= r; l >>= 1, r >>= 1) {
                if ((l & 1) > 0) left = combine(left, tree[l++]);
                if ((r & 1) == 0) right = combine(tree[r--], right);
            }
            Node full = combine(left, right);
            return full.maxSum;
        }
 
        void update(int i, long value) {
            tree[i += N] = makeSingleNode(value);
            for (i >>= 1; i >= 1; i >>= 1) {
                tree[i] = combine(tree[i << 1], tree[i << 1 | 1]);
            }
        }
 
        Node combine(Node left, Node right) {
            Node res = new Node();
            res.prefix = max(left.prefix, left.sum + right.prefix);
            res.suffix = max(left.suffix + right.sum, right.suffix);
            res.sum = left.sum + right.sum;
            res.maxSum = max(max(left.maxSum, right.maxSum), left.suffix + right.prefix);
            return res;
        }
    }
 
    static class FastScanner {
        private int BS = 1 << 16;
        private char NC = (char) 0;
        private byte[] buf = new byte[BS];
        private int bId = 0, size = 0;
        private char c = NC;
        private double cnt = 1;
        private BufferedInputStream in;
 
        public FastScanner() {
            in = new BufferedInputStream(System.in, BS);
        }
 
        public FastScanner(String s) {
            try {
                in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
            } catch (Exception e) {
                in = new BufferedInputStream(System.in, BS);
            }
        }
 
        char getChar() {
            while (bId == size) {
                try {
                    size = in.read(buf);
                } catch (Exception e) {
                    return NC;
                }
                if (size == -1) return NC;
                bId = 0;
            }
            return (char) buf[bId++];
        }
 
        int nextInt() {
            return (int) nextLong();
        }
 
        long nextLong() {
            cnt = 1;
            boolean neg = false;
            if (c == NC) c = getChar();
            for (; (c < '0' || c > '9'); c = getChar()) {
                if (c == '-') neg = true;
            }
            long res = 0;
            for (; c >= '0' && c <= '9'; c = getChar()) {
                res = (res << 3) + (res << 1) + c - '0';
                cnt *= 10;
            }
            return neg ? -res : res;
        }
 
        double nextDouble() {
            boolean neg = false;
            if (c == NC) c = getChar();
            for (; (c < '0' || c > '9'); c = getChar()) {
                if (c == '-') neg = true;
            }
            double cur = nextLong();
            if (c != '.') {
                return neg ? -cur : cur;
            } else {
                double frac = nextLong() / cnt;
                return neg ? -cur - frac : cur + frac;
            }
        }
 
        String next() {
            StringBuilder res = new StringBuilder();
            while (c <= 32) c = getChar();
            while (c > 32) {
                res.append(c);
                c = getChar();
            }
            return res.toString();
        }
 
        String nextLine() {
            StringBuilder res = new StringBuilder();
            while (c <= 32) c = getChar();
            while (c != '\n') {
                res.append(c);
                c = getChar();
            }
            return res.toString();
        }
 
        boolean hasNext() {
            if (c > 32) return true;
            while (true) {
                c = getChar();
                if (c == NC) return false;
                else if (c > 32) return true;
            }
        }
    }
 
    static void ASSERT(boolean assertion, String message) {
        if (!assertion) throw new AssertionError(message);
    }
 
    static void ASSERT(boolean assertion) {
        if (!assertion) throw new AssertionError();
    }
}