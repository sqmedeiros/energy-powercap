import io, os, sys

def inp():
    return (int(input()))
def inlt():
    return (list(map(int,input().split())))
def insr():
    return (input().strip())
def invr():
    return (map(int,input().split()))

def print_str(s):
    return sys.stdout.write(s+"\n")
def print_int(n):
    return sys.stdout.write(str(n)+"\n")
def print_list(l):
    return sys.stdout.write(" ".join(map(str,list)) + "\n")

n = inp()
l=inlt()
m=float('-inf')
s=0
flag=1
k=max(l)
if k<0:
    flag=0
    print(k)
if flag:
    for i in range(n):
        s+=l[i]
        if (s<0):
            s=0
        if s>m:
            m=s
    print(m)