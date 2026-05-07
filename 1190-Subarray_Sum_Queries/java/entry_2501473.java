import java.util.*;
import java.io.*;
public class entry_2501473 {
    public static void main(String[] args) throws IOException {
        Reader in = new Reader();
        PrintWriter out = new PrintWriter(System.out);
        
        int N = in.nextInt(), Q = in.nextInt();
        int M = 1;
        while (M < N) {
            M <<= 1;
        }
        long[] sum = new long[M * 2], left = new long[M * 2], right = new long[M * 2], max = new long[M * 2];
        for (int i = 0; i < M; i++) {
            int n = i < N ? in.nextInt() : 0;
            sum[i + M] = n;
            left[i + M] = n;
            right[i + M] = n;
            max[i + M] = Math.max(0, n);
        }
        for (int i = M - 1; i > 0; i--) {
            sum[i] = sum[i * 2] + sum[i * 2 + 1];
            left[i] = Math.max(left[i * 2], sum[i * 2] + left[i * 2 + 1]);
            right[i] = Math.max(right[i * 2 + 1], sum[i * 2 + 1] + right[i * 2]);
            max[i] = Math.max(Math.max(max[i * 2], max[i * 2 + 1]), right[i * 2] + left[i * 2 + 1]);
        }
        for (int q = 0; q < Q; q++) {
            int i = in.nextInt() - 1 + M, n = in.nextInt();
            sum[i] = n;
            left[i] = n;
            right[i] = n;
            max[i] = Math.max(0, n);
            i >>= 1;
            while (i > 0) {
                sum[i] = sum[i * 2] + sum[i * 2 + 1];
                left[i] = Math.max(left[i * 2], sum[i * 2] + left[i * 2 + 1]);
                right[i] = Math.max(right[i * 2 + 1], sum[i * 2 + 1] + right[i * 2]);
                max[i] = Math.max(Math.max(max[i * 2], max[i * 2 + 1]), right[i * 2] + left[i * 2 + 1]);
                i >>= 1;
            }
            out.println(max[1]);
        }
        
        out.close();
    }
    static class Reader {
        BufferedInputStream in;
        public Reader() {
            in = new BufferedInputStream(System.in);
        }
        public String nextLine() throws IOException {
            int c;
            StringBuilder sb = new StringBuilder("");
            while ((c = in.read()) != '\n')
                sb.append((char)(c));
            return sb.toString();
        }
        public String next() throws IOException {
            int c;
            StringBuilder sb = new StringBuilder("");
            while ((c = in.read()) != ' ' && c != '\n')
                sb.append((char)(c));
            return sb.toString();
        }
        public int nextInt() throws IOException {
            return (int)nextLong();
        }
        public long nextLong() throws IOException {
            int c;
            long res = 0;
            boolean start = false, negative = false;
            while ((c = in.read()) != ' ' && c != '\n' || !start)
                if (c >= '0' && c <= '9' || c == '-') {
                    start = true;
                    if (c == '-')
                        negative = true;
                    else
                        res = res * 10 + c - '0';
                }
            return res * (negative ? -1 : 1);
        }
    }
    public static void sort(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int i : arr) {
            list.add(i);
        }
        Collections.sort(list);
        for (int i = 0; i < arr.length; i++) {
            arr[i] = list.get(i);
        }
    }
}