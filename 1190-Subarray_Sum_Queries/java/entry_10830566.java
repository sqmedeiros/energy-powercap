import java.io.*;
 
public class entry_10830566 {
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
      din = new DataInputStream(
        new FileInputStream(file_name));
      buffer = new byte[BUFFER_SIZE];
      bufferPointer = bytesRead = 0;
    }
 
    public String readLine() throws IOException {
      byte[] buf = new byte[64]; // line length
      int cnt = 0, c;
      while ((c = read()) != -1) {
        if (c == '\n') {
          if (cnt != 0) {
            break;
          } else {
            continue;
          }
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
      if (neg)
        c = read();
      do {
        ret = ret * 10 + c - '0';
      } while ((c = read()) >= '0' && c <= '9');
 
      if (neg)
        return -ret;
      return ret;
    }
 
    public long nextLong() throws IOException {
      long ret = 0;
      byte c = read();
      while (c <= ' ')
        c = read();
      boolean neg = (c == '-');
      if (neg)
        c = read();
      do {
        ret = ret * 10 + c - '0';
      } while ((c = read()) >= '0' && c <= '9');
      if (neg)
        return -ret;
      return ret;
    }
 
    public double nextDouble() throws IOException {
      double ret = 0, div = 1;
      byte c = read();
      while (c <= ' ')
        c = read();
      boolean neg = (c == '-');
      if (neg)
        c = read();
 
      do {
        ret = ret * 10 + c - '0';
      } while ((c = read()) >= '0' && c <= '9');
 
      if (c == '.') {
        while ((c = read()) >= '0' && c <= '9') {
          ret += (c - '0') / (div *= 10);
        }
      }
 
      if (neg)
        return -ret;
      return ret;
    }
 
    private void fillBuffer() throws IOException {
      bytesRead = din.read(buffer, bufferPointer = 0,
        BUFFER_SIZE);
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
  }
 
  public static void main(String[] args) throws IOException {
    final Reader reader = new Reader();
    int n = reader.nextInt(), m = reader.nextInt();
    long[] arr = new long[n];
    for (int i = 0; i < n; i++) {
      arr[i] = reader.nextLong();
    }
    final SegTreeNode root = SegTreeNode.build(arr);
    StringBuilder output = new StringBuilder();
    for (int i = 0; i < m; i++) {
      int k = reader.nextInt() - 1;
      long x = reader.nextLong();
      root.update(k, x);
      output.append(root.subArrayValue).append('\n');
    }
    System.out.println(output);
  }
 
  public static class SegTreeNode {
    final SegTreeNode left, right;
    final int start, end;
    long subArrayValue;
    long prefixValue;
    long suffixValue;
    long sumValue;
 
    private SegTreeNode(final SegTreeNode left, final SegTreeNode right, final int start, final int end, final long subArrayValue, final long prefixValue, final long suffixValue, final long sumValue) {
      this.left = left;
      this.right = right;
      this.start = start;
      this.end = end;
      this.subArrayValue = subArrayValue;
      this.prefixValue = prefixValue;
      this.suffixValue = suffixValue;
      this.sumValue = sumValue;
    }
 
    public static SegTreeNode build(final long[] arr) {
      return buildHelper(arr, 0, arr.length - 1);
    }
 
    private static SegTreeNode buildHelper(final long[] arr, final int start, final int end) {
      if (start == end) {
        return new SegTreeNode(null, null, start, end, Math.max(0, arr[start]), Math.max(0, arr[start]), Math.max(0, arr[start]), arr[start]);
      }
      final int mid = start + (end - start) / 2;
      final SegTreeNode left = buildHelper(arr, start, mid);
      final SegTreeNode right = buildHelper(arr, mid + 1, end);
      return
        new SegTreeNode(
          left,
          right,
          start,
          end,
          Math.max(left.subArrayValue, Math.max(right.subArrayValue, left.suffixValue + right.prefixValue)),
          Math.max(left.prefixValue, left.sumValue + right.prefixValue),
          Math.max(right.suffixValue, right.sumValue + left.suffixValue),
          right.sumValue + left.sumValue);
    }
 
    public void update(final int index, final long newValue) {
      if (this.end < index || this.start > index) return;
      if (this.start == this.end) {
        this.subArrayValue = Math.max(0, newValue);
        this.prefixValue = Math.max(0, newValue);
        this.suffixValue = Math.max(0, newValue);
        this.sumValue = newValue;
      } else {
        left.update(index, newValue);
        right.update(index, newValue);
        this.subArrayValue = Math.max(left.subArrayValue, Math.max(right.subArrayValue, left.suffixValue + right.prefixValue));
        this.prefixValue = Math.max(left.prefixValue, left.sumValue + right.prefixValue);
        this.suffixValue = Math.max(right.suffixValue, right.sumValue + left.suffixValue);
        this.sumValue = right.sumValue + left.sumValue;
      }
    }
  }
}