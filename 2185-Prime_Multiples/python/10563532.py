# -*- coding: utf-8 -*-

import itertools

n,k = map(int,input().split())
prime_arr = list(map(int,input().split()))

place = set()
for i in range(k):
    place.add(i)

ans = 0
flag=-1
for i in range(1,k+1):
    flag*=-1
    for tu in itertools.combinations(place,i):
        val=1
        rv=0
        for r in tu:
            val*=prime_arr[r]
        if n>=val:
            rv=n//val
        ans+=flag*rv

print(ans)