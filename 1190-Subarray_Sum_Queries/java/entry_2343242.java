/*
CSES
Range Queries
*/
 
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
 
public class entry_2343242 {
	
	public static final int MAXN = 200001;
	
	public static int n, m;
	public static long[] a;
	public static Node[] segtree;
	
	public static void main(String[] args) throws IOException {
		FastIO in = new FastIO(System.in);
		
		n = in.nextInt();
		m = in.nextInt();
		a = new long[MAXN];
		segtree = new Node[4*MAXN];
		
		for (int i = 1; i <= n; i++) {
			a[i] = in.nextLong();
		}
		build(1, n, 1);
		
		StringBuilder sb = new StringBuilder();
		while (m-- > 0) {
			int i = in.nextInt();
			long j = in.nextLong();
			update(i, j, 1, n, 1);
			sb.append(segtree[1].g).append('\n');
		}
		System.out.println(sb);
		
		in.close();
	}
	
	public static void build(int l, int r, int v) {
		if (l == r) segtree[v] = new Node(Math.max(a[l], 0), Math.max(a[l], 0), Math.max(a[l], 0), a[l]);
		else {
			int mid = (l+r)/2;
			build(l, mid, 2*v);
			build(mid+1, r, 2*v+1);
			segtree[v] = new Node(Math.max(Math.max(segtree[2*v].g, segtree[2*v+1].g), segtree[2*v].r+segtree[2*v+1].l),
					Math.max(segtree[2*v].l, segtree[2*v].s+segtree[2*v+1].l),
					Math.max(segtree[2*v].r+segtree[2*v+1].s, segtree[2*v+1].r),
					segtree[2*v].s+segtree[2*v+1].s);
		}
	}
	
	public static void update(int i, long j, int l, int r, int v) {
		if (l == r) segtree[v] = new Node(Math.max(j, 0), Math.max(j, 0), Math.max(j, 0), j);
		else {
			int mid = (l+r)/2;
			if (i > mid) update(i, j, mid+1, r, 2*v+1);
			else update(i, j, l, mid, 2*v);
			segtree[v] = new Node(Math.max(Math.max(segtree[2*v].g, segtree[2*v+1].g), segtree[2*v].r+segtree[2*v+1].l),
					Math.max(segtree[2*v].l, segtree[2*v].s+segtree[2*v+1].l),
					Math.max(segtree[2*v].r+segtree[2*v+1].s, segtree[2*v+1].r),
					segtree[2*v].s+segtree[2*v+1].s);
		}
	}
	
	public static class Node {
		long g;
		long l;
		long r;
		long s;
		
		public Node(long g, long l, long r, long s) {
			this.g = g;
			this.l = l;
			this.r = r;
			this.s = s;
		}
	}
	
	public static class FastIO {
		private InputStream dis;
		private byte[] buffer = new byte[1 << 17];
		private int pointer = 0;
	
		public FastIO(String fileName) throws IOException {
			dis = new FileInputStream(fileName);
		}
	
		public FastIO(InputStream is) throws IOException {
			dis = is;
		}
	
		public int nextInt() throws IOException {
			int ret = 0;
			byte b;
			
			do {
				b = nextByte();
			} while (b <= ' ');
			
			boolean negative = false;
			if (b == '-') {
				negative = true;
				b = nextByte();
			}
			
			while (b >= '0' && b <= '9') {
				ret = 10 * ret + b - '0';
				b = nextByte();
			}
	
			return (negative) ? -ret : ret;
		}
	
		public long nextLong() throws IOException {
			long ret = 0;
			byte b;
			
			do {
				b = nextByte();
			} while (b <= ' ');
			
			boolean negative = false;
			if (b == '-') {
				negative = true;
				b = nextByte();
			}
			
			while (b >= '0' && b <= '9') {
				ret = 10 * ret + b - '0';
				b = nextByte();
			}
			
			return (negative) ? -ret : ret;
		}
	
		public byte nextByte() throws IOException {
			if (pointer == buffer.length) {
				dis.read(buffer, 0, buffer.length);
				pointer = 0;
			}
			return buffer[pointer++];
		}
	
		public String next() throws IOException {
			StringBuffer ret = new StringBuffer();
			byte b;
			
			do {
				b = nextByte();
			} while (b <= ' ');
			
			while (b > ' ') {
				ret.appendCodePoint(b);
				b = nextByte();
			}
	
			return ret.toString();
		}
	
		public void close() throws IOException {
			dis.close();
		}
	}
}