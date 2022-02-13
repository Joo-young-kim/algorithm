n,m,t = tuple(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(n)]
pos = [tuple(map(int,input().split())) for _ in range(m)]

def In_Range(x,y):
    return x>=0 and x<n and y>=0 and y<n

dxs,dys = [-1,1,0,0],[0,0,-1,1]
count = [[0]*n for _ in range(n)]
new_count = [[0]*n for _ in range(n)]
for x,y in pos:
    count[x-1][y-1] = 1
    
for _ in range(t):
    for i in range(n):
        for j in range(n):
            new_count[i][j] = 0

    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                max_num = 0
                for dx,dy in zip(dxs,dys):
                    nx,ny = i+dx,j+dy
                    if In_Range(nx,ny) and max_num < arr[nx][ny]:
                        max_num = arr[nx][ny]
                        max_pos = (nx,ny)    
                max_x,max_y = max_pos         
                new_count[max_x][max_y] += 1
    
    for i in range(n):
        for j in range(n):
            count[i][j] = new_count[i][j]
            if count[i][j] >= 2:
                count[i][j] = 0
ans = 0
for i in range(n):
    for j in range(n):
        if count[i][j] == 1:
            ans+=1
print(ans)
