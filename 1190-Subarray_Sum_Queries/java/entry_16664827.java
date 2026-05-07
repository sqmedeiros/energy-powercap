import java.io.*;
 
public class  entry_16664827 {
 
    static long[] seg, maxVal, prefixSum, suffixSum;
 
    static void build(int idx, int left, int right, long[] arr) {
        if (left == right) {
            seg[idx] = maxVal[idx] = prefixSum[idx] = suffixSum[idx] = arr[left];
            return;
        }
 
        int mid = (left + right) >>> 1;
        int l = 2 * idx + 1, r = 2 * idx + 2;
 
        build(l, left, mid, arr);
        build(r, mid + 1, right, arr);
 
        seg[idx] = seg[l] + seg[r];
        prefixSum[idx] = Math.max(prefixSum[l], seg[l] + prefixSum[r]);
        suffixSum[idx] = Math.max(suffixSum[r], seg[r] + suffixSum[l]);
        maxVal[idx] = Math.max(maxVal[l], Math.max(maxVal[r], suffixSum[l] + prefixSum[r]));
    }
 
    static void update(int idx, int left, int right, int pos, long val) {
        if (left == right) {
            seg[idx] = maxVal[idx] = prefixSum[idx] = suffixSum[idx] = val;
            return;
        }
 
        int mid = (left + right) >>> 1;
        int l = 2 * idx + 1, r = 2 * idx + 2;
 
        if (pos <= mid) update(l, left, mid, pos, val);
        else update(r, mid + 1, right, pos, val);
 
        seg[idx] = seg[l] + seg[r];
        prefixSum[idx] = Math.max(prefixSum[l], seg[l] + prefixSum[r]);
        suffixSum[idx] = Math.max(suffixSum[r], seg[r] + suffixSum[l]);
        maxVal[idx] = Math.max(maxVal[l], Math.max(maxVal[r], suffixSum[l] + prefixSum[r]));
    }
 
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        int n = fs.nextInt();
        int q = fs.nextInt();
 
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) arr[i] = fs.nextLong();
 
        seg = new long[4 * n];
        maxVal = new long[4 * n];
        prefixSum = new long[4 * n];
        suffixSum = new long[4 * n];
 
        build(0, 0, n - 1, arr);
 
        StringBuilder sb = new StringBuilder();
 
        while (q-- > 0) {
            int i = fs.nextInt() - 1;
            long val = fs.nextLong();
 
            update(0, 0, n - 1, i, val);
            sb.append(Math.max(0, maxVal[0])).append('\n');
        }
 
        System.out.print(sb);
    }
 
    // ⚡ FAST SCANNER
    static class FastScanner {
        private final InputStream in = System.in;
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
 
        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }
 
        int nextInt() throws IOException {
            int c, sign = 1, val = 0;
            while ((c = read()) <= ' ') if (c == -1) return -1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }
 
        long nextLong() throws IOException {
            int c, sign = 1;
            long val = 0;
            while ((c = read()) <= ' ') if (c == -1) return -1;
            if (c == '-') {
                sign = -1;
                c = read();
            }
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }
    }
}