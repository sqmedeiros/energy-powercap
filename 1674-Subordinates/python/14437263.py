#!/usr/bin/env python3

"""
Author: sahil
Date: 80/08/69
Description: sex
"""

def main():
    n=int(input())
    l=list(map(int,input().split()))
    fx=[[] for _ in range(n+1)]
    for i,j in enumerate(l,start=2):
        fx[j].append(i)
    stk=[1]
    vis=set()
    subcnt=[0]*(n+1)
    while stk:
        x=stk.pop()
        if x in vis:
            lm=sum(1+subcnt[m] for m in fx[x])
            subcnt[x]=lm
        else:
            stk.append(x)
            vis.add(x)
            for i in fx[x]:
                stk.append(i)
    print(*subcnt[1:])


if __name__ == "__main__":
    main()