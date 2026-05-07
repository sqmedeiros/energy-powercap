//import java.io.IOException;
 
import java.io.*;
import java.util.*;
 
public class  entry_11645571 {
 
 
    static InputReader inputReader=new InputReader(System.in);
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
 
    static class Node
    {
        long maxSum;
        long leftSum;
        long rightSum;
        long totalSum;
 
        Node(long maxSum,long leftSum,long rightSum,long totalSum)
        {
            this.maxSum=maxSum;
            this.leftSum=leftSum;
            this.rightSum=rightSum;
            this.totalSum=totalSum;
        }
 
        public Node()
        {
        }
    }
 
    static void solve() throws IOException
    {
        int n=inputReader.nextInt();
        int q=inputReader.nextInt();
        long arr[]=new long[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=inputReader.nextLong();
 
        }
        SegmentTree segmentTree=new SegmentTree(n,arr);
        segmentTree.buildTree(0,0,n-1);
        for(int i=0;i<q;i++)
        {
            int index=inputReader.nextInt();
            long val=inputReader.nextLong();
            index--;
            segmentTree.updateTree(0,0,n-1,index,val);
            Node ans=segmentTree.query(0,0,n-1,0,n-1);
            out.println(ans.maxSum);
        }
 
    }
 
    static class SegmentTree
    {
        Node st[];
        int n;
        long arr[];
 
        SegmentTree(int n,long arr[])
        {
            st=new Node[4*n];
            this.n=n;
            this.arr=arr;
        }
        Node combineNode(Node left, Node right) {
            Node parent = new Node();
            parent.totalSum = left.totalSum + right.totalSum;
            parent.leftSum = Math.max(left.leftSum, left.totalSum + right.leftSum);
            parent.rightSum = Math.max(right.rightSum, right.totalSum + left.rightSum);
            parent.maxSum = Math.max(Math.max(left.maxSum, right.maxSum), left.rightSum + right.leftSum);
            return parent;
        }
 
        void buildTree(int si,int ss,int se)
        {
            if(ss>se)
            {
                return;
            }
            if(ss==se)
            {
                Node newNode=new Node();
                newNode.leftSum=arr[ss];
                newNode.rightSum=arr[ss];
                newNode.maxSum=Math.max(0,arr[ss]);
                newNode.totalSum=arr[ss];
 
                st[si]=newNode;
                return;
            }
            int mid=(ss+se)/2;
            buildTree(2*si+1,ss,mid);
            buildTree(2*si+2,mid+1,se);
            st[si]=combineNode(st[2*si+1],st[2*si+2]);
        }
 
        Node query(int si, int ss, int se, int qs, int qe) {
            if (qe < ss || qs > se) {
                // Return a node with neutral values
                return new Node(0, 0, 0, 0);
            }
            if (qs <= ss && qe >= se) {
                return st[si];
            }
            int mid = (ss + se) / 2;
            Node left = query(2 * si + 1, ss, mid, qs, qe);
            Node right = query(2 * si + 2, mid + 1, se, qs, qe);
            if (left == null) return right;
            if (right == null) return left;
            return combineNode(left, right);
        }
 
 
        void updateTree(int si,int ss,int se,int index,long val)
        {
            if(ss>se)
            {
                return;
            }
            if(ss==se)
            {
                Node newNode=new Node();
                newNode.leftSum=val;
                newNode.rightSum=val;
                newNode.maxSum=Math.max(0,val);
                newNode.totalSum=val;
                st[si]=newNode;
                return;
            }
            int mid=(ss+se)/2;
            if(index<=mid)
            {
                updateTree(2*si+1,ss,mid,index,val);
 
            }
            else
            {
                updateTree(2*si+2,mid+1,se,index,val);
            }
            st[si]=combineNode(st[2*si+1],st[2*si+2]);
        }
    }
    static PrintWriter out=new PrintWriter((System.out));
    static void SortDec(long arr[])
    {
        List<Long>list=new ArrayList<>();
        for(long ele:arr) {
            list.add(ele);
        }
        Collections.sort(list,Collections.reverseOrder());
        for (int i=0;i<list.size();i++)
        {
            arr[i]=list.get(i);
        }
    }
    static void Sort(long arr[])
    {
        List<Long>list=new ArrayList<>();
        for(long  ele:arr) {
            list.add(ele);
        }
        Collections.sort(list);
        for (int i=0;i<list.size();i++)
        {
            arr[i]=list.get(i);
        }
    }
    public static void main(String args[])throws IOException
    {
 
        solve();
 
        long s = System.currentTimeMillis();
        //    out.println(System.currentTimeMillis()-s+"ms");
        out.close();
    }
    static class InputReader {
 
        private InputStream stream;
        private byte[] buf = new byte[8192];
        private int curChar, snumChars;
        private SpaceCharFilter filter;
 
        public InputReader(InputStream stream) {
            this.stream = stream;
        }
 
        public int snext() {
            if (snumChars == -1)
                throw new InputMismatchException();
            if (curChar >= snumChars) {
                curChar = 0;
                try {
                    snumChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (snumChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }
 
        public int nextInt() {
            int c = snext();
            while (isSpaceChar(c))
                c = snext();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = snext();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = snext();
            } while (!isSpaceChar(c));
            return res * sgn;
        }
 
        public long nextLong() {
            int c = snext();
            while (isSpaceChar(c))
                c = snext();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = snext();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = snext();
            } while (!isSpaceChar(c));
            return res * sgn;
        }
 
        public int[] nextIntArray(int n) {
            int a[] = new int[n];
            for (int i = 0; i < n; i++)
                a[i] = nextInt();
            return a;
        }
 
        public String readString() {
            int c = snext();
            while (isSpaceChar(c))
                c = snext();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = snext();
            } while (!isSpaceChar(c));
            return res.toString();
        }
 
        public boolean isSpaceChar(int c) {
            if (filter != null)
                return filter.isSpaceChar(c);
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
 
        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);
        }
    }
}