  import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
 
    // lazy propagation
    public class entry_987938 {
        static int n, m;
        static long[] x;  // storing the prefix sums
        static final StdIn in = new StdIn();
        static final PrintWriter out = new PrintWriter(System.out);
        static Node[] st;
        static final long INF = 0x3f3f3f3f3f3f3f3fL;
 
        static class Node {
            long s, mxl, mxr, mx;
 
//            public Node(long s, long mxl, long mxr, long mx) {
//                this.s = s;
//                this.mxl = mxl;
//                this.mxr = mxr;
//                this.mx = mx;
//            }
        }
 
//        // apply
//        static void app(int i, long x, int l2, int r2) {
////            st[i].mn += x;
//            st[i].mx += x;
//            st[i].s = x;
//            st[i].mxl = x;
//            st[i].mxr = x;
//        }
//
//        // push
//        static void psh(int i, int l2, int m2, int r2) {
//            app(2 * i, st[i].lz, l2, m2);
//            app(2 * i + 1, st[i].lz, m2 + 1, r2);
//            st[i].lz = 0;
//        }
 
        /**
         *
         * @param l1 position (1 based) of the num we want to update/insert in the original array
         * @param x num we want to insert/update
         * @param i index where the range the range minimum will be stored in the segment tree array
         * @param l2 left pointer of orig array
         * @param r2 right pointer of orig array
         */
        static void upd(int l1, long x, int i, int l2, int r2) {
            if (l2 == r2) {
//                st[i].mn = x;
                st[i].mx = x;
                st[i].s = x;
                st[i].mxl = st[i].mxr = x;
                return;
            }
            int m2 = (l2 + r2) / 2;
            if (l1 <= m2)
                upd(l1, x, 2 * i, l2, m2);
            else
                upd(l1, x, 2 * i + 1, m2 + 1, r2);
//            st[i].mn = Math.min(st[2 * i].mn, st[2 * i + 1].mn);
            st[i].mx = Math.max(st[2 * i].mx, Math.max(st[2 * i + 1].mx, st[2 * i].mxr + st[2 * i + 1].mxl));
            st[i].mxl = Math.max(st[2 * i].mxl, st[2 * i].s + st[2 * i + 1].mxl);
            st[i].mxr = Math.max(st[2 * i + 1].mxr, st[2 * i + 1].s + st[2 * i].mxr);
            st[i].s = st[2 * i].s + st[2 * i + 1].s;
        }
 
        /**
         *
         * @param l1 lower bound of range
         * @param r1 upper bound of range
         * @param i index where the range the range minimum/sum will be stored in the segment tree array
         * @param l2 left pointer of orig array
         * @param r2 right pointer of orig array
         * @return range sum
         */
        static long qry(int l1, int r1, int i, int l2, int r2) {
            if (l1 <= l2 && r2 <= r1) {
                return st[i].mx;
            }
            int m2 = (l2 + r2) / 2;
//            psh(i, l2, m2, r2);  // push
    //        return Math.min(l1 <= m2 ? qry(l1, r1, 2 * i, l2, m2) : (int) 1e9,
    //                m2 < r1 ? qry(l1, r1, 2 * i + 1, m2 + 1, r2) : (int) 1e9);
//            return (l1 <= m2 ? qry(l1, r1, 2 * i, l2, m2) : 0)
//                    + (m2 < r1 ? qry(l1, r1, 2 * i + 1, m2 + 1, r2) : 0);
                    return Math.max(l1 <= m2 ? qry(l1, r1, 2 * i, l2, m2) : 0,
                            m2 < r1 ? qry(l1, r1, 2 * i + 1, m2 + 1, r2) : 0);
        }
 
        // do binary search on segment tree
        static long qry2(int x, int i, int l2, int r2) {
            if (l2 == r2)
                return l2;
            int m2 = (l2 + r2) / 2;
//            psh(i, l2, m2, r2);
            if (st[2 * i].mx >= x)
                return qry2(x, 2 * i, l2, m2);
            return qry2(x, 2 * i + 1, m2 + 1, r2);
        }
 
        public static void main(String[] args) {
            n = in.nextInt();
            m = in.nextInt();
            x = new long[n];
            st = new Node[1 << 19];  // n <= 2*10^5 == 200_000 --> 2^18 = 262_144 > 200_000
            for (int i = 0; i < st.length; i++) st[i] = new Node();
            for (int i = 0; i < n; i++) {
                x[i] = in.nextInt();
                upd(i, x[i], 1, 0, n - 1);
            }
            while (m-- > 0) {
                int k = in.nextInt() - 1;
                x[k] = in.nextInt();
                upd(k, x[k], 1, 0, n - 1);
                out.println(Math.max(st[1].mx, 0));
            }
            out.close();
        }
 
        private static class StdIn {
            final private int BUFFER_SIZE = 1 << 16;
            private final DataInputStream din;
            private final byte[] buffer;
            private int bufferPointer, bytesRead;
            public StdIn() {
                din = new DataInputStream(System.in);
                buffer = new byte[BUFFER_SIZE];
                bufferPointer = bytesRead = 0;
            }
            public StdIn(InputStream in) {
                try {
                    din = new DataInputStream(in);
                } catch(Exception e) {
                    throw new RuntimeException();
                }
                buffer = new byte[BUFFER_SIZE];
                bufferPointer = bytesRead = 0;
            }
            public String next() {
                int c;
                while((c=read())!=-1&&(c==' '||c=='\n'||c=='\r'));
                StringBuilder s = new StringBuilder();
                while (c != -1)
                {
                    if (c == ' ' || c == '\n'||c=='\r')
                        break;
                    s.append((char)c);
                    c=read();
                }
                return s.toString();
            }
            public String nextLine() {
                int c;
                while((c=read())!=-1&&(c==' '||c=='\n'||c=='\r'));
                StringBuilder s = new StringBuilder();
                while (c != -1)
                {
                    if (c == '\n'||c=='\r')
                        break;
                    s.append((char)c);
                    c = read();
                }
                return s.toString();
            }
            public int nextInt() {
                int ret = 0;
                byte c = read();
                while (c <= ' ')
                    c = read();
                boolean neg = (c == '-');
                if (neg)
                    c = read();
                do
                    ret = ret * 10 + c - '0';
                while ((c = read()) >= '0' && c <= '9');
 
                if (neg)
                    return -ret;
                return ret;
            }
            public int[] readIntArray(int n, int os) {
                int[] ar = new int[n];
                for(int i=0; i<n; ++i)
                    ar[i]=nextInt()+os;
                return ar;
            }
            public long nextLong() {
                long ret = 0;
                byte c = read();
                while (c <= ' ')
                    c = read();
                boolean neg = (c == '-');
                if (neg)
                    c = read();
                do
                    ret = ret * 10 + c - '0';
                while ((c = read()) >= '0' && c <= '9');
                if (neg)
                    return -ret;
                return ret;
            }
            public long[] readLongArray(int n, long os) {
                long[] ar = new long[n];
                for(int i=0; i<n; ++i)
                    ar[i]=nextLong()+os;
                return ar;
            }
            public double nextDouble() {
                double ret = 0, div = 1;
                byte c = read();
                while (c <= ' ')
                    c = read();
                boolean neg = (c == '-');
                if (neg)
                    c = read();
                do
                    ret = ret * 10 + c - '0';
                while ((c = read()) >= '0' && c <= '9');
                if (c == '.')
                    while ((c = read()) >= '0' && c <= '9')
                        ret += (c - '0') / (div *= 10);
                if (neg)
                    return -ret;
                return ret;
            }
            private void fillBuffer() throws IOException {
                bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
                if (bytesRead == -1)
                    buffer[0] = -1;
            }
            private byte read() {
                try{
                    if (bufferPointer == bytesRead)
                        fillBuffer();
                    return buffer[bufferPointer++];
                } catch(IOException e) {
                    throw new RuntimeException();
                }
            }
            public void close() throws IOException {
                if (din == null)
                    return;
                din.close();
            }
        }
    }