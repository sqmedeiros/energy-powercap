import java.lang.*;
import java.io.*;
import java.util.*;
public class entry_12676411 {
    public static void main(String[] args) throws Exception {
        Reader br = new Reader();
        PrintWriter pw = new PrintWriter(System.out);
        int n = br.nextInt(), q = br.nextInt();
       
        int[] index = new int[n];
        int len = build(index, 1, n, 1);
        long[][] st = new long[1 + len][4];
        for (int i = 0; i < n; ++i) set(st, index[i], br.nextInt());
        while (0 < q--) {
            set(st, index[br.nextInt() - 1], br.nextInt());
            pw.println(st[1][3]);
        }
        pw.close();
    }
    private static int build(int[] index, int i, int j, int k) {
        if (i == j) {
            return index[i - 1] = k;
        } else {
            int m = i + ((j - i) >> 1);
            return Math.max(build(index, i, m, k << 1), build(index, m + 1, j, (k << 1) + 1));
        }
    }
    private static void set(long[][] st, int i, int val) {
        st[i][0] = st[i][1] = st[i][3] = Math.max(0, val);
        st[i][2] = val;
        for (int j = i >> 1; 1 <= j; j >>= 1) {
            if (st.length <= 1 + (j << 1)) {
                st[j][0] = st[j << 1][0];
                st[j][1] = st[j << 1][1];
                st[j][2] = st[j << 1][2];
                st[j][3] = st[j << 1][3];
            } else {
                st[j][0] = Math.max(st[j << 1][0], st[j << 1][2] + st[(j << 1) + 1][0]);
                st[j][1] = Math.max(st[1 + (j << 1)][1], st[1 + (j << 1)][2] + st[j << 1][1]);
                st[j][2] = st[j << 1][2] + st[1 + (j << 1)][2];
                st[j][3] = Math.max(st[j << 1][1] + st[1 + (j << 1)][0], Math.max(st[j << 1][3], st[1 + (j << 1)][3]));
            }
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
        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
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
        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do
            {
                ret = ret * 10 + c - '0';
            }  while ((c = read()) >= '0' && c <= '9');
 
            if (neg)
                return -ret;
            return ret;
        }
    }
}