# import sys
# sys.stdin = open("in")
import random

n,x = map(int,input().split())
a_list = list(map(int,input().split()))

seed = random.randrange(2**62)
def hash_mix(x):
    return x^seed

save_list = {}
for i,a in enumerate(a_list):
    if hash_mix(x-a) in save_list:
        print(i+1, save_list[hash_mix(x-a)]+1)
        exit()
    save_list[hash_mix(a)] = i
print("IMPOSSIBLE")