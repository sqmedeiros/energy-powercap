import os,sys
from io import BytesIO, IOBase
from collections import deque

BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0) 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
if(os.path.exists('input.txt')):
    sys.stdin = open('input.txt','r') ; sys.stdout = open('output.txt','w')
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    input = lambda: sys.stdin.readline().rstrip("\r\n")

def bfs(source):
    q = deque()
    q.append(source)
    visited[source] = 1
    while q:
        node = q.popleft()
        for i in adjList[node]:
            if visited[i] and team[i]==team[node]:
                return False
            elif not visited[i]:
                team[i] = 1 - team[node]
                visited[i] = 1
                q.append(i)
    return True

n,m = map(int, input().split())
adjList = {i:[] for i in range(n)}
for j in range(m):
    a,b = map(int, input().split())
    a-=1;b-=1
    adjList[a].append(b)
    adjList[b].append(a)
visited = [0]*n
team = [None]*n
possible = True
team[0] = 0
x = bfs(0)
if not x:
    possible = False
else:
    for i in range(1,n):
        if not visited[i]:
            team[i] = 0
            x = bfs(i)
            if not x:
                possible = False
                break

if possible:
    for i in team:
        print(i+1, end=' ')
    print()
else:
    print("IMPOSSIBLE")



