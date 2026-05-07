import java.io.*;
import java.util.*;
 
public class  entry_8923162 {
    static long[] solve(int[] A, int n, int[][] Q, int m) {
        var st = new SegmentTree(n); 
        for(var i = 0; i < n; i++) {
            st.update(i, A[i], i == n-1); 
        }
        var ans = new long[m];
        for(var j = 0; j < m; j++) {
            var q = Q[j];
            var i = q[0]; 
            var x = q[1];
            st.update(i, x, true);
            ans[j] = st.t[1][3];
            // System.out.println( Arrays.deepToString(st.t) );
        }
        return ans; 
    }
    public static void main(String[] args) throws Exception {
        var io = new FastIO(); 
        var n = io.nextInt(); 
        var m = io.nextInt(); 
        var A = io.nextIntArray(n); 
        var Q = io.nextIntArray(m, 2, new int[] {-1, 0}); 
        var ans = solve(A, n, Q, m); 
        io.println(ans, 0, '\n');
        io.close(); 
    }
    
    static class SegmentTree {
        static int VAL = 0, PFX = 1, SFX = 2, MAX = 3; 
        int n;
        long t[][];
 
        SegmentTree(int len) {
            this.n = (1 << (log2(len)+1)); 
            this.t = new long[2*n][4]; 
            for(var i = 0; i < 2*n; i++) {
                t[i][0] = t[i][PFX] = t[i][SFX] = t[i][MAX] = 0; 
            }
        }
        void update(int i, int x, boolean do_print) {
            // System.err.printf("update(i=%2d,x=%2d):%n", i, x);
            i += n; 
            t[i][VAL] = t[i][PFX] = t[i][SFX] = t[i][MAX] = x; 
            for(i /= 2; i > 0; i /= 2) {
                var l = 2*i; 
                var r = 2*i+1; 
                t[i][VAL] = t[l][VAL] + t[r][VAL]; 
                t[i][PFX] = max(t[l][PFX], t[l][VAL] + t[r][PFX]);
                t[i][SFX] = max(t[r][SFX], t[l][SFX] + t[r][VAL]); 
                t[i][MAX] = max(t[l][MAX], t[r][MAX], t[l][SFX] + t[r][PFX]); 
                // System.err.printf("\ti:%d\tt[i]:%s, \t", i, Arrays.toString(t[i]));
            }
            // if(do_print) {
            //     var rows = new LinkedList<String>();
            //     for(int start = n, size = n; true; start /= 2, size /= 2) {
            //         var row = new StringBuffer();
            //         for(var j = start; j < start+size; j++) {
            //             row.append( String.format("%d, ", t[j][0]) );
            //         }
            //         rows.addFirst( row.toString() );
            //         if(start == 0) {
            //             for(var _row: rows) {
            //                 System.err.printf("%s%n", _row);
            //             }
            //             break; 
            //         }
            //     }
            //     System.err.printf("%n~~~~~~%n");
            // }
        }
        long query(int l, int r) {
            l += n; 
            r += n; 
            long ans = 0; 
            while(l < r) {
                if(l % 2 == 1) { ans = max(ans, t[l++][MAX]); }
                if(r % 2 == 1) { ans = max(ans, t[--r][MAX]); }
                l /= 2;
                r /= 2;
            }
            return ans; 
        }
    }
 
    static long max(long a, long b) { return Math.max(a,b); }
    static long max(long a, long b, long c) { return Math.max(a, Math.max(b,c)); }
    static int log2(int a) { return 31 - Integer.numberOfLeadingZeros(a); }
    static class FastIO extends PrintWriter {
        private InputStream stream;
        private byte[] buf = new byte[1 << 16];
        private int curChar;
        private int numChars;
    
