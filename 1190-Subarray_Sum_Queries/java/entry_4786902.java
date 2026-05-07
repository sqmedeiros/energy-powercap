//package range_queries.subarray_sum_queries;
 
import java.io.BufferedInputStream;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.function.BinaryOperator;
 
class FastReader {
    private int BS = 1 << 16;
    private char NC = (char) 0;
    private byte[] buf = new byte[BS];
    private int bId = 0, size = 0;
    private char c = NC;
    private double cnt = 1;
    private BufferedInputStream in;
 
    public FastReader() {
        in = new BufferedInputStream(System.in, BS);
    }
 
    private char readChar() {
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
 
    public int readInt() {
        return (int) readLong();
    }
 
    public int[] readInts(int N) {
        int[] res = new int[N];
        for (int i = 0; i < N; i++) {
            res[i] = (int) readLong();
        }
        return res;
    }
 
    public long[] readLongs(int N) {
        long[] res = new long[N];
        for (int i = 0; i < N; i++) {
            res[i] = readLong();
        }
        return res;
    }
 
    public long readLong() {
        cnt = 1;
        boolean neg = false;
        if (c == NC) c = readChar();
        for (; (c < '0' || c > '9'); c = readChar()) {
            if (c == '-') neg = true;
        }
        long res = 0;
        for (; c >= '0' && c <= '9'; c = readChar()) {
            res = (res << 3) + (res << 1) + c - '0';
            cnt *= 10;
        }
        return neg ? -res : res;
    }
 
    public double nextDouble() {
        double cur = readLong();
        return c != '.' ? cur : cur + readLong() / cnt;
    }
 
    public double[] nextDoubles(int N) {
        double[] res = new double[N];
        for (int i = 0; i < N; i++) {
            res[i] = nextDouble();
        }
        return res;
    }
 
    public String next() {
        StringBuilder res = new StringBuilder();
        while (c <= 32) c = readChar();
        while (c > 32) {
            res.append(c);
            c = readChar();
        }
        return res.toString();
    }
 
    public String readString() {
        StringBuilder res = new StringBuilder();
        while (c <= 32) c = readChar();
        while (c != '\n') {
            res.append(c);
            c = readChar();
        }
        return res.toString();
    }
 
    public boolean hasNext() {
        if (c > 32) return true;
        while (true) {
            c = readChar();
            if (c == NC) return false;
            else if (c > 32) return true;
        }
    }
}
 
class SubArrayAssociativeOperationFinder<T> {
    private List<T> segmentTree;
    private T identity;
    private BinaryOperator<T> associativeBinaryOperator;
    SubArrayAssociativeOperationFinder(List<T> list, BinaryOperator<T> associativeBinaryOperator, T identity){
        this.identity = identity;
        this.associativeBinaryOperator = associativeBinaryOperator;
        createSegmentTree(list);
    }
 
