import java.io.*;
import java.util.*;
 
public class entry_5029355 {
    private static final String name = "runaway";
    private static PrintWriter out;
    private static FastIO sc;
    private static final int mod = 1_000_000_007;
    public static void main(String[] args) throws Exception {
        if(new File(name+".in").exists()){
            sc = new FastIO(name+".in");
            out = new PrintWriter(name+".out");
        }else{
            sc = new FastIO(System.in);
            out = new PrintWriter(new BufferedOutputStream(System.out));
        }
        int N = sc.nextInt(), Q = sc.nextInt();
        AST tree = new AST(N, (a, b) -> new long[] {
        	Math.max(Math.max(a[0], b[0]), a[2]+b[1]),
        	Math.max(a[1], a[3]+b[1]),
        	Math.max(b[2], b[3]+a[2]),
        	a[3]+b[3]
        });
        for(int i = 0; i<N; i++) {
        	int n = sc.nextInt();
        	tree.set(i, new long[] {Math.max(n, 0), n, n, n});
        }
        for(int i = 0; i<Q; i++) {
        	int k = sc.nextInt()-1, u = sc.nextInt();
        	tree.set(k, new long[] {Math.max(u, 0), u, u, u});
        	out.println(tree.all()[0]);
        }
        out.close();
    }
    private static class Merge implements Iterable<Integer>{
    	private static class Node{
    		public int num;
    		public Node next = null;
    		public Node(int num) {
    			this.num = num;
    		}
    	}
    	private class mergeIterator implements Iterator<Integer>{
    		private Node s;
    		public mergeIterator(Node s){
    			this.s = s;
    		}
			@Override
			public boolean hasNext() {
				return s != null;
			}
			@Override
			public Integer next() {
				int ret = s.num;
				s = s.next;
				return ret;
			}
    	}
    	private Node s, e;
    	private int size;
    	public Merge() {
    		s = e = null;
    		size = 0;
    	}
    	public void addF(int n) {
    		if(s == null) s = e = new Node(n);
    		else {
    			Node p = new Node(n);
    			p.next = s;
    			s = p;
    		}
    		size++;
    	}
    	public void add(int n) {
    		if(s == null) s = e = new Node(n);
    		else{
    			e.next = new Node(n);
    			e = e.next;
    		}
    		size++;
    	}
    	public void add(Merge m) {
    		e.next = m.s;
    		size+=m.size;
    	}
    	public int size() {
    		return size;
    	}
    	public String toString() {
    		StringBuilder sb = new StringBuilder();
    		sb.append("[");
    		for(int i: this)
    			sb.append(i+", ");
    		if(sb.length() > 1) sb.delete(sb.length()-2, sb.length());
    		sb.append("]");
    		return sb.toString();
    	}
		@Override
		public Iterator<Integer> iterator() {
			return new mergeIterator(s);
		}
    }
    private static class DSU{
    	private int[] par, size;
    	private int cc;
    	public DSU(int N) {
    		par = new int[N];
    		size = new int[N];
    		cc = N;
    		Arrays.fill(par, -1);
    		Arrays.fill(size, 1);
    	}
    	public int size(int num) {
    		return size[get(num)];
    	}
    	public int get(int num) {
    		return par[num] == -1 ? num:(par[num] = get(par[num]));
    	}
    	public boolean isSame(int x, int y) {
    		return get(x) == get(y);
    	}
    	public boolean unite(int x, int y) {
    		int p1 = get(x), p2 = get(y);
    		if(p1 == p2) return false;
    		if(size[p1] < size[p2]) {
    			int s = p2;
    			p2 = p1;
    			p1 = s;
    		}
    		size[p1]+=size[p2];
    		par[p2] = p1;
    		cc--;
    		return true;
    	}
    	public int getCC() {
    		return cc;
    	}
    }
    private static class Two<A, B>{
        public final A a;
        public final B b;
        public Two(A a, B b) {
        	this.a = a;
            this.b = b;
        }
        @Override
        public boolean equals(Object obj) {
            if(!(obj instanceof Two)) return false;
            Two curr = (Two)obj;
            return curr.a.equals(a) && curr.b.equals(b);
        }
        @Override
        public int hashCode() {
            long seed = a.hashCode();
            seed = seed<<32;
            seed|=b.hashCode();
            Random r = new Random();
            r.setSeed(seed);
            return r.nextInt();
        }
        @Override
        public String toString() {
            return "("+a.toString()+", "+b.toString()+")";
        }
    }
    private static class Cnt {
        public TreeMap<Integer, Integer> map;
        public Cnt() {
            map = new TreeMap<>();
        }
        public void add(int num) {
            add(num, 1);
        }
        public void rem(int num) {
            add(num, -1);
        }
        public void rem(int num, int cnt) {
            add(num, -cnt);
        }
        public void add(int num, int cnt) {
            Integer get = map.get(num);
            if(get == null) get = 0;
            get+=cnt;
            if(get == 0) map.remove(num);
            else map.put(num, get);
        }
    }
    private static class BIT {
        private final long[] bit;
        private final long[] arr;
        private final int len;
        public BIT(int len) {
            bit = new long[len + 1];
            arr = new long[len];
            this.len = len;
        }
        public long get(int ind) {
            return arr[ind];
        }
        public void set(int ind, long val) {
            add(ind, val - arr[ind]);
        }
        public void add(int ind, long val) {
            arr[ind] += val;
            ind++;
            for (; ind <= len; ind += ind & -ind) bit[ind] += val;
        }
        public long prev(int ind) {
            ind++;
            long sum = 0;
            for (; ind > 0; ind -= ind & -ind) sum += bit[ind];
            return sum;
        }
        public long sum(int a, int b) {
            return prev(b)-(a == 0 ? 0:prev(a-1));
        }
    }
	public static class AST {
		public interface Oper{
			long[] solve(long[] a, long[] b);
		}
		private class Node {
			public long[] val;
			public Node p, le, ri;
			public int l, r;
			public Node(int l, int r) {
				this.l = l;
				this.r = r;
			}
		}
		private final Oper oper;
		private final Node top;
		private final Node[] last;
		public AST(int n, Oper oper) {
			this.oper = oper;
			top = new Node(0, n-1);
			last = new Node[n];
			getNode(top);
		}
		private void getNode(Node t) {
			if(t.l == t.r) {
				last[t.l] = t; 
				return;
			}
			int mid = (t.l+t.r)>>1;
			t.le = new Node(t.l, mid);
			t.ri = new Node(mid+1, t.r);
			getNode(t.le);
			getNode(t.ri);
			t.le.p = t.ri.p = t;
		}
		public void set(int k, long[] num) {
			Node t = last[k];
			t.val = num;
			t = t.p;
			while(t != null) {
				if(t.le.val != null && t.ri.val != null) t.val = oper.solve(t.le.val, t.ri.val);
				t = t.p;
			}
		}
		public long[] all() {
			return top.val;
		}
	}
	public static class ST {
		public interface Oper{
			long solve(long a, long b);
		}
		private long[] tree;
		private final int n;
		private final Oper oper;
		public ST(int n, Oper oper) {
			this.n = n;
			tree = new long[n<<1];
			this.oper = oper;
		}
		public long get(int a, int b) {
			a += n;
			b += n;
			long curr = 0;
			boolean checked = false;
			while (a <= b) {
				if ((a&1) == 1) {
					if(checked) curr = oper.solve(curr, tree[a++]);
					else curr = tree[a++];
					checked = true;
				}
				if ((b&1) == 0) {
					if(checked) curr = oper.solve(curr, tree[b--]);
					else curr = tree[b--];
					checked = true;
				}
				a = a>>1;
				b = b>>1;
			}
			return curr;
		}
		public void set(int index, long val) {
			index += n;
			tree[index] = val;
			for (index = index>>1; index >= 1; index = index>>1)
				tree[index] = oper.solve(tree[index<<1], tree[(index<<1)+1]);
		}
	}
	private static class FastIO {
        InputStream dis;
        byte[] buffer = new byte[1 << 17];
        int pointer = 0, end = 0;
        public FastIO(String fileName) throws Exception {
            dis = new FileInputStream(fileName);
        }
        public FastIO(InputStream is) throws Exception {
            dis = is;
        }
        public int nextInt() throws Exception {
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
        public long nextLong() throws Exception {
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
        private byte nextByte() throws Exception {
            while(pointer >= end) {
                end = dis.read(buffer, 0, buffer.length);
                pointer = 0;
            }
            return buffer[pointer++];
        }
        public double nextDouble() throws Exception {
            return Double.parseDouble(next());
        }
        public String next() throws Exception {
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
        public int[] nextArr() throws Exception {
        	return nextArr(nextInt());
        }
        public int[] nextArr(int len) throws Exception {
        	int[] ans = new int[len];
        	for(int i = 0; i<len; i++) ans[i] = nextInt();
        	return ans;
        }
        public List<Integer>[] nextTree() throws Exception {
        	return nextTree(nextInt());
        }
        public List<Integer>[] nextTree(int n) throws Exception {
        	return nextGraph(n, n-1);
        }
        public List<Integer>[] nextGraph(int n, int m) throws Exception{
        	List<Integer>[] ans = new List[n];
        	for(int i = 0; i<n; i++) ans[i] = new LinkedList<>();
        	for(int i = 0; i<m; i++) {
        		int a = nextInt()-1, b = nextInt()-1;
        		ans[a].add(b);
        		ans[b].add(a);
        	}
        	return ans;
        }
    }
}