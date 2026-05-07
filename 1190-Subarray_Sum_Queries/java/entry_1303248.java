//package CSES;
 
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;
 
public class entry_1303248 {
 
	public static class node {
		long prefix;
		long suffix;
		long sum;
		long max;
		
		public node(node A, node B) {
			this.prefix = Math.max(0, Math.max(A.sum + B.prefix, A.prefix));
			this.suffix = Math.max(0, Math.max(B.suffix, B.sum + A.suffix));
			this.sum = A.sum + B.sum;
			this.max = Math.max(Math.max(this.prefix, this.suffix), Math.max(A.max, B.max));
			this.max = Math.max(this.max, this.sum);
			this.max = Math.max(this.max, A.suffix + B.prefix);
		}
		
		public node(long val) {
			this.prefix = Math.max(0, val);
			this.suffix = Math.max(0, val);
			this.sum = val;
			this.max = Math.max(0, val);
		}
	}
	
	public static node[] st;
	
	public static void Build(int start, int end, int index, long[] arr) {
		if(start == end) {
			st[index] = new node(arr[start]);
			return; 
		}
		int mid = (start + end)>>1;
		Build(start, mid, index<<1, arr);
		Build(mid + 1, end, index<<1|1, arr);
		st[index] = new node(st[index<<1], st[index<<1|1]);
	}
	
	public static void Update(int start, int end, int index, int idx, long val) {
		if(start > idx || idx > end) {
			return;
		}
		if(start == end) {
			st[index] = new node(val);
			return;
		}
		int mid = (start + end)>>1;
		Update(start, mid, index<<1, idx, val);
		Update(mid + 1, end, index<<1|1, idx, val);
		st[index] = new node(st[index<<1], st[index<<1|1]);
	}
	
	public static void solve() {
		int n = s.nextInt();
		int q = s.nextInt();
		long[] arr = s.nextLongArray(n);
		st = new node[4 * n + 1];
		Build(0, n - 1, 1, arr);
//		out.println(st[1].max);
		while(q-- > 0) {
			int idx = s.nextInt() - 1;
			long val = s.nextLong();
			Update(0, n - 1, 1, idx, val);
			out.println(st[1].max);
		}
	}
 
	public static void main(String[] args) {
		new Thread(null, null, "Thread", 1 << 27) {
			public void run() {
				try {
					out = new PrintWriter(new BufferedOutputStream(System.out));
					s = new FastReader(System.in);
					solve();
					out.close();
				} catch (Exception e) {
					e.printStackTrace();
					System.exit(1);
				}
			}
		}.start();
	}
 
	public static PrintWriter out;
	public static FastReader s;
 
	public static class FastReader {
 
		private InputStream stream;
		private byte[] buf = new byte[4096];
		private int curChar, snumChars;
 
		public FastReader(InputStream stream) {
			this.stream = stream;
		}
 
		public int read() {
			if (snumChars == -1) {
				throw new InputMismatchException();
			}
			if (curChar >= snumChars) {
				curChar = 0;
				try {
					snumChars = stream.read(buf);
				} catch (IOException E) {
					throw new InputMismatchException();
				}
			}
			if (snumChars <= 0) {
				return -1;
			}
			return buf[curChar++];
		}
 
		public int nextInt() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			int sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			int number = 0;
			do {
				number *= 10;
				number += c - '0';
				c = read();
			} while (!isSpaceChar(c));
			return number * sgn;
		}
 
		public long nextLong() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			long sgn = 1;
			if (c == '-') {
				sgn = -1;
				c = read();
			}
			long number = 0;
			do {
				number *= 10L;
				number += (long) (c - '0');
				c = read();
			} while (!isSpaceChar(c));
			return number * sgn;
		}
 
		public int[] nextIntArray(int n) {
			int[] arr = new int[n];
			for (int i = 0; i < n; i++) {
				arr[i] = this.nextInt();
			}
			return arr;
		}
 
		public long[] nextLongArray(int n) {
			long[] arr = new long[n];
			for (int i = 0; i < n; i++) {
				arr[i] = this.nextLong();
			}
			return arr;
		}
 
		public String next() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isSpaceChar(c));
			return res.toString();
		}
 
		public String nextLine() {
			int c = read();
			while (isSpaceChar(c)) {
				c = read();
			}
			StringBuilder res = new StringBuilder();
			do {
				res.appendCodePoint(c);
				c = read();
			} while (!isEndofLine(c));
			return res.toString();
		}
 
		public boolean isSpaceChar(int c) {
			return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
		}
 
		public boolean isEndofLine(int c) {
			return c == '\n' || c == '\r' || c == -1;
		}
 
	}
 
	
}