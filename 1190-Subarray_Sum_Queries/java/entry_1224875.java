import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;
import java.util.function.Supplier;
import java.io.UncheckedIOException;
import java.util.function.Consumer;
import java.io.Closeable;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;
import java.util.function.IntFunction;
 
/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class entry_1224875 {
    public static void main(String[] args) throws Exception {
        Thread thread = new Thread(null, new TaskAdapter(), "", 1 << 29);
        thread.start();
        thread.join();
    }
 
    static class TaskAdapter implements Runnable {
        @Override
        public void run() {
            InputStream inputStream = System.in;
            OutputStream outputStream = System.out;
            FastInput in = new FastInput(inputStream);
            FastOutput out = new FastOutput(outputStream);
            SubarraySumQueries solver = new SubarraySumQueries();
            solver.solve(1, in, out);
            out.close();
        }
    }
 
    static class SubarraySumQueries {
        public void solve(int testNumber, FastInput in, FastOutput out) {
            int n = in.readInt();
            int m = in.readInt();
            int[] a = new int[n];
            in.populate(a);
            UpdateImpl u = new UpdateImpl();
            SumImpl s = new SumImpl();
            SegTree<SumImpl, UpdateImpl> segTree = new SegTree<>(0, n - 1, SumImpl::new,
                    UpdateImpl::new, i -> {
                SumImpl sum = new SumImpl();
                u.x = a[i];
                sum.update(u);
                return sum;
            });
 
            for (int i = 0; i < m; i++) {
                int k = in.readInt() - 1;
                int x = in.readInt();
                u.x = x;
                segTree.update(k, k, 0, n - 1, u);
                out.println(segTree.sum.max);
            }
        }
 
    }
 
    static interface Update<U extends Update<U>> extends Cloneable {
        void update(U u);
 
        void clear();
 
        boolean ofBoolean();
 
        U clone();
 
    }
 
    static class SumImpl implements Sum<SumImpl, UpdateImpl> {
        long left;
        long right;
        long max;
        long sum;
 
        public void add(SumImpl right) {
            SumImpl left = this;
            long bestLeft = Math.max(left.left, left.sum + right.left);
            long bestRight = Math.max(left.right + right.sum, right.right);
            long bestMax = Math.max(left.max, right.max);
            bestMax = Math.max(bestMax, left.right + right.left);
            long bestSum = left.sum + right.sum;
 
            this.left = bestLeft;
            this.right = bestRight;
            this.max = bestMax;
            this.sum = bestSum;
        }
 
        public void update(UpdateImpl update) {
            sum = update.x;
            max = left = right = Math.max(0, update.x);
        }
 
        public void copy(SumImpl sum) {
            left = sum.left;
            right = sum.right;
            max = sum.max;
            this.sum = sum.sum;
        }
 
        public SumImpl clone() {
            SumImpl ans = new SumImpl();
            ans.copy(this);
            return ans;
        }
 
        public String toString() {
            return "" + sum;
        }
 
    }
 
    static class DigitUtils {
        private DigitUtils() {
        }
 
        public static int floorAverage(int x, int y) {
            return (x & y) + ((x ^ y) >> 1);
        }
 
    }
 
    static class UpdateImpl implements Update<UpdateImpl> {
        int x;
 
        public void update(UpdateImpl update) {
        }
 
        public void clear() {
            x = Integer.MIN_VALUE;
        }
 
        public boolean ofBoolean() {
            return x != Integer.MIN_VALUE;
        }
 
        public UpdateImpl clone() {
            UpdateImpl ans = new UpdateImpl();
            ans.x = x;
            return ans;
        }
 
    }
 
    static class FastInput {
        private final InputStream is;
        private byte[] buf = new byte[1 << 13];
        private int bufLen;
        private int bufOffset;
        private int next;
 
        public FastInput(InputStream is) {
            this.is = is;
        }
 
        public void populate(int[] data) {
            for (int i = 0; i < data.length; i++) {
                data[i] = readInt();
            }
        }
 
        private int read() {
            while (bufLen == bufOffset) {
                bufOffset = 0;
                try {
                    bufLen = is.read(buf);
                } catch (IOException e) {
                    bufLen = -1;
                }
                if (bufLen == -1) {
                    return -1;
                }
            }
            return buf[bufOffset++];
        }
 
        public void skipBlank() {
            while (next >= 0 && next <= 32) {
                next = read();
            }
        }
 
        public int readInt() {
            int sign = 1;
 
            skipBlank();
            if (next == '+' || next == '-') {
                sign = next == '+' ? 1 : -1;
                next = read();
            }
 
            int val = 0;
            if (sign == 1) {
                while (next >= '0' && next <= '9') {
                    val = val * 10 + next - '0';
                    next = read();
                }
            } else {
                while (next >= '0' && next <= '9') {
                    val = val * 10 - next + '0';
                    next = read();
                }
            }
 
            return val;
        }
 
    }
 
    static class FastOutput implements AutoCloseable, Closeable, Appendable {
        private static final int THRESHOLD = 1 << 13;
        private final Writer os;
        private StringBuilder cache = new StringBuilder(THRESHOLD * 2);
 
        public FastOutput append(CharSequence csq) {
            cache.append(csq);
            return this;
        }
 
        public FastOutput append(CharSequence csq, int start, int end) {
            cache.append(csq, start, end);
            return this;
        }
 
        private void afterWrite() {
            if (cache.length() < THRESHOLD) {
                return;
            }
            flush();
        }
 
        public FastOutput(Writer os) {
            this.os = os;
        }
 
        public FastOutput(OutputStream os) {
            this(new OutputStreamWriter(os));
        }
 
        public FastOutput append(char c) {
            cache.append(c);
            afterWrite();
            return this;
        }
 
        public FastOutput append(long c) {
            cache.append(c);
            afterWrite();
            return this;
        }
 
        public FastOutput append(String c) {
            cache.append(c);
            afterWrite();
            return this;
        }
 
        public FastOutput println(long c) {
            return append(c).println();
        }
 
        public FastOutput println() {
            return append(System.lineSeparator());
        }
 
        public FastOutput flush() {
            try {
                os.append(cache);
                os.flush();
                cache.setLength(0);
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
            return this;
        }
 
        public void close() {
            flush();
            try {
                os.close();
            } catch (IOException e) {
                throw new UncheckedIOException(e);
            }
        }
 
        public String toString() {
            return cache.toString();
        }
 
    }
 
    static class SegTree<S extends Sum<S, U>, U extends Update<U>> implements Cloneable {
        private SegTree<S, U> left;
        private SegTree<S, U> right;
        public S sum;
        private U update;
 
        private void modify(U x) {
            update.update(x);
            sum.update(x);
        }
 
        private void pushDown() {
            if (update.ofBoolean()) {
                left.modify(update);
                right.modify(update);
                update.clear();
                assert !update.ofBoolean();
            }
        }
 
        private void pushUp() {
            sum.copy(left.sum);
            sum.add(right.sum);
        }
 
        public SegTree(int l, int r, Supplier<S> sSupplier, Supplier<U> uSupplier,
                       IntFunction<S> func) {
            update = uSupplier.get();
            update.clear();
            if (l < r) {
                sum = sSupplier.get();
                int m = DigitUtils.floorAverage(l, r);
                left = new SegTree<>(l, m, sSupplier, uSupplier, func);
                right = new SegTree<>(m + 1, r, sSupplier, uSupplier, func);
                pushUp();
            } else {
                sum = func.apply(l);
            }
        }
 
        private boolean cover(int ll, int rr, int l, int r) {
            return ll <= l && rr >= r;
        }
 
        private boolean leave(int ll, int rr, int l, int r) {
            return rr < l || ll > r;
        }
 
        public void update(int ll, int rr, int l, int r, U u) {
            if (leave(ll, rr, l, r)) {
                return;
            }
            if (cover(ll, rr, l, r)) {
                modify(u);
                return;
            }
            int m = DigitUtils.floorAverage(l, r);
            pushDown();
            left.update(ll, rr, l, m, u);
            right.update(ll, rr, m + 1, r, u);
            pushUp();
        }
 
        public SegTree<S, U> deepClone() {
            SegTree<S, U> clone = clone();
            clone.sum = clone.sum.clone();
            clone.update = clone.update.clone();
            if (clone.left != null) {
                clone.left = clone.left.deepClone();
                clone.right = clone.right.deepClone();
            }
            return clone;
        }
 
        public void visitLeave(Consumer<SegTree<S, U>> consumer) {
            if (left == null) {
                consumer.accept(this);
                return;
            }
            pushDown();
            left.visitLeave(consumer);
            right.visitLeave(consumer);
        }
 
        public String toString() {
            StringBuilder ans = new StringBuilder();
            deepClone().visitLeave(x -> ans.append(x.sum).append(' '));
            return ans.toString();
        }
 
        public SegTree<S, U> clone() {
            try {
                return (SegTree<S, U>) super.clone();
            } catch (CloneNotSupportedException e) {
                throw new UnsupportedOperationException(e);
            }
        }
 
    }
 
    static interface Sum<S, U> extends Cloneable {
        void add(S s);
 
        void update(U u);
 
        void copy(S s);
 
        S clone();
 
    }
}
