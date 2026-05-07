import java.io.*;
import java.util.*;
 
public class entry_827896 { 
    static Random random;
 
    /* public static void main(String[] args){
        new Thread(null, new SolutionA (), "Main", 1<<26).start();
    } */
 
    public static void main(String[] args) {
        FastScanner in = new FastScanner();
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        random = new Random();
 
        // long timeStamp = System.currentTimeMillis();
        Solver solver = new Solver();
        solver.solve(in, out);
        out.close();
        // System.err.println("TIME: "+(System.currentTimeMillis()-timeStamp)+" ms");
    }
 
    /* ------------------------------------- START -------------------------------------------- */
    static class Solver {
        public void solve(FastScanner in, PrintWriter out) {
            int n = in.nextInt(), q = in.nextInt();
            int input[] = new int[n];
            for(int i = 0; i<n; i++){
                input[i] = in.nextInt();
            }
 
            SegTree segTree = new SegTree(0, n-1, input);
 
            for(int i = 0; i<q; i++){
                int k = in.nextInt()-1, x = in.nextInt();
                segTree.update(k, x);
                out.println(segTree.best);
            }
        }
 
        private static class SegTree {
            int L, R;
            SegTree left, right;
            long best = 0, leftBest = 0, rightBest = 0, sum = 0;
            SegTree(int L, int R, int[] arr){
                this.L = L; this.R = R;
                if(L == R) {
                    sum = arr[L];
                    best = (arr[L] < 0)? 0 : arr[L];
                    leftBest = best;
                    rightBest = best;
                }
                else{
                    int mid = (L+R)>>1;
                    left = new SegTree(L, mid, arr);
                    right = new SegTree(mid+1, R, arr);
                    recalc();
                }
            }
    
            private void recalc() {                 //Two childs merging
                sum = left.sum + right.sum;
                best = Math.max(left.best, right.best);
                best = Math.max(best, left.rightBest + right.leftBest);
                leftBest = Math.max(left.leftBest, left.sum + right.leftBest);
                rightBest = Math.max(right.rightBest, right.sum + left.rightBest);
            }
    
            void update(int index, int value){
                if(L == R){
                    sum = value;
                    best = (value < 0)? 0 : value;
                    leftBest = best;
                    rightBest = best;
                    return;
                }
                if(index <= left.R) left.update(index, value);
                else right.update(index, value);
                recalc();
            }
    
            // long query(int l, int r){
            //     if(r < L || R < l) return 0;        // return identity
            //     if(l <= L && R <= r) return sum;
            //     long p = left.query(l, r);
            //     long q = right.query(l, r);
            //     return p+q;                         // return sum of two childs
            // }
        }
        
    }
    /* -------------------------------------- END --------------------------------------------- */
 
    /* Shuffle function to shuffle before Arrays.sort */
    static void shuffle(int[] arr){
        int swapTemp;
        for(int i = arr.length-1; i>= 1; i--){
            int pos = random.nextInt(i+1);
            if(pos == i) continue;
            {swapTemp = arr[i]; arr[i] = arr[pos]; arr[pos] = swapTemp;}
        }
    }
 
    /* Fast Input reader */
    static class FastScanner {
        BufferedReader reader;
        StreamTokenizer tokenizer;
        public FastScanner() {
            reader = new BufferedReader(new InputStreamReader(System.in));
            tokenizer = new StreamTokenizer(reader);
            tokenizer.resetSyntax();
            tokenizer.whitespaceChars(0, 32);
            tokenizer.wordChars(33, 126);
        }
        private void nextToken(){
            try{ tokenizer.nextToken(); }
            catch (Exception e) { e.printStackTrace(); }
        }
        String next() {
            nextToken();
            return tokenizer.sval;
        }
        int nextInt() {
            nextToken();
            return Integer.parseInt(tokenizer.sval);
        }
        long nextLong() {
            nextToken();
            return Long.parseLong(tokenizer.sval);
        }
        double nextDouble() {
            nextToken();
            return Double.parseDouble(tokenizer.sval);
        }
        String nextLine() {
            try{
                String string = reader.readLine();
                return string;
            } catch (Exception e) {
                e.printStackTrace();
                return "";
            }
        }
    }
}