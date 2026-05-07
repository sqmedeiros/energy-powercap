import java.io.*;
import java.util.*;
 
 
class Node{
    long sum,maxsubsum,prefix,suffix;
 
    public Node(long s, long  m,long p,long su){
        sum=s;
        maxsubsum=m;
        prefix=p;
        suffix=su;
    }
}
 
public class entry_16530717 {
    static long INF=(long)1e18;
 
    static FastScanner fs = new FastScanner();
 
    public static void main(String[] args) throws Exception {
        int n = fs.nextInt();
        int m = fs.nextInt();
 
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = fs.nextInt();
        }
 
        //segment tree
        Node[] st=new Node[4*n];
        createST(st,0,n-1,0,arr);
 
        StringBuilder sb = new StringBuilder();
 
        while (m-->0) {
            int k = fs.nextInt()-1;
            int x = fs.nextInt();
            // sb.append(solve(arr, a, b,st,0,n-1,0)).append('\n');
            update(0, n-1, 0, k, x, st);
             sb.append(Math.max(0L,st[0].maxsubsum)).append('\n');
        }
 
        System.out.print(sb.toString());
    }
 
    static long solve(long[] arr, int a, int b,long[] st,int ss,int se,int idx) {
        // logic here
        if(a> se || b< ss){
            return INF; //oot of bound
        }
 
        if(a<=ss && b>=se) {
            return st[idx]; // completely inside
        }
        int mid=(se+ss)/2;
        long l=solve(arr,a,b,st,ss,mid,idx*2+1);
        long r=solve(arr,a,b,st,mid+1,se,idx*2+2);
        return Math.min(l,r);
 
    }
    static void update(int ss, int se, int idx, int pos, long val, Node[] st) {
    if (ss == se) {
        st[idx] = new Node(val,val,val,val);
        return;
    }
 
    int mid = (ss + se) / 2;
 
    if (pos <= mid)
        update(ss, mid, idx * 2 + 1, pos, val, st);
    else
        update(mid + 1, se, idx * 2 + 2, pos, val, st);
 
    st[idx] = merge(st[2 * idx + 1] ,st[2 * idx + 2]);
}
 
    static void createST(Node[] st, int ss, int se,int idx,long[] arr) {
        if(ss==se){
            st[idx]=new Node(arr[ss],arr[ss],arr[ss],arr[ss]);
            return;
        }
        int mid=(ss+se)/2;
        createST(st,ss,mid,idx*2+1,arr);
        createST(st,mid+1,se,idx*2+2,arr);
        st[idx]=merge(st[2*idx+1],st[2*idx+2]);
    }
 
    static Node merge(Node left,Node right){
        Node node=new Node(0,0,0,0);
        node.sum=left.sum+right.sum;
        node.prefix=Math.max(left.prefix,left.sum+right.prefix);
        node.suffix=Math.max(right.suffix,right.sum+left.suffix);
        node.maxsubsum=Math.max(left.suffix+right.prefix,Math.max(left.maxsubsum,right.maxsubsum));
    return node;
    }
 
    // FAST INPUT
    static class FastScanner {
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0, len = 0;
        private final InputStream in = System.in;
 
        int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) return -1;
            }
            return buffer[ptr++];
        }
 
        int nextInt() throws IOException {
            int c, sign = 1, val = 0;
            do {
                c = read();
            } while (c <= ' ');
 
            if (c == '-') {
                sign = -1;
                c = read();
            }
 
            while (c > ' ') {
                val = val * 10 + (c - '0');
                c = read();
            }
            return val * sign;
        }
    }
}