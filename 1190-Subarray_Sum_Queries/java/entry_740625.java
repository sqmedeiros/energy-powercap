import java.io.*;
import java.math.*;
import java.util.*;
import java.lang.*;
 
// import java.text.DecimalFormat; 
// import java.text.DecimalFormatSymbols; 
 
 
// Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
 
public class entry_740625 {
    
    static class Reader 
    { 
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
            din = new DataInputStream(new FileInputStream(file_name)); 
            buffer = new byte[BUFFER_SIZE]; 
            bufferPointer = bytesRead = 0; 
        } 
  
        public String readLine() throws IOException 
        { 
            byte[] buf = new byte[64]; // line length 
            int cnt = 0, c; 
            while ((c = read()) != -1) 
            { 
                if (c == '\n') 
                    break; 
                buf[cnt++] = (byte) c; 
            } 
            return new String(buf, 0, cnt); 
        } 
  
        public int nextInt() throws IOException 
        { 
            int ret = 0; 
            byte c = read(); 
            while (c <= ' ') 
                c = read(); 
            boolean neg = (c == '-'); 
            if (neg) 
                c = read(); 
            do
            { 
                ret = ret * 10 + c - '0'; 
            }  while ((c = read()) >= '0' && c <= '9'); 
  
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
            } 
            while ((c = read()) >= '0' && c <= '9'); 
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
            } 
            while ((c = read()) >= '0' && c <= '9'); 
  
            if (c == '.') 
            { 
                while ((c = read()) >= '0' && c <= '9') 
                { 
                    ret += (c - '0') / (div *= 10); 
                } 
            } 
  
            if (neg) 
                return -ret; 
            return ret; 
        } 
  
        private void fillBuffer() throws IOException 
        { 
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE); 
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
  
  
    //Range Minimum
    public static int size;
    public static long[][] sar;
    
    public static void main(String args[] ) throws Exception {
        StringBuffer str = new StringBuffer();
        PrintWriter pw=new PrintWriter(System.out);
        Reader sc = new Reader();
        
        int n = sc.nextInt();
        int m =sc.nextInt();
        init(n);
        int[] ar = new int[n];
        for(int i=0;i<n;i++){
            ar[i] = sc.nextInt();
        }
        build(ar,n);
        long ans = maxseg();
        // if(ans<0L)
        //     str.append("0\n");
        // else 
        //     str.append(ans+"\n");
        while(m-->0){
            
            int a,b;
 
            a = sc.nextInt();
            a--;
            b = sc.nextInt();
            set(a,b);
            
            ans = maxseg();
            if(ans<0L)
                str.append("0\n");
            else 
                str.append(ans+"\n");
            
        }
        
        
       
        pw.println(str.toString());
        
        pw.close();
    }
    
    
    public static void build(int[] ar,int n){
        build(ar,n,0,0,size);
    }
    public static void build(int[] ar,int n,int x,int lx,int rx){
        if(rx-lx==1){
            if(lx<n){
                sar[x][0] = ar[lx];
                sar[x][1] = ar[lx];
                sar[x][2] = ar[lx];
                sar[x][3] = ar[lx];
            }
            return;
        }
        int m = lx+(rx-lx)/2;
        build(ar,n,2*x+1,lx,m);
        build(ar,n,2*x+2,m,rx);
        
        sar[x][3] = sar[2*x+1][3]+sar[2*x+2][3];
        
        sar[x][1] = (sar[2*x+1][1]<sar[2*x+1][3]+sar[2*x+2][1])?sar[2*x+1][3]+sar[2*x+2][1]:sar[2*x+1][1];
        
        sar[x][2] = (sar[2*x+2][2]<sar[2*x+2][3]+sar[2*x+1][2])?sar[2*x+2][3]+sar[2*x+1][2]:sar[2*x+2][2];
        
        long te = (sar[2*x+1][0]>sar[2*x+2][0])?sar[2*x+1][0]:sar[2*x+2][0];
        
        sar[x][0] = (te>sar[2*x+1][2]+sar[2*x+2][1])?te:sar[2*x+1][2]+sar[2*x+2][1];
        
    }
    public static long maxseg(){
        return sar[0][0];
    }
 
    public static void set(int i,int v){
        set(i,v,0,0,size);
    }
    public static void set(int i,int v,int x,int lx,int rx){
        if(rx-lx==1){
            sar[x][0]=v;
            sar[x][1]=v;
            sar[x][2]=v;
            sar[x][3]=v;
            return;
        }
        int m = lx+(rx-lx)/2;
        if(i<m)
            set(i,v,2*x+1,lx,m);
        else
            set(i,v,2*x+2,m,rx);
        
        sar[x][3] = sar[2*x+1][3]+sar[2*x+2][3];
        
        sar[x][1] = (sar[2*x+1][1]<sar[2*x+1][3]+sar[2*x+2][1])?sar[2*x+1][3]+sar[2*x+2][1]:sar[2*x+1][1];
        
        sar[x][2] = (sar[2*x+2][2]<sar[2*x+2][3]+sar[2*x+1][2])?sar[2*x+2][3]+sar[2*x+1][2]:sar[2*x+2][2];
        
        long te = (sar[2*x+1][0]>sar[2*x+2][0])?sar[2*x+1][0]:sar[2*x+2][0];
        
        sar[x][0] = (te>sar[2*x+1][2]+sar[2*x+2][1])?te:sar[2*x+1][2]+sar[2*x+2][1];
        
        
    }
    public static void init(int n){
        size = 1;
        while(size<n) size*=2;
        sar = new long[2*size][4];
        for(int i=0;i<2*size;i++){
            sar[i][0] = Integer.MIN_VALUE;
            sar[i][1] = Integer.MIN_VALUE;
            sar[i][2] = Integer.MIN_VALUE;
        }
    }
    
    public static void show(){
        for(int i=0;i<2*size;i++){
            System.out.print(sar[i][0]+" ");
        }
        
    }
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
}