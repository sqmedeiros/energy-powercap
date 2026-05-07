import java.io.*;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
 
public class entry_6857493 {
	
	final static int MOD = 1000000007;
	final static long INF = 1000000000000000000L;
	
	int ds;
	long[] sum, maxPref, maxSuff, bestSum;
	
	
	void merge(int iL, int iR, int iOut)
	{
		sum[iOut] = sum[iL] + sum[iR];
		maxPref[iOut] = Math.max(maxPref[iL], sum[iL] + maxPref[iR]);
		maxSuff[iOut] = Math.max(maxSuff[iL] + sum[iR], maxSuff[iR]);
		bestSum[iOut] = Math.max(Math.max(bestSum[iL], bestSum[iR]), maxSuff[iL] + maxPref[iR]);
	}
	
	void setValue(int x, long v)
	{
		x += ds;
		sum[x] = maxPref[x] = maxSuff[x] = v;
		bestSum[x] = Math.max(0, v);
		while((x/=2)>0)
			merge(2*x, 2*x+1, x);
	}
	
	void solve()
	{
		int n, q;
		n = in.nextInt();
		q = in.nextInt();
		
		ds = 1;
		while(ds<n)
			ds*=2;
		
		int[] p = in.nextInts(n);
		
		sum = new long[2*ds];
		maxPref = new long[2*ds];
		maxSuff = new long[2*ds];
		bestSum = new long[2*ds];
		
		for(int i=0;i<n;i++)
		{
			setValue( i, p[i]);
		}
		
		while(q-->0)
		{
			int k = in.nextInt()-1;
			int u = in.nextInt();
			setValue(k, u);
			out.println(bestSum[1]);
		}
	}
 
	static Random rand = new Random();	
	public static void safeSort(int[] arr)
	{
		int n = arr.length;
		while(n>1)
		{
			int pos = rand.nextInt(n);
			int tmp = arr[pos];
			arr[pos] = arr[n-1];
			arr[n-1] = tmp;
			n--;
		}
		Arrays.sort(arr);
	}
	
	public static void safeSort(long[] arr)
	{
		int n = arr.length;
		while(n>1)
		{
			int pos = rand.nextInt(n);
			long tmp = arr[pos];
			arr[pos] = arr[n-1];
			arr[n-1] = tmp;
			n--;
		}
		Arrays.sort(arr);
	}
 
	private QuickReader in;
	private PrintWriter out;
 
	
	public entry_6857493(QuickReader in, PrintWriter out) {
		this.in = in;
		this.out = out;
	}
	
	public static void main(String[] args) throws IOException {
		QuickReader in = new QuickReader(System.in);
 
		try(PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));)
		{
			new entry_6857493(in, out).solve();
		}
	}
	
}
 
class QuickReader {
	BufferedReader in;
	StringTokenizer token;
 
	public QuickReader(InputStream ins) {
		in = new BufferedReader(new InputStreamReader(ins));
		token = new StringTokenizer("");
	}
 
	public boolean hasNext() {
		while (!token.hasMoreTokens()) {
			try {
				String s = in.readLine();
				if (s == null)
					return false;
				token = new StringTokenizer(s);
			} catch (IOException e) {
				throw new InputMismatchException();
			}
		}
		return true;
	}
 
	public String next() {
		hasNext();
		return token.nextToken();
	}
 
	public int nextInt() {
		return Integer.parseInt(next());
	}
 
	public int[] nextInts(int n) {
		int[] res = new int[n];
		for (int i = 0; i < n; i++)
			res[i] = nextInt();
		return res;
	}
 
	public long nextLong() {
		return Long.parseLong(next());
	}
 
	public long[] nextLongs(int n) {
		long[] res = new long[n];
		for (int i = 0; i < n; i++)
			res[i] = nextLong();
		return res;
	}
 
}
 
class SuperQuickReader
{
	final int BUFFER_SIZE = 4096;
	Reader in;
	
	char[] buf = new char[BUFFER_SIZE];
	int bufL, bufR;
	
	public SuperQuickReader(InputStream ins)
	{
		in=new InputStreamReader(ins);
	}
 
	public char nextChar()
	{
		try {
			while(bufR >= 0)
			{
				if(bufL < bufR)
				{
					char x = buf[bufL++];
					return x;
				}
				else
				{
					bufR = in.read(buf);
					bufL = 0;
				}
			}
		}
		catch(IOException e)
		{
			bufL = bufR = -1;
		}
		return 0;
	}
	
	public char nextNonSpaceChar()
	{
		char c;
		do
		{
			c = nextChar();
		}while(c == ' ' || c == '\n');
		return c;
	}
	
	public int nextInt()
	{
		int res = 0;
		char c;
		boolean neg = false;
		do
		{
			c = nextChar();
		}
		while(c==' ' || c=='\n');
		if(c == '-')
		{
			neg = true;
			c = nextChar();
		}
		
		do
		{
			res = res * 10 + (c-'0');
			c = nextChar();
		}
		while(c!=' ' && c!='\n' && c!=0);
		if(neg) res = -res;
		return res;
	}
 
	public int[] nextInts(int n)
	{
		int[] res = new int[n];
		for (int i = 0; i < n; i++)
			res[i] = nextInt();
		return res;
	}
 
}