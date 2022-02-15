n = int(input())
original_grid = [list(map(int,input().split())) for _ in range(n)]
grid = [[0]*n for _ in range(n)]
dxs,dys = [0,1,0,-1],[1,0,-1,0]
def In_Range(x,y):
    return x>=0 and x<n and y>=0 and y<n

max_num = 0
for i in range(n):
    for j in range(n):
        for ni in range(n):
            for nj in range(n):
                grid[ni][nj] = original_grid[ni][nj]
        bomb_range = grid[i][j]
        for k in range(n):
            for l in range(n):
                if (k==i or l==j) and abs(k-i)+abs(l-j) < bomb_range:
                    grid[k][l] = 0
        new_grid = [[0]*n for _ in range(n)]
        for col in range(n):
            new_row = n-1
            for row in range(n-1,-1,-1):
                if grid[row][col]:
                    new_grid[new_row][col] = grid[row][col]
                    new_row -= 1
        cnt = 0
        check = [[0]*n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                for dx,dy in zip(dxs,dys):
                    nx,ny = x+dx,y+dy
                    if new_grid[x][y] and In_Range(nx,ny) and check[nx][ny]==0 and new_grid[x][y] == new_grid[nx][ny]:
                        cnt+=1
                        check[x][y] += 1
        max_num = max(max_num,cnt)
print(max_num)
