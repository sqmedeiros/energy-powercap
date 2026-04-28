import math

def dfs(pos,s,prod,coef):
  if pos==len(A):return s//prod*coef
  if prod>s: return 0
  return dfs(pos+1,s,prod,coef)+dfs(pos+1,s,math.lcm(prod,A[pos]),-coef)

N,K=map(int,input().split())
A=list(map(int,input().split()))
print(N-dfs(0,N,1,1))