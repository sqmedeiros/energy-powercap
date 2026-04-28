from bisect import bisect_right
# SEE MODIFICATIONS WHICH HELP SPEED UP CODE
# ALSO SEE BASIC DP TEMPLATE
def main():
    n,x = map(int,(input().split())) 
    a = sorted(list(map(int, input().split())))
    mod = pow(10,9)+7
    ans=[1 for i in range(x+1)]
    for i in range(1,x+1):
        _=0
        for j in range(bisect_right(a,i)):
            _+=ans[i-a[j]]
        ans[i]= divmod(_,mod)[1]
    print(ans[-1])

if __name__ == '__main__':
    main()
