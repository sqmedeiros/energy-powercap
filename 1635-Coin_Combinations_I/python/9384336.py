# -*- coding: utf-8 -*-
# @Author: daghn
# @Date:   2024-05-27 01:15:31
# @Last Modified by:   daghn
# @Last Modified time: 2024-05-28 23:32:57

# file = open("C:\\Users\\daghn\\Desktop\\python_work\\test_input.txt")
# input = file.readline 

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
coins = list(map(int, input().split()))

possible_ways = [0 for _ in range(x+1)]
possible_ways[0] = 1

for i in range(1, x+1):
 for c in coins:
  if i - c >=0:
   possible_ways[i] += possible_ways[i-c]

 possible_ways[i] = possible_ways[i] % 1000000007

print(possible_ways[x]) 
