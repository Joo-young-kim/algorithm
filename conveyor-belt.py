n,t = tuple(map(int,input().split()))
ups = list(map(int,input().split()))
downs =list(map(int,input().split()))[::-1]
for _ in range(t):
    temp = ups[n-1]
    for i in range(n-1,0,-1):
        ups[i] = ups[i-1]
    ups[0] = downs[0]
    for j in range(n-1):
        downs[j] = downs[j+1]
    downs[n-1] = temp
for elem in ups:
    print(elem,end=' ')
print()
for i in range(n-1,-1,-1):
    print(downs[i],end=' ')
