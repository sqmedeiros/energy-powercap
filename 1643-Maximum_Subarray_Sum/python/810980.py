#inputs
def ii():return int(input())
def li():return list(map(int,input().split()))
def mi():return map(int,input().split())

def main():
    n=ii()
    ar=li()
    temp=ar[0]
    sums=temp
    for i in range(1,n):
        temp=max(ar[i],temp+ar[i])
        sums=max(temp,sums)
    print(sums)









if __name__ == "__main__":
    main()

