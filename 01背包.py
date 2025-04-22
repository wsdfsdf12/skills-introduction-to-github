N,M=map(int,input().split())
dp=[0]*(M+1)
for i in range(0,N):
    v,w=map(int,input().split())
    for j in reversed(range(v,M+1)):
        dp[j]=max(dp[j],dp[j-v]+w)
print(dp[-1])


