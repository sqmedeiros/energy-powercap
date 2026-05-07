//package CSES.RangeQueries;
 
import java.io.*;import java.util.*;import java.math.*;
public class entry_1228044
{
    static long mod=1000000007l;
    static int max=Integer.MAX_VALUE,min=Integer.MIN_VALUE;
    static long maxl=Long.MAX_VALUE,minl=Long.MIN_VALUE;
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out=new PrintWriter(System.out);
    static StringTokenizer st;
    static StringBuilder sb;
 
    static class node{
        long sum,prefixsum,suffixsum,maxsum ;
    };
    static node[] seg ;
    static long[] a ;
 
    static void build(long[] a,int s,int e,int tind) {
        if (s == e) {
            seg[tind].sum = a[s - 1];
            seg[tind].prefixsum = a[s - 1];
            seg[tind].suffixsum = a[s - 1];
            seg[tind].maxsum = a[s - 1];
            return;
        }
        int mid = (s + e) / 2;
        build(a, s, mid, 2 * tind);
        build(a, mid + 1, e, 2 * tind + 1);
        seg[tind].sum = seg[2 * tind ].sum + seg[2 * tind + 1].sum;
        seg[tind].prefixsum = Math.max(seg[2 * tind].prefixsum, seg[2 * tind].sum + seg[2 * tind + 1].prefixsum);
        seg[tind].suffixsum = Math.max(seg[2 * tind + 1].suffixsum, seg[2 * tind + 1].sum + seg[2 * tind ].suffixsum);
        seg[tind].maxsum = Math.max(seg[tind].prefixsum, Math.max(seg[tind].suffixsum, Math.max(seg[2 * tind].maxsum, Math.max(seg[2 * tind + 1].maxsum, seg[2 * tind ].suffixsum + seg[2 * tind + 1].prefixsum))));
 
    }
    static void update(int s,int e,int tind,int ind,int val) {
        if (s == e) {
            seg[tind].sum = val;
            seg[tind].prefixsum = val;
            seg[tind].suffixsum = val;
            seg[tind].maxsum = val;
        } else {
            int mid = (s + e) / 2;
            if (ind > mid) update(mid + 1, e, 2 * tind + 1, ind, val);
            else update(s, mid, 2 * tind, ind, val);
            seg[tind].sum = seg[2 * tind].sum + seg[2 * tind + 1].sum;
            seg[tind].prefixsum = Math.max(seg[2 * tind].prefixsum, seg[2 * tind].sum + seg[2 * tind + 1].prefixsum);
            seg[tind].suffixsum = Math.max(seg[2 * tind + 1].suffixsum, seg[2 * tind + 1].sum + seg[2 * tind].suffixsum);
            seg[tind].maxsum = Math.max(seg[tind].prefixsum, Math.max(seg[tind].suffixsum, Math.max(seg[2 * tind].maxsum, Math.max(seg[2 * tind + 1].maxsum, seg[2 * tind].suffixsum + seg[2 * tind + 1].prefixsum))));
        }
    }
    static node query(int s, int e,int tind,int l, int r) {
        node result = new node();
        result.sum = result.prefixsum = result.suffixsum = result.maxsum = min;
        if(s>r || e<l) return result ;
        if(s>=l && e<=r) return seg[tind];
        int mid = (s+e) / 2;
        if (l > mid) return query(mid+1,e,2*tind+1,l,r);
        if (r <= mid) return query(s,mid,2*tind,l,r);
 
        node left = query(s,mid,2*tind,l,r);
        node right = query(mid+1,e,2*tind+1,l,r);
        result.sum = left.sum + right.sum;
        result.prefixsum = max(left.prefixsum, left.sum + right.prefixsum);
        result.suffixsum = max(right.suffixsum, right.sum + left.suffixsum);
        result.maxsum = max(result.prefixsum, max(result.suffixsum, max(left.maxsum, max(right.maxsum, left.suffixsum + right.prefixsum))));
 
        return result;
    }
 
