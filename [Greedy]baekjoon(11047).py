N,K = map(int,input().split())

money_list = []
for i in range(N):
    money_list.append(int(input()))

count = 0
for n in range(N-1,-1,-1):
    if money_list[n] <= K:
        count += K//money_list[n]
        K %= money_list[n]
    if K == 0:
        break
print(count)
