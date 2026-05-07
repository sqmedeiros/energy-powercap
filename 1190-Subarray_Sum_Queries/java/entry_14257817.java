// package segmentTree;
 
import java.io.*; 
 
public class entry_14257817 {
    static long arr[]; 
    static Node seg[]; 
 
    public static void main(String args[]) throws IOException {
        FastScanner fs = new FastScanner(); 
 
        int n = fs.nextInt(), m = fs.nextInt(); 
        arr = new long[n]; 
        
        for(int i = 0; i < n; i ++) {
            arr[i] = fs.nextInt(); 
        }
 
        seg = new Node[4 * n]; 
        build(0, 0, n - 1);
 
        StringBuilder ans = new StringBuilder(); 
 
        for(int i = 0; i < m; i ++) {
            int k = fs.nextInt() - 1, x = fs.nextInt(); 
            update(0, 0, n - 1, k, x); 
            ans.append(Math.max(seg[0].maxSum, 0)).append(" "); 
        }
 
        System.out.println(ans);
 
    }
 
    static void update(int node, int l, int r, int ind, long val) {
        if(l == r) {
            seg[node] = new Node(val, val, val, val);
            return; 
        }
 
        int mid = l + (r - l) / 2; 
 
        if(ind <= mid) {
            update(2 * node + 1, l, mid, ind, val); 
        }
        else {
            update(2 * node + 2, mid + 1, r, ind, val); 
        }
 
        Node left = seg[2 * node + 1], right = seg[2 * node + 2]; 
 
        long maxSum = Math.max(Math.max(left.maxSum, right.maxSum), left.suffix + right.prefix); 
        long totalSum = left.totalSum + right.totalSum; 
        long prefix = Math.max(left.prefix, left.totalSum + right.prefix); 
        long suffix = Math.max(right.suffix, right.totalSum + left.suffix); 
 
        seg[node] = new Node(maxSum, totalSum, prefix, suffix); 
        
    }
 
    static void build(int node, int l, int r) {
        if(l == r) {
            seg[node] = new Node(arr[l], arr[l], arr[l], arr[l]);  
            return; 
        }
 
        int mid = l + (r - l) / 2; 
 
        build(2 * node + 1, l, mid);
        build(2 * node + 2, mid + 1, r); 
 
        Node left = seg[2 * node + 1], right = seg[2 * node + 2]; 
 
        long maxSum = Math.max(Math.max(left.maxSum, right.maxSum), left.suffix + right.prefix); 
        long totalSum = left.totalSum + right.totalSum; 
        long prefix = Math.max(left.prefix, left.totalSum + right.prefix); 
        long suffix = Math.max(right.suffix, right.totalSum + left.suffix); 
 
        seg[node] = new Node(maxSum, totalSum, prefix, suffix); 
 
    }
 
    static class Node {
        long maxSum, totalSum, prefix, suffix; 
        public Node(long maxSum, long totalSum, long prefix, long suffix) {
            this.maxSum = maxSum; 
            this.totalSum = totalSum; 
            this.prefix = prefix; 
            this.suffix = suffix; 
        }
    }
 
    static class FastScanner {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
    
        public FastScanner() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
    
        private byte read() throws IOException {
            if (bufferPointer == bytesRead) {
                bytesRead = din.read(buffer, 0, BUFFER_SIZE);
                if (bytesRead == -1) {
                    buffer[0] = -1;
                }
                bufferPointer = 0;
            }
            return buffer[bufferPointer++];
        }
    
        public String next() throws IOException {
            byte c;
            do {
                c = read();
            } while (c <= ' ');
            StringBuilder sb = new StringBuilder();
            do {
                sb.append((char) c);
                c = read();
            } while (c > ' ');
            return sb.toString();
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
            return neg ? -ret : ret;
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
            return neg ? -ret : ret;
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
            return neg ? -ret : ret;
        }
    
        public String nextLine() throws IOException {
            byte c = read();
            while (c == '\n' || c == '\r') {
                c = read();
            }
            StringBuilder sb = new StringBuilder();
            do {
                sb.append((char) c);
                c = read();
            } while (c != '\n' && c != '\r');
            return sb.toString();
        }
    }
}