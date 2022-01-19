num = int(input())
stair_list = [0]+[int(input()) for _ in range(num)]+[0]
dp = [0]*(num+2)
dp[1] = stair_list[1]
dp[2] = stair_list[1]+stair_list[2]
for i in range(3,num+1):
    dp[i] = max(dp[i-3]+stair_list[i-1],dp[i-2])+stair_list[i]
print(dp[num])
