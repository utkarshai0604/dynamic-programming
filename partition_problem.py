def part(l,n, s1):
    dp=[[True for i in range(n+1)] for j in  range(s1+1)]
    for i in range(n+1):
        dp[0][i]=True
    for i in range(1,s1+1):
        dp[i][0]=False
    for i in range(1,s1+1):
        for j in range(1,n+1):
            dp[i][j]=dp[i][j-1]
            if(i>=l[j-1]):
                dp[i][j]=dp[i-l[j-1]][j-1] or dp[i][j-1]
    return dp[s1][n]



for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    s=sum(l)
    if(s%2!=0):
        print("NO")
    else:
        s1=s//2
        if (part(l,n, s1)):
            print("YES")
        else:
            print("NO")
