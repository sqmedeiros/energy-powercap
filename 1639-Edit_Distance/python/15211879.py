a = input().strip()
b = input().strip()

m = len(b)
#instead of O(n^2), we use O(n)
prev = list(range(m+1)) #prev row of dp which includes base case
cur = [0] * (m+1) #curr row of dp; idx = length of prefix of b[0:i], val = count/cost
n = len(a)

for i in range(1,n+1):
    #changing first i character to an empty str(0) requires i character 
    cur[0] = i

    for j in range(1, m + 1):
        #check all 3 possible operations and find min one
        #if char match no change is needed, else cost of 1
        cost = 0 if a[i-1] == b[j - 1] else 1
        cur[j] = min(
            prev[j] + 1,        
            cur[j - 1] + 1,     
            prev[j - 1] + cost  
        )
    prev, cur = cur, prev

print(prev[m])