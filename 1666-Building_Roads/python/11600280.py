from typing import List, Dict
from collections import deque

def bfs(adj_list: Dict[int, List[int]], init_city: int, parent_city: List[int]):

    parent_city[init_city]= init_city

    q= deque([init_city])

    while q:
        city= q.popleft()
        if city in adj_list.keys():
            for temp_city in adj_list[city]:
                if parent_city[temp_city]==-1:
                    parent_city[temp_city]=init_city
                    q.append(temp_city)

    return



def solve():
    n, m= map(int , input().strip().split())

    adj_list= {}

    for _ in range(m):
        city_a, city_b= map(int, input().strip().split())
        if city_a not in adj_list.keys():
            adj_list[city_a]= []
        if city_b not in adj_list.keys():
            adj_list[city_b]= []
        adj_list[city_a].append(city_b)
        adj_list[city_b].append(city_a)

    parent_city= [-1]*(n+1)

    for i in range(1,n+1):
        if parent_city[i]==-1:
            bfs(adj_list, i, parent_city)

    temp=[]

    for i, val in enumerate(parent_city):

        if i==val:
            temp.append(val)


    print(len(temp)-1)

    for i in range(1, len(temp)):
        print(f'{temp[0]} {temp[i]}\n')

solve()







