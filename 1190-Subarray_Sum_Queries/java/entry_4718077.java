//package cronumax.demo;
 
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Arrays;
 
public class entry_4718077 {
 
    static InputStream in = new BufferedInputStream(System.in);
    static PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
 
    static int nextInt() {
        int r = 0;
        boolean flag = false;
        try {
            int c = in.read();
            if( ((char) c) == '-'){
                flag = true;
            }
            while (c < '0' || c > '9') c = in.read();
            while (c >= '0' && c <= '9') {
                r = r * 10 + (c - '0');
                c = in.read();
            }
 
        } catch (Exception e) {
            // ignore
        }
        return flag ? -r : r;
    }
 
    static class Node {
        long prefix;
        long suffix;
        long sum;
        long max;
 
        public Node(long prefix, long suffix, long sum, long max) {
            this.prefix = prefix;
            this.suffix = suffix;
            this.sum = sum;
            this.max = max;
        }
    }
 
    static Node seg[] = new Node[1000000];
    static int INF = Integer.MIN_VALUE;
 
    public static void modify(int u, int l, int r, int pos, int val) {
        if (l == r) {
            seg[u] = new Node(val, val, val, val);
            return;
        }
 
        int lc = 2 * u;
        int rc = 2 * u + 1;
 
        int mid = (l + r) / 2;
 
        if ( pos <= mid) {
            modify(lc, l, mid, pos, val);
        } else {
            modify(rc, mid + 1, r, pos, val);
        }
        seg[u] = merge(seg[lc], seg[rc]);
    }
 
    public static Node query(int u, int l, int r, int qL, int qR) {
        if (qR < l || qL > r) {
            // sum 最小值是 0
            return new Node(INF, INF, 0, INF);
        }
 
        if (qL <= l && r <= qR) {
            return seg[u];
        }
 
        int lc = 2 * u;
        int rc = 2 * u + 1;
 
        int mid = (l + r) / 2;
 
        Node left = query(lc, l, mid, qL, qR);
        Node right = query(rc, mid + 1, r, qL, qR);
        // 所有交集的集合合併，就是 max 值
        return merge(left, right); // [l ,r] 交集[qL, qR]
    }
 
    public static Node merge(Node l, Node r) {
        Node node = new Node(0, 0, 0, 0);
        node.prefix = Math.max(l.prefix, l.sum + r.prefix);
        node.suffix = Math.max(r.suffix, r.sum + l.suffix);
        node.sum = l.sum + r.sum;
        node.max = Math.max(Math.max(l.max, r.max), l.suffix + r.prefix);
        return node;
    }
 
    public static void main(String[] args) {
        int n = nextInt();
        int m = nextInt();
 
        Arrays.fill(seg, new Node(INF, INF, 0, INF));
 
        for(int i = 1; i <= n; i++){
            // init 所有 leaf node 的值, 並更新 parent
            int val = nextInt();
            modify(1, 1, n, i, val);
        }
 
 
        for(int i = 0; i < m; i++){
            int p = nextInt();
            int val = nextInt();
            // 單點更新
            modify(1, 1, n, p, val);
            // root 會存最大值
            out.println(seg[1].max < 0 ? 0 : seg[1].max );
            //out.println(query(1, 1, n, 1, n).max);
        }
        out.flush();
 
    }
 
 
}