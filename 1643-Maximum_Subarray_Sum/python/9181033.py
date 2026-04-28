# ctrl + t: toggle side bar
# alt + c: switch to c++ build
# alt + p: switch to python build
# for index, value in enumerate(list)
# type 'setupWithFile' and press Tab: ready to code?

import sys
import io,os


def readFile(name):
    sys.stdin = open(name+".INP", "r")
    sys.stdout = open(name+".OUT", "w")

def fastInput():
    input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

# readFile("TASK")

n = int(input())
arr = list(map(int, input().split()))
prefixS = [0] * (n+1)
prefixmin = [float('inf')] * (n+1)
ans=-float('inf')
for i in range(n):
    prefixS[i+1] = prefixS[i] + arr[i]
    prefixmin[i+1] = min(prefixmin[i], prefixS[i])
for r in range(n):
    ans = max(ans, prefixS[r+1] - prefixmin[r+1])
print(ans)