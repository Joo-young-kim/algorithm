T = int(input())

t_list = [int(input()) for _ in range(T)]

dp = [0]*101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for n in t_list:
    for j in range(4,n+1):
        dp[j] = dp[j-3]+dp[j-2]
    print(dp[n])
