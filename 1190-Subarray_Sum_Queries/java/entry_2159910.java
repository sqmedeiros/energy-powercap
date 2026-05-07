// package RangeQueries;
 
import java.io.*;
import java.util.*;
 
public class  entry_2159910 {
 
    public static void main(String[] args) throws IOException {
        Reader rd = new Reader();
        PrintWriter pw = new PrintWriter(System.out);
 
        int n = rd.nextInt();
        int q = rd.nextInt();
        long[] nums = new long[n];
        for (int i = 0; i < n; i++) {
            nums[i] = rd.nextInt();
        }
        segtree sgt = new segtree(nums, 0, nums.length - 1);
        for (int i = 0; i < q; i++) {
            pw.println(Math.max(0, sgt.update(
                    rd.nextInt() - 1,
                    rd.nextInt(),
                    0, nums.length - 1
            )));
        }
 
        pw.close();
    }
 
    static class segtree {
 
        public segtree left;
        public segtree right;
        public long suf;
        public long pref;
        public long best;
        public long sum;
 
        public segtree(long[] nums, int l, int r) {
            if (l == r) {
                suf = pref = best = sum = nums[l];
                return;
            }
            left = new segtree(nums, l, (l + r) / 2);
            right = new segtree(nums, (l + r) / 2 + 1, r);
            comb(left, right);
        }
 
        public long update(int idx, int up, int l, int r) {
            if (l == r) {
                suf = pref = best = sum = up;
            } else {
                if (idx <= (l + r) / 2) {
                    left.update(idx, up, l, (l + r) / 2);
                } else {
                    right.update(idx, up, (l + r) / 2 + 1, r);
                }
                comb(left, right);
            }
            return best;
        }
 
        private void comb(segtree a, segtree b) { //associative
            sum = a.sum + b.sum;
            pref = Math.max(a.sum + b.pref, a.pref);
            suf = Math.max(b.sum + a.suf, b.suf);
            best = Math.max(a.best, Math.max(b.best, a.suf + b.pref));
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
            din = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public String readLine() throws IOException {
            byte[] buf = new byte[64]; // line length 
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n') {
                    break;
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
            if (neg) {
                c = read();
            }
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
 
            if (neg) {
                return -ret;
            }
            return ret;
        }
 
        public long nextLong() throws IOException {
            long ret = 0;
            byte c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean neg = (c == '-');
            if (neg) {
                c = read();
            }
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg) {
                return -ret;
            }
            return ret;
        }
 
        public double nextDouble() throws IOException {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean neg = (c == '-');
            if (neg) {
                c = read();
            }
 
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
 
            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }
 
            if (neg) {
                return -ret;
            }
            return ret;
        }
 
        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
            if (bytesRead == -1) {
                buffer[0] = -1;
            }
        }
 
        private byte read() throws IOException {
            if (bufferPointer == bytesRead) {
                fillBuffer();
            }
            return buffer[bufferPointer++];
        }
 
        public void close() throws IOException {
            if (din == null) {
                return;
            }
            din.close();
        }
    }
}