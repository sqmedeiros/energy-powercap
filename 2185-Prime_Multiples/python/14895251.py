from itertools import combinations as c
from math import prod as p

l = int(input().split(' ')[0])
r = [int(i) for i in input().split(' ')]
t = 0
for i in range(1, len(r)+1):
    for d in c(r, i):t+=l//p(d) * (-1)**(i+1)
print(t)