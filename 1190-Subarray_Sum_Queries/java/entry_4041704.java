import java.io.*;
import java.util.*;
 
public class entry_4041704 {
 static BufferedReader bf;
 static PrintWriter out;
 static Scanner sc;
 static StringTokenizer st;
    
	public static void main (String[] args)throws IOException {
     bf = new BufferedReader(new InputStreamReader(System.in));
     out = new PrintWriter(System.out);
     sc = new Scanner(System.in);
 
	// int t = Integer.parseInt(bf.readLine());
    
    // while(t-->0){
        solve();
       
    // }
    
}
 
 
 public static void solve() throws IOException{
  int n = nextInt();
  int N = findN(n);
  int q = nextInt();
  int []arr = new int[n];
  for(int i  =0;i<n;i++){
      arr[i] = nextInt();
  }
  long[][]tree = new long[N*2][4];
 
  for(int i = 0;i<n;i++){
      tree[N+i][0] = arr[i];
      tree[N+i][1] = arr[i];
      tree[N+i][2] = arr[i];
      tree[N+i][3] = arr[i];
  }
  for(int i = N-1;i>=1;i--){
      tree[i][0] = tree[i*2][0] + tree[i*2+1][0];
      tree[i][1] = Math.max(tree[i*2][1],tree[i*2][0]+tree[i*2+1][1]);
      tree[i][2] = Math.max(tree[i*2+1][2],tree[i*2+1][0] + tree[i*2][2]);
      tree[i][3] = Math.max(tree[i*2+1][1]+tree[i*2][2],Math.max(tree[i*2][3],tree[i*2+1][3]));
  }
  for(int i = 0;i<q;i++){
   int index = nextInt();
   int value = nextInt();
   index-- ;
   index = index+N;
   tree[index][0] = value;
   tree[index][1] = value;
   tree[index][2] = value;
   tree[index][3] = value;
   index /=2;
   while(index > 0){
    tree[index][0] = tree[index*2][0] + tree[index*2+1][0];
    tree[index][1] = Math.max(tree[index*2][1],tree[index*2][0]+tree[index*2+1][1]);
    tree[index][2] = Math.max(tree[index*2+1][2],tree[index*2+1][0] + tree[index*2][2]);
    tree[index][3] = Math.max(tree[index*2+1][1]+tree[index*2][2],Math.max(tree[index*2][3],tree[index*2+1][3]));
    index /=2;
 
   }
   if(tree[1][3] < 0){
       out.println(0);
   }
   else{
       out.println(tree[1][3]);
   }
 
  }
 
 
 
 
  out.flush();
  
}
public static long[] findPrefix(int node,int low,int high,int tlow,int thigh,long [][]tree){
    if(low >= tlow && high <= thigh)return new long[]{tree[node][0],tree[node][1],tree[node][2],tree[node][3]};
    if(high < tlow || low > thigh)return new long[]{0,0,0,0};
    int mid = (low+high)/2;
    long left[] = findPrefix(node*2,low,mid,tlow,thigh,tree);
    long right[] = findPrefix(node*2+1,mid+1,high,tlow,thigh,tree);
    return new long[]{left[0]+right[0],Math.max(left[0]+right[1],left[1]),Math.max(right[0]+left[2],right[2]),Math.max(left[2]+right[1],Math.max(left[3],right[3]))};
}
 
 
public static boolean isSorted(int[]arr){
    for(int i =1;i<arr.length;i++){
        if(arr[i] < arr[i-1]){
            return false;
        }
 
    }
    return true;
}
 
   
 
 
 
 
 
 
 
    //function to find the topological sort of the a DAG
    public static boolean hasCycle(int[]indegree,List<List<Integer>>list,int n,List<Integer>topo){
        Queue<Integer>q  = new LinkedList<>();
        for(int i =1;i<indegree.length;i++){
            if(indegree[i] == 0){
                q.add(i);
                topo.add(i);
            }
        }
        while(!q.isEmpty()){
            int cur = q.poll();
           
            List<Integer>l = list.get(cur);
            for(int i = 0;i<l.size();i++){
                indegree[l.get(i)]--;
                if(indegree[l.get(i)] == 0){
                    q.add(l.get(i));
                    topo.add(l.get(i));
                }
            }
        }
       if(topo.size() == n)return false;
        return true;
    }
 
 
 
 
    // function to find the parent of any given node with path compression in DSU 
 public static int find(int val,int[]parent){
     if(val == parent[val])return val;
     return parent[val] = find(parent[val],parent);
 }
 
 
 // function to connect two components
 public static void union(int[]rank,int[]parent,int u,int v){
     int a = find(u,parent);
     int b= find(v,parent);
     if(a == b)return;
     if(rank[a] == rank[b]){
         parent[b] = a;
         rank[a]++;
     }
     else{
         if(rank[a] > rank[b]){
             parent[b] = a;
         }
         else{
             parent[a] = b;
         }
     }
 }
 //
 public static int findN(int n){
     int num = 1;
     while(num < n){
         num *=2;
     }
     return num;
 }
 
 
 
 
 
   // code for input
  
