import sys

def main():
    input = sys.stdin.read
    data = input().split()
    n=int(data[0])
    x=int(data[1])
    arr = []
    for i in range(2,len(data)):
        arr.append((int(data[i]),i-1))
    arr.sort(key=lambda x : x[0])
    i,j = 0,len(arr)-1
    while i<j:
        # print(arr[i][0],arr[i][1],arr[j][0],arr[j][1])
        if arr[i][0] + arr[j][0] < x:
            i = i+1
        elif arr[i][0] + arr[j][0] > x:
            j = j-1
        else:
            print(arr[i][1],arr[j][1])
            return
    print("IMPOSSIBLE")


if __name__ == "__main__":
    main()