n,m = tuple(map(int,input().split()))
arr = [[0]*n for _ in range(n)]
dxs = [1,-1,0,0]
dys = [0,0,1,-1]

def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n

for _ in range(m):
    x,y = tuple(map(int,input().split()))
    arr[x-1][y-1] = 1
    cnt = 0
    # for i in range(4):
    #     nx,ny = x-1+dxs[i],y-1+dys[i]
    #     if in_range(nx,ny) and arr[nx][ny] == 1:
    #         cnt += 1
    for dx,dy in zip(dxs,dys):
        nx,ny = x-1+dx,y-1+dy
        if in_range(nx,ny) and arr[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)
