n = int(input())
leng = [int(x) for x in input().split()]
cost = [int(y) for y in input().split()]
ans = 0
cs = cost[0]
for i in range(n-1):
    if cost[i] < cs:
        cs = cost[i]
    ans += cs*leng[i]
print(ans)
