n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort() # ab.sort(key = lambda x:x[0]) 가 기본
dp = [1]*n
for i in range(n):
    for j in range(i):
        if ab[j][1]<ab[i][1]:
            dp[i] = max(dp[i],dp[j]+1)
print(n-max(dp))
