
def main():

    dic = {}
    n,target = map(int,input().split())
    arr = list(map(int,input().split()))


    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] not in dic:  dic[arr[i]+arr[j]] = set()
            dic[arr[i]+arr[j]].add((i+1,j+1))

    for i in range(n):
        for j in range(i+1,n):
            dic[arr[i]+arr[j]].remove((i+1,j+1))
            if not dic[arr[i]+arr[j]]:   del dic[arr[i]+arr[j]]


        for j in range(i):
            curr = arr[j] + arr[i]
            if target - curr in dic: 
                for ele in dic[target-curr]:
                    print(j+1,i+1,ele[0],ele[1]) 
                    return 

    print("IMPOSSIBLE")          











main()