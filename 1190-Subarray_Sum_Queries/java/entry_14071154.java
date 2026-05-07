import java.io.*;
import java.util.*;
 
public class  entry_14071154 {
 
    static class SegmentTree {
        int size;
        long[] pref, suff, sum, best;
 
        SegmentTree(int n) {
            size = 1;
            while (size < n) size <<= 1;
            pref = new long[2 * size];
            suff = new long[2 * size];
            sum = new long[2 * size];
            best = new long[2 * size];
        }
 
        void build(int[] arr) {
            for (int i = 0; i < arr.length; i++) {
                long v = arr[i];
                sum[size + i] = v;
                if (v > 0) {
                    pref[size + i] = v;
                    suff[size + i] = v;
                    best[size + i] = v;
                }
            }
            for (int i = size - 1; i >= 1; i--) pull(i);
        }
 
        void pull(int x) {
            int l = x << 1, r = l | 1;
            sum[x] = sum[l] + sum[r];
            pref[x] = Math.max(pref[l], sum[l] + pref[r]);
            suff[x] = Math.max(suff[r], sum[r] + suff[l]);
            best[x] = Math.max(Math.max(best[l], best[r]), suff[l] + pref[r]);
        }
 
        void set(int idx, int val) {
            int pos = size + idx;
            sum[pos] = val;
            if (val > 0) {
                pref[pos] = val;
                suff[pos] = val;
                best[pos] = val;
            } else {
                pref[pos] = 0;
                suff[pos] = 0;
                best[pos] = 0;
            }
            pos >>= 1;
            while (pos >= 1) {
                pull(pos);
                pos >>= 1;
            }
        }
 
        long getBest() {
            return best[1];
        }
    }
 
    public static void main(String[] args) throws IOException {
        FastScanner fs = new FastScanner(System.in);
        StringBuilder sb = new StringBuilder();
 
        int n = fs.nextInt();
        int m = fs.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = fs.nextInt();
 
        SegmentTree st = new SegmentTree(n);
        st.build(nums);
 
        for (int i = 0; i < m; i++) {
            int k = fs.nextInt() - 1;
            int x = fs.nextInt();
            st.set(k, x);
            sb.append(st.getBest()).append('\n');
        }
 
        System.out.print(sb);
    }
 
    // Very fast scanner
    static class FastScanner {
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
        private final InputStream in;
        FastScanner(InputStream in) { this.in = in; }
        private int readByte() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }
        int nextInt() throws IOException {
            int c, sign = 1, val = 0;
            do { c = readByte(); } while (c <= ' ');
            if (c == '-') { sign = -1; c = readByte(); }
            while (c > ' ') {
                val = val * 10 + c - '0';
                c = readByte();
            }
            return val * sign;
        }
    }
}