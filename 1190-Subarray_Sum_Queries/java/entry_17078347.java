import java.io.*;
import java.util.*;
 
 
public class entry_17078347{
    static int MOD=(int)(1e9+7);
    static int MAX=Integer.MAX_VALUE;
    static int n,m;
    static long[] a;
    
    static class SegTree{
    	Node[] tree;
    	int n;
    	SegTree(long[] arr){
    		this.n=arr.length;
    		tree=new Node[4*n];	
    		build(1,0,n-1,arr);
    	}
    	class Node{
    		long sum;
    		long pref;
    		long suf;
    		long ans;
		
    		Node(long sum,long pref,long suf,long ans){
    			this.sum=sum;
    			this.pref=pref;
    			this.suf=suf;
    			this.ans=ans;
    		}
    	}
    	
    	Node merge(Node left,Node right){
    		Node res=new Node(0,0,0,0);
    		res.sum=left.sum+right.sum;
    		res.pref=Math.max(left.pref,left.sum+right.pref);
    		res.suf=Math.max(right.suf,right.sum+left.suf);
    		res.ans=Math.max(left.ans,right.ans);
    		res.ans=Math.max(res.ans,left.suf+right.pref);
    		return res;
    	}
    	void build(int node,int l,int r,long[] arr){
    		if(r<l)return;
    		if(l==r){
    			long num=Math.max(arr[l],0);
    			tree[node]=new Node(arr[l],num,num,num);
    			return;
    		}
    		int mid=(l+r)/2;
    		build(2*node,l,mid,arr);
    		build(2*node+1,mid+1,r,arr);
    		tree[node]=merge(tree[2*node],tree[2*node+1]);
    	}
    	void update(int node,int l,int r,int pos,long val){
    		if(r<l)return;
    		if(l==r){
    			long num=Math.max(val,0);
    			tree[node]=new Node(val,num,num,num);
    			return;
    		}
    		int mid=(l+r)/2;
    		
    		if(pos<=mid)
    		 update(2*node,l,mid,pos,val);
    		else
    		 update(2*node+1,mid+1,r,pos,val);
    		 tree[node]=merge(tree[2*node],tree[2*node+1]);
    	}
    	Node query(int node,int l,int r,int ql,int qr){
    		if(r<ql || l>qr)
    		 return new Node(0,0,0,0);
    		
    		if(ql<=l && r<=qr){
    			return tree[node];
    		}
    		int mid=(l+r)/2;
    		
    		Node left=query(2*node,l,mid,ql,qr);
    		Node right=query(2*node+1,mid+1,r,ql,qr);
    		return merge(left,right);
    	}
    	void update(int pos,long val){
    		update(1,0,n-1,pos,val);
    	}
    	long query(int ql,int qr){
    		return query(1,0,n-1,ql,qr).ans;
    	}
    }
    
	static void solve(FastScanner fs,PrintWriter out){
         n=fs.nextInt();
         m=fs.nextInt();
         a=fs.readArrayLong(n);
         SegTree seg=new SegTree(a);
         
         for(int i=0;i<m;i++){
         	 int k=fs.nextInt()-1;
         	 long x=fs.nextLong();
         	 seg.update(k,x);
         	 out.println(seg.query(0,n-1));
         }
	}
		
		
   public static void main(String[] args)  {
		 FastScanner fs=new FastScanner();
		 PrintWriter out = new PrintWriter(System.out);
 
		 // int t=fs.nextInt();
 
		 // while(t-- !=0){
         //    out.println(solve(fs,out));
		 // }
		 //out.println(solve(fs,out));
          solve(fs,out);
		 out.flush();
	}
	
	static class FastScanner {
	    private final InputStream in = System.in;
	    private final byte[] buffer = new byte[1 << 16];
	    private int ptr = 0, len = 0;
	
	    private int read() {
	        if (ptr >= len) {
	            try {
	                len = in.read(buffer);
	                ptr = 0;
	                if (len <= 0) return -1;
	            } catch (IOException e) {
	                return -1;
	            }
	        }
	        return buffer[ptr++];
	    }
	
	    String next() {
	        StringBuilder sb = new StringBuilder();
	        int c;
	
	        while ((c = read()) != -1 && c <= ' ');
	
	        while (c > ' ') {
	            sb.append((char)c);
	            c = read();
	        }
	        return sb.toString();
	    }
	
	    int nextInt() {
	        int c;
	        while ((c = read()) <= ' ');
	
	        int sign = 1;
	        if (c == '-') {
	            sign = -1;
	            c = read();
	        }
	
	        int val = 0;
	        while (c > ' ') {
	            val = val * 10 + (c - '0');
	            c = read();
	        }
	        return val * sign;
	    }
	
	    long nextLong() {
	        int c;
	        while ((c = read()) <= ' ');
	
	        int sign = 1;
	        if (c == '-') {
	            sign = -1;
	            c = read();
	        }
	
	        long val = 0;
	        while (c > ' ') {
	            val = val * 10 + (c - '0');
	            c = read();
	        }
	        return val * sign;
	    }
	
	    char nextChar() {
	        int c;
	        while ((c = read()) <= ' ');
	        return (char)c;
	    }
	
	    int[] readArray(int n) {
	        int[] a = new int[n];
	        for (int i = 0; i < n; i++) a[i] = nextInt();
	        return a;
	    }
	
	    long[] readArrayLong(int n) {
	        long[] a = new long[n];
	        for (int i = 0; i < n; i++) a[i] = nextLong();
	        return a;
	    }
	}
	static void debug(Object... obj) {
       System.err.println(Arrays.deepToString(obj));
    }
}