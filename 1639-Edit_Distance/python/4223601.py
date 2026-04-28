def editDistance(s, t) :
    dp=[0 for i in range(len(t)+1)]
    n = len(s)
    m= len(t)
    for i in range(m+1):
        dp[i]=i
    for i in range(1,n+1):
        temp =[0 for i in range(m+1)]
        temp[0]=i
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                temp[j]=dp[j-1]
            else:
                temp[j]=1+min(dp[j-1], min(dp[j], temp[j-1]))
        dp=temp
    return dp[m]


s1 = input()
s2 = input()
print(editDistance(s1,s2))