import java.io.*;
import java.util.*;
 
class FastIO extends PrintWriter{
    private InputStream stream;private byte[]buf=new byte[1<<16];
    private int curChar,numChars;public FastIO(){this(System.in,System.out);}
    public FastIO(InputStream i,OutputStream o){super(o);stream=i;}
    public FastIO(String i,String o)throws IOException{super(new FileWriter(o));stream=new FileInputStream(i);}
    private int nextByte(){if(numChars==-1)throw new InputMismatchException();if(curChar>=numChars){curChar=0;try{numChars=stream.read(buf);}catch(IOException e){throw new InputMismatchException();}if(numChars==-1)return -1;}return buf[curChar++];}
    public String nextLine(){int c;do{c=nextByte();}while(c<='\n');StringBuilder res=new StringBuilder();do{res.appendCodePoint(c);c=nextByte();}while(c>'\n');return res.toString();}
    public String next(){int c;do{c=nextByte();}while(c<=' ');StringBuilder res=new StringBuilder();do{res.appendCodePoint(c);c=nextByte();}while(c>' ');return res.toString();}
    public int nextInt(){int c;do{c=nextByte();}while(c<=' ');int sgn=1;if(c=='-'){sgn=-1;c=nextByte();}int res=0;do{if(c<'0'||c>'9')throw new InputMismatchException();res=10*res+c-'0';c=nextByte();}while(c>' ');return res * sgn;}
    public long nextLong(){int c;do{c=nextByte();}while(c<=' ');long sgn=1;if(c=='-'){sgn=-1;c=nextByte();}long res=0;do{if(c<'0'||c>'9')throw new InputMismatchException();res=10*res+c-'0';c=nextByte();}while(c>' ');return res * sgn;}
    public double nextDouble(){return Double.parseDouble(next());
    }
}
 
class Node{
    long maxSubArray;
    long maxPrefix;
    long maxSuffix;
    long sum;
 
 
    Node(long maxSubArray,long maxPrefix,long maxSuffix,long sum){
        this.maxSubArray=maxSubArray;
        this.maxPrefix=maxPrefix;
        this.maxSuffix=maxSuffix;
        this.sum=sum;
        
    }
 
}
class SegmentTree{
    Node tree[];
    SegmentTree(int n){
        tree=new Node[4*n];
    }
 
    public Node combine(Node left,Node right){
        long sum=left.sum+right.sum;
        long maxPrefix=Math.max(left.maxPrefix,Math.max(left.sum+right.maxPrefix,sum));
        long maxSuffix=Math.max(right.maxSuffix,Math.max(right.sum+left.maxSuffix,sum));
        long crossSum = left.maxSuffix + right.maxPrefix; // Max subarray crossing the middle
        long maxSubArray = Math.max(maxPrefix,
                    Math.max(maxSuffix,
                    Math.max(crossSum, 
                             Math.max(left.maxSubArray, right.maxSubArray))));
 
        return new Node(maxSubArray,maxPrefix,maxSuffix,sum);
   
    }
 
    public void buildSt(int i,int si,int sj,int arr[]){
        if(si==sj){
            if(arr[si]<0){
                tree[i]=new Node(0,0,0,arr[si]);
            }else{
                tree[i]=new Node(arr[si],arr[si],arr[si],arr[si]);
 
            }
            return;
            
        }
 
        int mid=(si+sj)/2;
        buildSt(2*i+1,si,mid,arr);
        buildSt(2*i+2,mid+1,sj,arr);
        tree[i]=combine(tree[2*i+1],tree[2*i+2]);
    }
 
    public void update(int i,int si,int sj,int index,int newVal){
        if(si==sj&&si==index){
            if(newVal<0){
                tree[i]=new Node(0,0,0,newVal);
            }else{
                tree[i]=new Node(newVal,newVal,newVal,newVal);
 
            }
            return;
        }
        int mid=(si+sj)/2;
        if(index<=mid){
            update(2*i+1, si,mid, index, newVal);
        }else{
            update(2*i+2,mid+1,sj,index,newVal);
        }
        tree[i]=combine(tree[2*i+1], tree[2*i+2]);
    }
 
}
 
public class  entry_11703954 {
    static FastIO sc = new FastIO();
 
    public static void main(String args[]){
        int n=sc.nextInt();
        int q=sc.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        SegmentTree st=new SegmentTree(n);
        st.buildSt(0, 0, n-1, arr);
        for(int i=0;i<q;i++){
            int k=sc.nextInt()-1;
            int x=sc.nextInt();
            st.update(0,0,n-1,k,x);
            sc.println(st.tree[0].maxSubArray);
        }
 
        sc.close();
    }
}