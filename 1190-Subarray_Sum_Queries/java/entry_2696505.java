import java.util.*;
import java.io.*;
import java.math.*;
import java.lang.*;
 
public class entry_2696505 {
	
	public static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
 
        public Reader()
        {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public Reader(String file_name) throws IOException
        {
            din = new DataInputStream(
                new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public String readLine() throws IOException
        {
            byte[] buf = new byte[64]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n') {
                    if (cnt != 0) {
                        break;
                    }
                    else {
                        continue;
                    }
                }
                buf[cnt++] = (byte)c;
            }
            return new String(buf, 0, cnt);
        }
 
        public int nextInt() throws IOException
        {
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
 
        public long nextLong() throws IOException
        {
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
 
        public double nextDouble() throws IOException
        {
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
 
        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0,
                                 BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }
 
        private byte read() throws IOException
        {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }
 
        public void close() throws IOException
        {
            if (din == null)
                return;
            din.close();
        }
    }
 
    public static class Pair{
    	long pfsum;
    	long sfsum;
    	long tsum;
    	long msum;
 
    	Pair(long pfsum, long sfsum, long tsum, long msum){
    		this.pfsum = pfsum;
    		this.sfsum = sfsum;
    		this.tsum = tsum;
    		this.msum = msum;
    	}
    }
 
    private static Pair merge(Pair left, Pair right){
    	Pair pair = new Pair(0L, 0L, 0L, 0L);
    	pair.pfsum = Math.max(left.pfsum, left.tsum + right.pfsum);
    	pair.sfsum = Math.max(right.sfsum, right.tsum + left.sfsum);
    	pair.tsum = left.tsum + right.tsum;
    	pair.msum = Math.max(Math.max(left.msum, right.msum), left.sfsum + right.pfsum);
    	return pair;
    }
 
    public static void buildTree(long[] arr, int si, int ei, Pair[] tree, int idx){
    	if(si == ei){
    		tree[idx] = new Pair(arr[si], arr[si], arr[si], arr[si]);
    		return;
    	}
    	int mid = si + (ei - si) / 2;
    	buildTree(arr, si, mid, tree, 2*idx);
    	buildTree(arr, mid+1, ei, tree, 2*idx+1);
    	tree[idx] = merge(tree[2*idx], tree[2*idx+1]);
    }
 
    private static void update(Pair[] tree, int si, int ei, int i, long update, int idx){
    	if(i < si || i > ei){
    		return;
    	}
    	if(si == ei){
    		tree[idx] = new Pair(update, update, update, update);
    		return;
    	}
    	int mid = si + (ei - si) / 2;
    	update(tree, si, mid, i, update, 2*idx);
    	update(tree, mid+1, ei, i, update, 2*idx+1);
    	tree[idx] = merge(tree[2*idx], tree[2*idx+1]);
    }
 
	public static void main(String[] args) throws Exception {
		Reader scn = new Reader();
		PrintWriter pw = new PrintWriter(System.out); 
		int n = scn.nextInt();
		int m = scn.nextInt();
		long[] arr = new long[n];
		for(int i=0; i<n; i++){
			arr[i] = scn.nextLong();
		}
		Pair[] tree = new Pair[4*n+1];
		buildTree(arr, 0, n-1, tree, 1);
		while(m-->0){
			int k = scn.nextInt();
			long x = scn.nextLong();
			update(tree, 0, n-1, k-1, x, 1);
			long ans = tree[1].msum;
			if(ans < 0){
				pw.println(0);
			}else{
				pw.println(ans);
			}
		}
		pw.close();
	}
}