   public static void  print(String s ){
     System.out.print(s);
   }
   public static void  print(int num ){
     System.out.print(num);
   }
   public static void  print(long num ){
     System.out.print(num);
   }
   public static void println(String s){
       System.out.println(s);
   }
   public static void println(int num){
       System.out.println(num);
   }
   public static void println(long num){
       System.out.println(num);
   }
   public static void println(){
       System.out.println();
   }
 
   public static int Int(String s){
       return Integer.parseInt(s);
   }
   public static long Long(String s){
       return Long.parseLong(s);
   }
   public static String[] nextStringArray()throws IOException{
       return  bf.readLine().split(" ");
   }
   
 
   public static String nextString()throws IOException{
       return bf.readLine();
   }
  
   public static long[] nextLongArray(int n)throws IOException{
       String[]str = bf.readLine().split(" ");
       long[]arr = new long[n];
       for(int i =0;i<n;i++){
           arr[i] = Long.parseLong(str[i]);
       }
       return arr;
   }
   public static int[][] newIntMatrix(int r,int c)throws IOException{
       int[][]arr = new int[r][c];
       for(int i =0;i<r;i++){
           String[]str = bf.readLine().split(" ");
           for(int j =0;j<c;j++){
               arr[i][j] = Integer.parseInt(str[j]);
           }
         }
         return arr;
   }
 
   public static long[][] newLongMatrix(int r,int c)throws IOException{
       long[][]arr = new long[r][c];
       for(int i =0;i<r;i++){
           String[]str = bf.readLine().split(" ");
           for(int j =0;j<c;j++){
               arr[i][j] = Long.parseLong(str[j]);
           }
         }
         return arr;
   }
 
   static class pair{
       int one;
       int two;
       pair(int one,int two){
           this.one = one ;
           this.two =two;
       }
   }
   public static long gcd(long a,long b){
    if(b == 0)return a;
    return gcd(b,a%b);
}
 
 
public static long lcm(long a,long b){
    return (a*b)/(gcd(a,b));
}
public static boolean isPalindrome(String s){
    int i = 0;
    int j = s.length()-1;
    while(i<=j){
        if(s.charAt(i) != s.charAt(j)){
            return false;
        }
        i++;
        j--;
    }
    return true;
}
 
// these functions are to calculate the number of smaller elements after self
public static void sort(int[]arr,int l,int r){
    if(l < r){
        int mid  = (l+r)/2;
        sort(arr,l,mid);
        sort(arr,mid+1,r);
        smallerNumberAfterSelf(arr, l, mid, r);
    }
}
public static void smallerNumberAfterSelf(int[]arr,int l,int mid,int r){
    int n1 = mid - l +1;
    int n2 = r - mid;
    int []a = new int[n1];
    int[]b = new int[n2];
    for(int i = 0;i<n1;i++){
        a[i] = arr[l+i];
    }
    for(int i =0;i<n2;i++){
        b[i] = arr[mid+i+1];
    }
    int i = 0;
    int j =0;
    int k = l;
    while(i<n1 && j < n2){
        if(a[i] < b[j]){
            arr[k++] = a[i++];
        }
        else{
            arr[k++] = b[j++];
        }
 
    }
    while(i<n1){
        arr[k++] = a[i++];
    }
    while(j<n2){
        arr[k++] = b[j++];
    }
    
    
    
}
public static String next(){
    while (st == null || !st.hasMoreElements()) {
        try {
            st = new StringTokenizer(bf.readLine());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    return st.nextToken();
}
static int nextInt() {
    return Integer.parseInt(next());
}
 
static long nextLong() {
    return Long.parseLong(next());
}
 
static double nextDouble() {
    return Double.parseDouble(next());
}
 
static String nextLine(){
    String str = "";
try {
   str = bf.readLine();
} catch (IOException e) {
   e.printStackTrace();
}
return str;
}
 
}
 
 
 
// use some math tricks it might help
// sometimes just try to think in straightforward plan in A and B problems don't always complecate the questions with thinking too much differently 
// always use long number to do 10^9+7 modulo 
// if a problem is related to binary string it could also be related to parenthesis
// *****try to use binary search(it is a very beautiful thing it can work in some of the very unexpected problems ) in the question it might work******
// try sorting
// try to think in opposite direction of question it might work in your way
// if a problem is related to maths try to relate some of the continuous subarray with variables like - > a+b+c+d or a,b,c,d in general 
 
// if the question is to much related to left and/or right side of any element in an array then try monotonic stack it could work.
// in range query sums try to do binary search it could work
// analyse the time complexity of program thoroughly
// anylyse the test cases properly
// if we divide any number by 2 till it gets 1 then there will be (number - 1) operation required 
// try to do the opposite operation of what is given in the problem
//think about the base cases properly
//If a question is related to numbers try prime factorisation or something related to number theory
// keep in mind unique strings 
//you can calculate the number of inversion in O(n log n)
// in a matrix you could sometimes think about row and cols indenpendentaly.
// Try to think in more constructive(means a way to look through various cases of a problem) way.
// observe the problem carefully the answer could be hidden in the given test cases itself. (A, B , C);
// when we have equations like (a+b = N) and we have to find the max of (a*b) then the values near to the N/2 must be chosen as (a and b);