import java.lang.*;
import java.io.*;
import java.nio.file.NotLinkException;
import java.util.*;
 
public class entry_3095502 {
 
    static class Reader {
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
//    static class FastReader {
//        BufferedReader br;
//        StringTokenizer st;
//
//        public FastReader()
//        {
//            br = new BufferedReader(
//                    new InputStreamReader(System.in));
//        }
//
//        String next()
//        {
//            while (st == null || !st.hasMoreElements()) {
//                try {
//                    st = new StringTokenizer(br.readLine());
//                }
//                catch (IOException e) {
//                    e.printStackTrace();
//                }
//            }
//            return st.nextToken();
//        }
//
//        int nextInt() { return Integer.parseInt(next()); }
//
//        long nextLong() { return Long.parseLong(next()); }
//
//        double nextDouble()
//        {
//            return Double.parseDouble(next());
//        }
//
//        String nextLine()
//        {
//            String str = "";
//            try {
//                str = br.readLine();
//            }
//            catch (IOException e) {
//                e.printStackTrace();
//            }
//            return str;
//        }
//    }
 
 
    static class Node{
 
        long ans , prefix , suffix , sum;
        int L , R;
        Node left , right;
 
        public Node(long sum, long prefix , long suffix , long ans , int L , int R)
        {
            this.sum = sum;
            this.prefix = prefix;
            this.suffix = suffix;
            this.ans = ans;
            this.L = L;
            this.R = R;
        }
    }
 
    public static void main(String[] args) throws java.lang.Exception {
        try {
            Reader scan = new Reader();
            StringBuilder sb = new StringBuilder();
 
            int N = scan.nextInt();
            int Q = scan.nextInt();
 
            int arr[] = new int[N];
 
            for(int i  = 0;i<N;i++)
                arr[i] = scan.nextInt();
 
            Node head = buildTree(0 , arr.length-1 , arr);
 
            while(Q-- > 0)
            {
                int pos = scan.nextInt();
                int newVal = scan.nextInt();
 
                update(head , pos - 1 , newVal);
 
                sb.append(Math.max(0 , head.ans));
                sb.append("\n");
            }
 
 
            System.out.println(sb);
 
 
        } catch (Exception e) {
            System.out.println(e);
            return;
        }
    }
 
    static Node update(Node head , int pos , int newVal)
    {
 
        if(head.L > pos || head.R < pos)
            return head;
 
        if(head.L == pos && head.R == pos)
        {
            head.prefix = newVal;
            head.suffix = newVal;
            head.ans = newVal;
            head.sum = newVal;
 
            return head;
        }
 
 
        Node left = update(head.left , pos , newVal);
        Node right = update(head.right , pos, newVal);
 
        long prefix = Math.max(left.prefix , left.sum + right.prefix);
        long suffix = Math.max(right.suffix , right.sum + left.suffix);
        long ans = Math.max(left.ans , right.ans);
        long middle = left.suffix + right.prefix;
        ans = Math.max(ans , Math.max(prefix , suffix));
 
        head.sum = left.sum + right.sum;
        head.prefix = prefix;
        head.suffix = suffix;
        head.ans = Math.max(ans , middle);
 
        return head;
    }
 
    static Node buildTree(int l , int r , int arr[])
    {
        if(l == r)
        {
            Node node = new Node(arr[l] , arr[l], arr[l] , arr[l] , l , r);
            return node;
        }
 
        int mid = l + (r - l)/2;
 
        Node left = buildTree(l , mid , arr);
        Node right = buildTree(mid + 1 , r , arr);
 
        long prefix = Math.max(left.prefix , left.sum + right.prefix);
        long suffix = Math.max(right.suffix , right.sum + left.suffix);
        long ans = Math.max(left.ans , right.ans);
        long middle = left.suffix + right.prefix;
        ans = Math.max(ans , Math.max(prefix , suffix));
 
        Node node = new Node(left.sum + right.sum  , prefix , suffix , Math.max(ans , middle),l,r);
        node.left = left;
        node.right = right;
 
        return node;
 
 
    }
}