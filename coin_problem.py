def coin(l,s1,n):
    dp=[[0 for i in range(n)] for j in range(s1+1) ]

    for i in range(n):
        dp[0][i]=1
    
    for i in range(1,s1+1):
        for j in range(n):
            x=dp[i][j-1] if j>0 else 0
            y=dp[i-l[j]][j] if (i-l[j])>=0 else  0
            dp[i][j]=x+y
    return dp[s1][n-1]
for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    s1=int(input())
    print(coin(l,s1,n))


# another solution
# for _ in range(int(input())):
#     n,ar,m=int(input()),list(map(int,input().split())),int(input())
#     dp=[0]*(m+1)
#     dp[0]=1
#     for i in range(n):
#         for j in range(ar[i],m+1):
#             dp[j]+=dp[j-ar[i]]
#     print(dp[m]) 