import java.io.*;
import java.util.*;
 
public class entry_1117718 extends PrintWriter {
 
    private void solve()  {
        int n = sc.nextInt();
        int m = sc.nextInt();
        x = new long[n];
        for(int i = 0; i < n; i++) {
            x[i] = sc.nextInt();
        }
        L = new long[4*n];
        R = new long[4*n];
        sum = new long[4*n];
        best = new long[4*n];
        build(0,n-1,1);
        for(int i = 0; i < m; i++) {
            int k = sc.nextInt()-1;
            long x = sc.nextInt();
            set_point(0, n-1, 1, k, x);
            println(query());
        }
    }
    
    long[] L;
    long[] R;
    long[] sum;
    long[] best;
    
    long[] x;
    
    void build(int il, int ir, int i) {
        if(il == ir) {
            L[i] = x[il];
            R[i] = x[il];
            sum[i] = x[il];
            best[i] = x[il];
        } else {
            int imid = (il+ir)/2;
            build(il, imid, 2*i);
            build(imid+1, ir, 2*i+1);
            sum[i] = sum[2*i] + sum[2*i+1];
            L[i] = Math.max(L[2*i], sum[2*i]+L[2*i+1]);
            R[i] = Math.max(R[2*i+1], R[2*i]+sum[2*i+1]);
            best[i] = Math.max(best[2*i], best[2*i+1]);
            best[i] = Math.max(best[i], L[i]);
            best[i] = Math.max(best[i], R[i]);
            best[i] = Math.max(best[i], R[2*i]+L[2*i+1]);
        }
    }
    
    void set_point(int il, int ir, int i, int q, long x) {
        if(ir < q || il > q) return;
        
        if(q <= il && ir <= q) {
            sum[i] = x;
            L[i] = x;
            R[i] = x;
            sum[i] = x;
            best[i] = x;
            return;
        }
        
 
        int imid = (il+ir)/2;
        set_point(il, imid, 2*i, q, x);
        set_point(imid+1, ir, 2*i+1, q, x);
        sum[i] = sum[2*i] + sum[2*i+1];
        L[i] = Math.max(L[2*i], sum[2*i]+L[2*i+1]);
        R[i] = Math.max(R[2*i+1], R[2*i]+sum[2*i+1]);
        best[i] = Math.max(best[2*i], best[2*i+1]);
        best[i] = Math.max(best[i], L[i]);
        best[i] = Math.max(best[i], R[i]);
        best[i] = Math.max(best[i], R[2*i]+L[2*i+1]);
    }
    
    long query() {
        return Math.max(0, best[1]);
    }
         
    
    
//  Solution() throws FileNotFoundException { super(new File("output.txt")); }
//  InputReader sc = new InputReader(new FileInputStream("test_input.txt"));
  entry_1117718() { super(System.out); }
  InputReader sc = new InputReader(System.in);
  static class InputReader {
      InputReader(InputStream in) { this.in = in; } InputStream in;
      
      private byte[] buf = new byte[16384];
      private int    curChar;
      private int    numChars;
      
 
      public int read() {
          if (numChars == -1)
              throw new InputMismatchException();
          if (curChar >= numChars) {
              curChar = 0;
              try {
                  numChars = in.read(buf);
              } catch (IOException e) {
                  throw new InputMismatchException();
              }
              if (numChars <= 0)
                  return -1;
          }
          return buf[curChar++];
      }
 
      public String nextLine() {
          int c = read();
          while (isSpaceChar(c))
              c = read();
          StringBuilder res = new StringBuilder();
          do {
              res.appendCodePoint(c);
              c = read();
          } while (!isEndOfLine(c));
          return res.toString();
      }
 
      public String nextString() {
          int c = read();
          while (isSpaceChar(c))
              c = read();
          StringBuilder res = new StringBuilder();
          do {
              res.appendCodePoint(c);
              c = read();
          } while (!isSpaceChar(c));
          return res.toString();
      }
 
      public long nextLong() {
          int c = read();
          while (isSpaceChar(c))
              c = read();
          int sgn = 1;
          if (c == '-') {
              sgn = -1;
              c = read();
          }
          long res = 0;
          do {
              if (c < '0' || c > '9')
                  throw new InputMismatchException();
              res *= 10;
              res += c - '0';
              c = read();
          } while (!isSpaceChar(c));
          return res * sgn;
      }
 
      public int nextInt() {
          int c = read();
          while (isSpaceChar(c))
              c = read();
          int sgn = 1;
          if (c == '-') {
              sgn = -1;
              c = read();
          }
          int res = 0;
          do {
              if (c < '0' || c > '9')
                  throw new InputMismatchException();
              res *= 10;
              res += c - '0';
              c = read();
          } while (!isSpaceChar(c));
          return res * sgn;
      }
 
      private boolean isSpaceChar(int c) {
          return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
      }
 
      private boolean isEndOfLine(int c) {
          return c == '\n' || c == '\r' || c == -1;
      }
  }
 
    public static void main(String[] $) {
        new Thread(null, new Runnable() {
            public void run() {
                long start = System.nanoTime();
                try {entry_1117718 solution = new entry_1117718(); solution.solve(); solution.flush();} 
                catch (Exception e) {e.printStackTrace(); System.exit(1);}
                System.err.println((System.nanoTime()-start)/1E9);
            }
        }, "1", 1 << 27).start();
 
    }
 
}