    static public void main(String[] args)throws Exception
    {
        st=new StringTokenizer(br.readLine());
        sb=new StringBuilder(1000000);
        int t=1 ;
        while(t-->0) {
            int n =i() , q=i() ;
            a = arl(n) ;
            seg = new node[4*n] ;
            for(int i=0;i<4*n;i++) seg[i] = new node();
            build(a,1,n,1);
            while (q-->0){
                int ind=i() , val=i() ;
                update(1,n,1,ind,val);
                sl((query(1,n,1,1,n).maxsum < 0) ? 0:query(1,n,1,1,n).maxsum  );
            }
        }
        p(sb);
    }
 
    static void s(String s){sb.append(s);}
    static void s(int s){sb.append(s);}
    static void s(long s){sb.append(s);}
    static void s(char s){sb.append(s);}
    static void s(double s){sb.append(s);}
    static void ss(){sb.append(' ');}
    static void sl(String s){sb.append(s);sb.append("\n");}
    static void sl(int s){sb.append(s);sb.append("\n");}
    static void sl(long s){sb.append(s);sb.append("\n");}
    static void sl(char s){sb.append(s);sb.append("\n");}
    static void sl(double s){sb.append(s);sb.append("\n");}
    static void sl(){sb.append("\n");}
    static int max(int a,int b){return a>b?a:b;}
    static int min(int a,int b){return a<b?a:b;}
    static int abs(int a){return Math.abs(a);}
    static int floor(int a){return (int)Math.floor(a);}
    static int ceil(int a){return (int)Math.ceil(a);}
    static long max(long a,long b){return a>b?a:b;}
    static long min(long a,long b){return a<b?a:b;}
    static long abs(long a){return Math.abs(a);}
    static int sq(int a){return (int)Math.sqrt(a);}
    static long sq(long a){return (long)Math.sqrt(a);}
    static int gcd(int a,int b){return b==0?a:gcd(b,a%b);}
    static boolean pa(String s,int i,int j)
    {
        while(i<j)if(s.charAt(i++)!=s.charAt(j--))return false;
        return true;
    }
    static int ncr(int n,int c,long m)
    {
        long a=1l;
        for(int x=n-c+1;x<=n;x++)a=((a*x)%m);
        long b=1l;
        for(int x=2;x<=c;x++)b=((b*x)%m);
        return (int)((a*(mul((int)b,m-2,m)%m))%m);
    }
    static boolean[] sieve(int n)
    {
        boolean bo[]=new boolean[n+1];
        bo[0]=true;bo[1]=true;
        for(int x=4;x<=n;x+=2)bo[x]=true;
        for(int x=3;x*x<=n;x+=2)if(!bo[x])for(int y=x*x;y<=n;y+=x)bo[y]=true;
        return bo;
    }
    static long fac(long n){
        if(n==0 || n==1) return 1 ;
        else return 1L*n*fac(n-1) ;
    }
    static long mul(long a,long b,long m)
    {
        long r=1l;
        a%=m;
        while(b>0)
        {
            if((b&1)==1)r=(r*a)%m;
            b>>=1;
            a=(a*a)%m;
        }
        return r;
    }
    static int i()throws IOException
    {
        if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
        return Integer.parseInt(st.nextToken());
    }
    static long l()throws IOException
    {
        if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
        return Long.parseLong(st.nextToken());
    }
    static String s()throws IOException
    {
        if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
        return st.nextToken();
    }
    static double d()throws IOException
    {
        if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
        return Double.parseDouble(st.nextToken());
    }
    static void p(Object p){System.out.print(p);}
    static void p(String p){System.out.print(p);}
    static void p(int p){System.out.print(p);}
    static void p(double p){System.out.print(p);}
    static void p(long p){System.out.print(p);}
    static void p(char p){System.out.print(p);}
    static void p(boolean p){System.out.print(p);}
    static void pl(Object p){System.out.println(p);}
    static void pl(String p){System.out.println(p);}
    static void pl(int p){System.out.println(p);}
    static void pl(char p){System.out.println(p);}
    static void pl(double p){System.out.println(p);}
    static void pl(long p){System.out.println(p);}
    static void pl(boolean p){System.out.println(p);}
    static void pl(){System.out.println();}
    static int[] ari(int n)throws IOException
    {
        int ar[]=new int[n];
        if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
        for(int x=0;x<n;x++)ar[x]=Integer.parseInt(st.nextToken());
        return ar;
    }
    static int[][] ari(int n,int m)throws IOException
    {
        int ar[][]=new int[n][m];
        for(int x=0;x<n;x++)
        {
            if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
            for(int y=0;y<m;y++)ar[x][y]=Integer.parseInt(st.nextToken());
        }
        return ar;
    }
    static long[] arl(int n)throws IOException
    {
        long ar[]=new long[n];
        if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
        for(int x=0;x<n;x++) ar[x]=Long.parseLong(st.nextToken());
        return ar;
    }
    static long[][] arl(int n,int m)throws IOException
    {
        long ar[][]=new long[n][m];
        for(int x=0;x<n;x++)
        {
            if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
            for(int y=0;y<m;y++)ar[x][y]=Long.parseLong(st.nextToken());
        }
        return ar;
    }
    static String[] ars(int n)throws IOException
    {
        String ar[]=new String[n];
        if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
        for(int x=0;x<n;x++) ar[x]=st.nextToken();
        return ar;
    }
    static double[] ard(int n)throws IOException
    {
        double ar[]=new double[n];
        if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
        for(int x=0;x<n;x++)ar[x]=Double.parseDouble(st.nextToken());
        return ar;
    }
    static double[][] ard(int n,int m)throws IOException
    {
        double ar[][]=new double[n][m];
        for(int x=0;x<n;x++)
        {
            if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
            for(int y=0;y<m;y++)ar[x][y]=Double.parseDouble(st.nextToken());
        }
        return ar;
    }
    static char[] arc(int n)throws IOException
    {
        char ar[]=new char[n];
        if(!st.hasMoreTokens())st=new StringTokenizer(br.readLine());
        for(int x=0;x<n;x++)ar[x]=st.nextToken().charAt(0);
        return ar;
    }
    static char[][] arc(int n,int m)throws IOException
    {
        char ar[][]=new char[n][m];
        for(int x=0;x<n;x++)
        {
            String s=br.readLine();
            for(int y=0;y<m;y++)ar[x][y]=s.charAt(y);
        }
        return ar;
    }
    static void p(int ar[])
    {
        StringBuilder sb=new StringBuilder(2*ar.length);
        for(int a:ar)
        {
            sb.append(a);
            sb.append(' ');
        }
        System.out.println(sb);
    }
    static void p(int ar[][])
    {
        StringBuilder sb=new StringBuilder(2*ar.length*ar[0].length);
        for(int a[]:ar)
        {
            for(int aa:a)
            {
                sb.append(aa);
                sb.append(' ');
            }
            sb.append("\n");
        }
        p(sb);
    }
    static void p(long ar[])
    {
        StringBuilder sb=new StringBuilder(2*ar.length);
        for(long a:ar)
        {
            sb.append(a);
            sb.append(' ');
        }
        System.out.println(sb);
    }
    static void p(long ar[][])
    {
        StringBuilder sb=new StringBuilder(2*ar.length*ar[0].length);
        for(long a[]:ar)
        {
            for(long aa:a)
            {
                sb.append(aa);
                sb.append(' ');
            }
            sb.append("\n");
        }
        p(sb);
    }
    static void p(String ar[])
    {
        int c=0;
        for(String s:ar)c+=s.length()+1;
        StringBuilder sb=new StringBuilder(c);
        for(String a:ar)
        {
            sb.append(a);
            sb.append(' ');
        }
        System.out.println(sb);
    }
    static void p(double ar[])
    {
        StringBuilder sb=new StringBuilder(2*ar.length);
        for(double a:ar)
        {
            sb.append(a);
            sb.append(' ');
        }
        System.out.println(sb);
    }
    static void p(double ar[][])
    {
        StringBuilder sb=new StringBuilder(2*ar.length*ar[0].length);
        for(double a[]:ar)
        {
            for(double aa:a)
            {
                sb.append(aa);
                sb.append(' ');
            }
            sb.append("\n");
        }
        p(sb);
    }
    static void p(char ar[])
    {
        StringBuilder sb=new StringBuilder(2*ar.length);
        for(char aa:ar)
        {
            sb.append(aa);
            sb.append(' ');
        }
        System.out.println(sb);
    }
    static void p(char ar[][])
    {
        StringBuilder sb=new StringBuilder(2*ar.length*ar[0].length);
        for(char a[]:ar)
        {
            for(char aa:a)
            {
                sb.append(aa);
                sb.append(' ');
            }
            sb.append("\n");
        }
        p(sb);
    }
}