n = int(input())
A = list(map(int,input().split()))
dp_left = [0]*n
dp_right = [0]*n
dp_sum = [0]*n
for i in range(n):
    for j in range(i):
        if A[j]<A[i]:
            dp_left[i] = max(dp_left[i],dp_left[j]+1)
for i in range(n-1,-1,-1):
    for k in range(n-1,i,-1):
        if A[k]<A[i]:
            dp_right[i] = max(dp_right[i],dp_right[k]+1)
for l in range(n):
    dp_sum[l] = dp_left[l]+dp_right[l]+1
print(max(dp_sum))