        public FastIO() { // standard input
            this(System.in, System.out); 
        }
        public FastIO(InputStream i, OutputStream o) {
            super(o);
            stream = i;
        }
        public FastIO(String i, String o) throws IOException { // file input
            super(new FileWriter(o));
            stream = new FileInputStream(i);
        }
        private boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
        private int nextByte() { // throws InputMismatchException() if previously detected end of file
            if (numChars == -1) { 
                throw new InputMismatchException(); 
            }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) { 
                    throw new InputMismatchException(); 
                }
                if (numChars == -1) {
                    return -1;  // end of file
                }
            }
            return buf[curChar++];
        }
        public char nextChar() {
            int c = nextByte();
            return (char) c; 
        }
        public String nextString() {
            int c;
            do { 
                c = nextByte(); 
            } while (c <= ' ');
            var res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = nextByte();
            } while (c > ' ');
            return res.toString();
        }
        public String nextLine() {
            int c;
            do { 
                c = nextByte(); 
            } while (c <= '\n');
            var res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = nextByte();
            } while (c > '\n');
            return res.toString();
        }
        public int nextInt() {  
            int c;
            do { 
                c = nextByte(); 
            } while (c <= ' ');
            var sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = nextByte();
            }
            var res = 0;
            do {
                if(c < '0' || c > '9') { 
                    throw new InputMismatchException(); 
                }
                res = 10 * res + c - '0';
                c = nextByte();
            } while (c > ' ');
            return res * sgn;
        }
        public long nextLong() throws IOException {
            long ret = 0;
            int c = nextByte();
            while (c <= ' ') {
                c = nextByte();
            }
            boolean neg = (c == '-');
            if (neg) {
                c = nextByte();
            }
            do {
                ret = ret * 10 + c - '0';
            } while ((c = nextByte()) >= '0' && c <= '9');
            if (neg) {
                return -ret;
            }
            return ret;
        }
        public double nextDouble() {
            int c = nextByte();
            while (isSpaceChar(c)) {
                c = nextByte();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = nextByte();
            }
            double res = 0;
            while (!isSpaceChar(c) && c != '.') {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res *= 10;
                res += c - '0';
                c = nextByte();
            }
            if (c == '.') {
                c = nextByte();
                double m = 1;
                while (!isSpaceChar(c)) {
                    if (c < '0' || c > '9') {
                        throw new InputMismatchException();
                    }
                    m /= 10;
                    res += (c - '0') * m;
                    c = nextByte();
                }
            }
            return res * sgn;
        }
        public int[] nextIntArray(int n)                              { return nextIntArray(n, 0); }
        public int[] nextIntArray(int n, int offset) {
            var ans = new int[n]; 
            for(var i = 0; i < n; i++) {
                ans[i] = nextInt() + offset; 
            }
            return ans;
        }
        public int[][] nextIntArray(int n, int m, int[] offset) {
            var ans = new int[n][m]; 
            for(var i = 0; i < n; i++) {
                for(var j = 0; j < m; j++) {
                    ans[i][j] = nextInt() + offset[j]; 
                }
            }
            return ans;
        }
        public void println(int[] A, char separator)                 { println(A, 0, separator);  }
        public void println(int[] A, int offset, char separator) {
            var sb = new StringBuffer(); 
            for(var a: A) {
                sb.append( a+offset ).append(separator); 
            }
            println(sb); 
        }
        public void println(int[][] A)                               { println(A, 0, ' ', '\n'); }
        public void println(int[][] A, int offset)                   { println(A, offset, ' ', '\n'); }
        public void println(int[][] A, int offset, char separator)   { println(A, offset, separator, '\n'); }
        public void println(int[][] A, int[] offset)                 { println(A, offset, ' ', '\n'); }
        public void println(int[][] A, int[] offset, char separator) { println(A, offset, separator, '\n');  }
        public void println(int[][] A, int offset, char separator1, char separator2) {
            var sb = new StringBuffer(); 
            for(var row: A) {
                for(var cell:  row) {
                    sb.append( cell+offset ).append(separator1); 
                }
                sb.append(separator2); 
            }
            println(sb);
        }
        public void println(int[][] A, int[] offset, char separator1, char separator2) {
            var sb = new StringBuffer(); 
            for(var y = 0; y < A.length; y++) {
                for(var x = 0; x < A[y].length; x++) {
                    var a = A[y][x] + offset[x];
                    sb.append(a).append(separator1); 
                }
                sb.append(separator2); 
            }
            println(sb);
        }
        public void println(long[] A, char separator)                { println(A, 0, separator); }
        public void println(long[] A, long offset, char separator) {
            var sb = new StringBuffer(); 
            for(var a: A) {
                sb.append( a+offset ).append(separator);
            }
            println(sb); 
        }
        public void println(String[] A, char separator) {
            var sb = new StringBuffer(); 
            for(var a: A) {
                sb.append(a).append(separator);
            }
            println(sb); 
        }
        private void println(boolean[] A, char deny, char affirm, char separator) {
            var sb = new StringBuffer(); 
            for(var b: A) {
                sb.append( !b ? deny : affirm ).append(separator); 
            }
            println(sb); 
        }
        private void println(boolean[] A, String deny, String affirm, char separator) {
            var sb = new StringBuffer(); 
            for(var b: A) {
                sb.append( !b ? deny : affirm ).append(separator); 
            }
            println(sb); 
        }
    }
}