# import sys
# sys.stdin = open('C:\\Users\\Preetish\\Desktop\\Python\\input.txt', 'r') 
# sys.stdout = open('C:\\Users\\Preetish\\Desktop\\Python\\output.txt', 'w')


def func(prod, ind, pm1, arr, n, n1):
    if(ind >= n):
        return ((-1)**pm1)*(n1//prod)
    elif(prod>n1):
        return 0
    elif(ind == -1):
        co = 0;
        for i in range(n):
            co+=func(prod*arr[i], i, pm1, arr, n, n1)
        return co

    else:
        co =((-1)**pm1)*(n1//prod);
        for i in range(ind+1,n):
            co+=func(prod*arr[i], i, pm1+1, arr, n, n1)
        return co



n,k  = input().split()
n = int(n)
k = int(k)
arr = input().split()
arr = [int(i) for i in arr]


print(func(1, -1, 2, arr, k, n))