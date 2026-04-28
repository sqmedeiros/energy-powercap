#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:39:50 2021
 @author: ericwang
"""

N = int(input())
A = list(map(int, input().split()))

prefix = [0]*(N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + A[i]

minimum_left_prefix = float('inf')
maximum_diff_prefix = -float('inf')
for j in range(1,N+1):
    minimum_left_prefix = min(minimum_left_prefix, prefix[j-1])
    maximum_diff_prefix = max(maximum_diff_prefix, prefix[j]-minimum_left_prefix)

print(maximum_diff_prefix)