import java.io.*;
import java.util.*;
public class entry_5587952 {
    public static void main(String[] args) throws Exception {
        Reader io = new Reader();
        int N = io.nextInt();
        int Q = io.nextInt();
        int[] x = new int[N+1];
        for (int i = 1; i <= N; i++) {
            x[i] = io.nextInt();
        }
        SegmentTree tree = new SegmentTree(x);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            int index = io.nextInt();
            int newValue = io.nextInt();
            tree.update(index, newValue);
            sb.append(tree.maxSubarraySum()).append('\n');
        }
        io.print(sb);
        io.closeAll();
    }
    static class SegmentTree {
        private Node[] t;
        private int[] nums;
        private int size, N;
        public SegmentTree(int[] nums) {
            this.nums = Arrays.copyOf(nums, nums.length);
            N = nums.length-1;
            //The max size of this array is about 2 * 2 ^ log2(n) + 1
            size = (int) (2 * Math.pow(2.0, Math.floor((Math.log((double) N) / Math.log(2.0)) + 1)));
            t = new Node[size];
            build(1, 1, N);
        }
        public int size() {
            return N;
        }
        private void build(int v, int from, int to) {
            t[v] = new Node();
            t[v].from = from;
            t[v].to = to;
            if (from == to) {
                t[v].sum = nums[from];
                t[v].maxPrefixSum = t[v].maxSuffixSum = t[v].maxSubarraySum = nums[from];
            } else {
                int mid = (from+to)/2;
                build(2*v, from, mid);
                build(2*v+1, mid+1, to);
                t[v].sum = t[2*v].sum + t[2*v+1].sum;
                t[v].maxPrefixSum = Math.max(t[2*v].maxPrefixSum, t[2*v].sum+t[2*v+1].maxPrefixSum);
                t[v].maxSuffixSum = Math.max(t[2*v+1].maxSuffixSum, t[2*v+1].sum+t[2*v].maxSuffixSum);
                t[v].maxSubarraySum = Math.max(t[2*v].maxSubarraySum, t[2*v+1].maxSubarraySum);
                t[v].maxSubarraySum = Math.max(t[v].maxSubarraySum, t[2*v].maxSuffixSum+t[2*v+1].maxPrefixSum);
            }
        }
        public void update(int index, int value) {
            update(1, index, index, value);
        }
        public void update(int from, int to, int value) {
            update(1, from, to, value);
        }
        private void update(int v, int from, int to, int value) {
            Node n = t[v];
            if (contains(from, to, n.from, n.to)) {
                change(n, value);
            }
            if (n.size() == 1) return;
            if (intersects(from, to, n.from, n.to)) {
                propagate(v);
                update(2*v, from, to, value);
                update(2*v+1, from, to, value);
                t[v].sum = t[2*v].sum + t[2*v+1].sum;
                t[v].maxPrefixSum = Math.max(t[2*v].maxPrefixSum, t[2*v].sum+t[2*v+1].maxPrefixSum);
                t[v].maxSuffixSum = Math.max(t[2*v+1].maxSuffixSum, t[2*v+1].sum+t[2*v].maxSuffixSum);
                t[v].maxSubarraySum = Math.max(t[2*v].maxSubarraySum, t[2*v+1].maxSubarraySum);
                t[v].maxSubarraySum = Math.max(t[v].maxSubarraySum, t[2*v].maxSuffixSum+t[2*v+1].maxPrefixSum);
            }
        }
        private void propagate(int v) {
            Node n = t[v];
            if (n.pendingVal != null) {
                change(t[2*v], n.pendingVal);
                change(t[2*v+1], n.pendingVal);
                n.pendingVal = null; //unset the pending propagation value
            }
        }
        private void change(Node n, int value) {
            n.pendingVal = value;
            n.sum = n.size()*value;
            n.maxPrefixSum = n.maxSuffixSum = n.maxSubarraySum = value;
            nums[n.from] = value;
        }
        public long maxSubarraySum() {
            // 0 represents empty subarray
            return Math.max(0, maxSubarraySum(1, N));
        }
        public long maxSubarraySum(int from, int to) {
            return maxSubarraySum(1, from, to);
        }
        private long maxSubarraySum(int v, int from, int to) {
            if (t[v].pendingVal != null && contains(t[v].from, t[v].to, from, to)) {
                return (to - from + 1) * t[v].pendingVal;
            }
            if (contains(from, to, t[v].from, t[v].to)) {
                return t[v].maxSubarraySum;
            }
            if (intersects(from, to, t[v].from, t[v].to)) {
                propagate(v);
                t[v].maxSubarraySum = Math.max(t[2*v].maxSubarraySum, t[2*v+1].maxSubarraySum);
                t[v].maxSubarraySum = Math.max(t[v].maxSubarraySum, t[2*v].maxSuffixSum+t[2*v+1].maxPrefixSum);
            }
            return 0;
        }
        private boolean contains(int from1, int to1, int from2, int to2) {
            return from2 >= from1 && to2 <= to1;
        }
        private boolean intersects(int from1, int to1, int from2, int to2) {
            return from1 <= from2 && from2 <= to1 || from2 <= from1 && from1 <= to2; 
        }
        public String toString(){
            return Arrays.toString(t);
        }
        static class Node {
            long sum, maxSubarraySum, maxPrefixSum, maxSuffixSum;
            //Here We store the value that will be propagated lazily
            Integer pendingVal = null;
            int from, to;
            int size() {
                return to - from + 1;
            }
            public String toString() {
                return "[" + sum + ", " + maxPrefixSum + ", " + maxSuffixSum + ", " + maxSubarraySum + "]";
            }
        }
    }
    static class Reader extends PrintWriter {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
        StringBuilder sb = new StringBuilder();
        public Reader() {
            super(System.out);
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
        public Reader(String fileName) throws IOException {
            super(new File(fileName+".out"));
            din = new DataInputStream(new FileInputStream(fileName+".in"));
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
        public String readLine() throws IOException {
            sb.setLength(0);
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n' || c == '\r') {
                    if (cnt != 0) {
                        break;
                    } else {
                        continue;
                    }
                }
                sb.append((char)c);
                cnt++;
            }
            return sb.toString();
        }
        public String nextToken() throws IOException {
            sb.setLength(0);
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == ' ' || c == '\n' || c == '\r') {
                    if (cnt != 0) {
                        break;
                    } else {
                        continue;
                    }
                }
                cnt++;
                sb.append((char)c);
            }
            return sb.toString();
        }
        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            }  while ((c = read()) >= '0' && c <= '9');
            if (neg) return -ret;
            return ret;
        }
        public long nextLong() throws IOException {
            long ret = 0;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg) return -ret;
            return ret;
        }
        public double nextDouble() throws IOException {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ') c = read();
            boolean neg = (c == '-');
            if (neg) c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }
            if (neg) return -ret;
            return ret;
        }
        public void closeAll() throws Exception {
            super.close();
            din.close();
        }
    }    
}