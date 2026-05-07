import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.InputStream;
 
/**
 * Built using CHelper plug-in Actual solution is at the top
 *
 * @author NMouad21
 */
public class entry_252910 {
 
  public static void main(String[] args) {
    InputStream inputStream = System.in;
    OutputStream outputStream = System.out;
    InputReader in = new InputReader(inputStream);
    PrintWriter out = new PrintWriter(outputStream);
    Task1190 solver = new Task1190();
    solver.solve(1, in, out);
    out.close();
  }
 
  static class Task1190 {
 
    public void solve(int testNumber, InputReader in, PrintWriter out) {
      int n = in.nextInt();
      int q = in.nextInt();
      int[] a = in.nextIntArrayOneBased(n);
      SegTree st = new SegTree(n, a);
      while (q-- > 0) {
        int pos = in.nextInt();
        int v = in.nextInt();
        out.println(st.update(pos, v));
      }
    }
 
    private final class SegTree {
 
      private final int[] a;
      private final int n;
      private final long[] vl;
      private final long[] vr;
      private final long[] v;
      private final long[] mx;
      private int queryPos;
      private int queryValue;
 
      public SegTree(int n, int[] a) {
        this.n = n;
        this.a = a;
        this.v = new long[(n + 1) << 2];
        this.vl = new long[v.length];
        this.vr = new long[v.length];
        this.mx = new long[v.length];
        build(1, 1, n);
      }
 
      private final void combine(int lid, int rid) {
        int id = lid >>> 1;
        v[id] = v[lid] + v[rid];
        vl[id] = Long.max(Long.max(v[id], vl[lid]), v[lid] + vl[rid]);
        vr[id] = Long.max(Long.max(v[id], vr[rid]), v[rid] + vr[lid]);
        mx[id] = Long
            .max(Long.max(Long.max(vl[id], vr[id]), Long.max(mx[lid], mx[rid])), vr[lid] + vl[rid]);
        assert mx[id] >= 0;
        assert vl[id] >= 0;
        assert vr[id] >= 0;
      }
 
      private final void build(int id, int l, int r) {
        if (l == r) {
          v[id] = a[l];
          vl[id] = vr[id] = mx[id] = Long.max(0L, a[l]);
        } else {
          int m = (l + r) >>> 1;
          build(id << 1, l, m);
          build(id << 1 | 1, m + 1, r);
          combine(id << 1, id << 1 | 1);
        }
      }
 
      private final void update(int id, int l, int r) {
        if (l == r) {
          v[id] = a[queryPos] = queryValue;
          vl[id] = vr[id] = mx[id] = Long.max(0L, queryValue);
        } else {
          int m = (l + r) >>> 1;
          if (queryPos <= m) {
            update(id << 1, l, m);
          } else {
            update(id << 1 | 1, m + 1, r);
          }
          combine(id << 1, id << 1 | 1);
        }
      }
 
      private final long update(int pos, int v) {
        queryPos = pos;
        queryValue = v;
        update(1, 1, n);
        return mx[1];
      }
 
    }
 
  }
 
  static final class InputReader {
 
    private final InputStream stream;
    private final byte[] buf = new byte[1 << 20];
    private int curChar;
    private int numChars;
 
    public InputReader() {
      this.stream = System.in;
    }
 
    public InputReader(final InputStream stream) {
      this.stream = stream;
    }
 
    private final int read() {
      if (this.numChars == -1) {
        throw new UnknownError();
      } else {
        if (this.curChar >= this.numChars) {
          this.curChar = 0;
 
          try {
            this.numChars = this.stream.read(this.buf);
          } catch (IOException ex) {
            throw new InputMismatchException();
          }
 
          if (this.numChars <= 0) {
            return -1;
          }
        }
 
        return this.buf[this.curChar++];
      }
    }
 
    public final int nextInt() {
      int c;
      for (c = this.read(); isSpaceChar(c); c = this.read()) {
      }
 
      byte sgn = 1;
      if (c == 45) { // 45 == '-'
        sgn = -1;
        c = this.read();
      }
 
      int res = 0;
 
      while (c >= 48 && c <= 57) { // 48 == '0', 57 == '9'
        res *= 10;
        res += c - 48; // 48 == '0'
        c = this.read();
        if (isSpaceChar(c)) {
          return res * sgn;
        }
      }
 
      throw new InputMismatchException();
    }
 
    private static final boolean isSpaceChar(final int c) {
      return c == 32 || c == 10 || c == 13 || c == 9
          || c == -1; // 32 == ' ', 10 == '\n', 13 == '\r', 9 == '\t'
    }
 
    public final int[] nextIntArrayOneBased(final int n) {
      int[] ret = new int[n + 1];
      for (int i = 1; i <= n; i++) {
        ret[i] = nextInt();
      }
      return ret;
    }
 
  }
}
 