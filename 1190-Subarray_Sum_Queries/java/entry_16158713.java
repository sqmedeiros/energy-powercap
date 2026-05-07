import java.io.*;
public class entry_16158713{
    static class Node{
        long sum,pref,suff,best;
    }
    static Node[] seg;
    static int size;
 
    static Node merge(Node a,Node b){
        Node c=new Node();
        c.sum=a.sum+b.sum;
        c.pref=Math.max(a.pref,a.sum+b.pref);
        c.suff=Math.max(b.suff,b.sum+a.suff);
        c.best=Math.max(Math.max(a.best,b.best),a.suff+b.pref);
        return c;
    }
    static Node make(long v){
        Node n=new Node();
        n.sum=v;
        n.pref=Math.max(v,0);
        n.suff=Math.max(v,0);
        n.best=Math.max(v,0);
        return n;
    }
    public static void main(String[] args)throws Exception{
        FastScanner fs=new FastScanner(System.in);
        int n=fs.nextInt();
        int m=fs.nextInt();
        size=1;
        while(size<n) size<<=1;
        seg=new Node[2*size];
 
        for(int i=0;i<2*size;i++) seg[i]=make(0);
 
        for(int i=0;i<n;i++){
            seg[size+i]=make(fs.nextLong());
        }
 
        for(int i=size-1;i>0;i--){
            seg[i]=merge(seg[i<<1],seg[i<<1|1]);
        }
 
        StringBuilder sb=new StringBuilder();
        while(m-- >0){
            int pos=fs.nextInt()-1;
            long val=fs.nextLong();
            int i=size+pos;
            seg[i]=make(val);
            for(i>>=1;i>0;i>>=1){
                seg[i]=merge(seg[i<<1],seg[i<<1|1]);
            }
            sb.append(seg[1].best).append('\n');
        }
        System.out.print(sb.toString());
    }
 
    static class FastScanner{
        private final byte[] buffer=new byte[1<<16];
        private int ptr=0,len=0;
        private final InputStream in;
        FastScanner(InputStream in){
            this.in=in;
        }
        private int readByte()throws IOException{
            if(ptr>=len){
                len=in.read(buffer);
                ptr=0;
                if(len<=0) return -1;
            }
            return buffer[ptr++];
        }
        long nextLong()throws IOException{
            int c;
            while((c=readByte())<=32);
            boolean neg=false;
            if(c=='-'){
                neg=true;
                c=readByte();
            }
            long val=0;
            while(c>32){
                val=val*10+(c-'0');
                c=readByte();
            }
            return neg?-val:val;
        }
        int nextInt()throws IOException{
            return (int)nextLong();
        }
    }
}