    private void createSegmentTree(List<T> list) {
        int identityPaddedLen = 1;
        while (identityPaddedLen < list.size()) identityPaddedLen <<= 1;
 
        segmentTree = new ArrayList<>(2*identityPaddedLen);
 
        for (int i = 0; i < 2*identityPaddedLen; i++) segmentTree.add(identity);
 
        for (int i = 0; i < list.size(); i++) segmentTree.set(i+identityPaddedLen, list.get(i));
 
        for (int i = identityPaddedLen-1; i > 0; i--){
            T leftChildVal = segmentTree.get(2*i);
            T rightChildVal = segmentTree.get(2*i+1);
            segmentTree.set(i, associativeBinaryOperator.apply(leftChildVal, rightChildVal));
        }
    }
    public T pointQuery(int index){
        int treeIndex = segmentTree.size()/2 + index;
        return segmentTree.get(treeIndex);
    }
    public void update(int index, T newValue){
        int treeIndex = segmentTree.size()/2+index;
        segmentTree.set(treeIndex, newValue);
        for (int parent = treeIndex/2; parent != 0; parent /= 2){
            T leftVal = segmentTree.get(2*parent);
            T rightVal = segmentTree.get(2*parent+1);
            segmentTree.set(parent, associativeBinaryOperator.apply(leftVal, rightVal));
        }
 
    }
    private T getSubArrayValue(int arrayLeft, int arrayRight, int nodeLeft, int nodeRight, int treeIndex){
        if (arrayLeft > nodeRight || arrayRight < nodeLeft) return identity;
        if (arrayLeft <= nodeLeft && nodeRight <= arrayRight){
            return segmentTree.get(treeIndex);
        }
        int mid = (nodeLeft+nodeRight)/2;
        return associativeBinaryOperator.apply(
                getSubArrayValue(arrayLeft, arrayRight, nodeLeft, mid, 2*treeIndex),
                getSubArrayValue(arrayLeft, arrayRight, mid+1, nodeRight, 2*treeIndex+1)
        );
 
    }
    public T getSubArrayValue(int arrayLeft, int arrayRight){
        return getSubArrayValue(arrayLeft, arrayRight, 0, (segmentTree.size()/2)-1, 1);
    }
 
 
}
 
class SubArraySumContainer {
    public SubArraySumContainer(long maxPrefixSum, long maxSuffixSum, long maxSubArraySum, long sum) {
        this.maxPrefixSum = maxPrefixSum;
        this.maxSuffixSum = maxSuffixSum;
        this.maxSubArraySum = maxSubArraySum;
        this.sum = sum;
    }
 
    long maxPrefixSum;
    long maxSuffixSum;
    long maxSubArraySum;
    long sum;
}
 
public class entry_4786902 {
    private PrintWriter writer;
    private FastReader reader;
    private static final SubArraySumContainer IDENTITY_CONTAINER = new SubArraySumContainer(-1, -1,-1,-1);
    private SubArraySumContainer combine(SubArraySumContainer firstArg, SubArraySumContainer secondArg){
        if (firstArg == IDENTITY_CONTAINER) return secondArg;
        else if (secondArg == IDENTITY_CONTAINER) return firstArg;
 
        long sum = firstArg.sum + secondArg.sum;
        long maxPrefixSum = Math.max(firstArg.maxPrefixSum, firstArg.sum + secondArg.maxPrefixSum);
 
        long maxSuffixSum = Math.max(firstArg.maxSuffixSum + secondArg.sum, secondArg.maxSuffixSum);
 
 
        long maxCrossingSubArraySum = firstArg.maxSuffixSum + secondArg.maxPrefixSum;
 
        long maxSubArraySumAmongFirstAndSecond = Math.max(firstArg.maxSubArraySum, secondArg.maxSubArraySum);
 
        long maxSubArraySum = Math.max(maxCrossingSubArraySum, maxSubArraySumAmongFirstAndSecond);
 
 
        return new SubArraySumContainer(maxPrefixSum, maxSuffixSum, maxSubArraySum, sum);
    }
    private void solve(){
        writer = new PrintWriter(System.out);
        reader = new FastReader();
 
        int n = reader.readInt();
        int numQueries = reader.readInt();
        List<SubArraySumContainer> list = new ArrayList<>();
        for (int i = 0; i < n; i++){
            int val = reader.readInt();
            list.add(new SubArraySumContainer(val, val,val, val));
        }
        SubArrayAssociativeOperationFinder<SubArraySumContainer> maxSubArrayFinder =
                new SubArrayAssociativeOperationFinder<>(list, this::combine, IDENTITY_CONTAINER);
 
        while (--numQueries >= 0){
            int index = reader.readInt()-1;
            int newVal = reader.readInt();
            maxSubArrayFinder.update(index, new SubArraySumContainer(newVal, newVal, newVal, newVal));
            SubArraySumContainer container = maxSubArrayFinder.getSubArrayValue(0, n-1);
            long maxSubArraySum = Math.max(container.maxSubArraySum, 0);
            writer.println(maxSubArraySum);
 
        }
 
        writer.close();
 
    }
 
    public static void main(String[] args) {
        new entry_4786902().solve();
    }
}