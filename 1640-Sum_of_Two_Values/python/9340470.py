# -*- coding: utf-8 -*-
# @Author: daghn
# @Date:   2024-05-24 00:10:46
# @Last Modified by:   daghn
# @Last Modified time: 2024-05-24 01:53:54
# 
# file = open("C:\\Users\\daghn\\Desktop\\python_work\\test_input11.txt")
# content = file.readlines()
# n, target = map(int, content[0].split())
# values = list(map(int, content[1].split()))

from bisect import *

n, target = map(int, input().split())
values = list(map(int, input().split()))

# We need both the sorted list and the unsorted list so we can 
# look up id in the unsorted list.
values_sorted = sorted(values)

# One number at a time...
for number in values_sorted:

 # Just a little optimization.
 new_target = target - number
 if new_target < number:
  print("IMPOSSIBLE")
  exit()

 #  Binary search to find candidate partner 
 idx = bisect(values_sorted, new_target) - 1
 number_to_try = values_sorted[idx]

 # Did we hit gold?
 if number + number_to_try == target:

  # Index of first number.
  a = values.index(number)

  # Avoid picking the same index.
  if number == number_to_try:
   values[a] += 1

  # Second number not even there if we had to use 
  # the same unique number twice, so we kindly
  # ask before asking for index.
  if number_to_try in values:
   b = values.index(number_to_try)
   print(f"{a+1} {b+1}")
   exit()

print("IMPOSSIBLE")