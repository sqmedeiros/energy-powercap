import java.io.*;
import java.util.*;
 
public class  entry_16564378 {
 
    static long[] sum, pref, suff, best;
    static int n;
 
    static void build(long[] arr, int idx, int l, int r) {
 
        if (l == r) {
            sum[idx] = arr[l];
            pref[idx] = Math.max(0, arr[l]);
            suff[idx] = Math.max(0, arr[l]);
            best[idx] = Math.max(0, arr[l]);
            return;
        }
 
        int mid = (l + r) / 2;
 
        build(arr, idx * 2 + 1, l, mid);
        build(arr, idx * 2 + 2, mid + 1, r);
 
        int L = idx * 2 + 1;
        int R = idx * 2 + 2;
 
        sum[idx] = sum[L] + sum[R];
        pref[idx] = Math.max(pref[L], sum[L] + pref[R]);
        suff[idx] = Math.max(suff[R], sum[R] + suff[L]);
        best[idx] = Math.max(Math.max(best[L], best[R]), suff[L] + pref[R]);
    }
 
    static void update(int idx, int l, int r, int pos, long val) {
 
        if (l == r) {
            sum[idx] = val;
            pref[idx] = Math.max(0, val);
            suff[idx] = Math.max(0, val);
            best[idx] = Math.max(0, val);
            return;
        }
 
        int mid = (l + r) / 2;
 
        if (pos <= mid)
            update(idx * 2 + 1, l, mid, pos, val);
        else
            update(idx * 2 + 2, mid + 1, r, pos, val);
 
        int L = idx * 2 + 1;
        int R = idx * 2 + 2;
 
        sum[idx] = sum[L] + sum[R];
        pref[idx] = Math.max(pref[L], sum[L] + pref[R]);
        suff[idx] = Math.max(suff[R], sum[R] + suff[L]);
        best[idx] = Math.max(Math.max(best[L], best[R]), suff[L] + pref[R]);
    }
 
    public static void main(String[] args) throws Exception {
 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
 
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
 
        long[] arr = new long[n];
 
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
            arr[i] = Long.parseLong(st.nextToken());
 
        sum = new long[4 * n];
        pref = new long[4 * n];
        suff = new long[4 * n];
        best = new long[4 * n];
 
        build(arr, 0, 0, n - 1);
 
        StringBuilder sb = new StringBuilder();
 
        while (m-- > 0) {
 
            st = new StringTokenizer(br.readLine());
 
            int k = Integer.parseInt(st.nextToken()) - 1;
            long x = Long.parseLong(st.nextToken());
 
            update(0, 0, n - 1, k, x);
 
            sb.append(best[0]).append("\n");
        }
 
        System.out.print(sb);
    }
}