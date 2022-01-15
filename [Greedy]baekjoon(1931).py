n = int(input())

lis = [list(map(int,input().split())) for _ in range(n)]
lis.sort(key=lambda x:(x[1],x[0]))

s = lis[0][0]
f = lis[0][1]

cnt = 1
for i in range(1,n):
    if lis[i][0] >= f:
        cnt+=1
        f=lis[i][1]
print(cnt)
