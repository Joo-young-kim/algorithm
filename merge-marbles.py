EMPTY = (0,0,0)
n, m, t = tuple(map(int, input().split()))
grid = [[EMPTY]*n for _ in range(n)]
next_grid = [[EMPTY]*n for _ in range(n)]

def In_Range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n
def next_pos(x,y,move_dir):
    dxs,dys = [-1,0,0,1],[0,1,-1,0]
    nx,ny = x+dxs[move_dir],y+dys[move_dir]
    if not In_Range(nx,ny):
        move_dir = 3-move_dir
    else:
        x,y = nx,ny
    return (x,y,move_dir)
def update(x,y,new_marble):
    num,weight,move_dir = next_grid[x][y]
    new_num,new_weight,new_dir = new_marble
    if new_num>num:
        next_grid[x][y]=(new_num,weight+new_weight,new_dir)
    else:
        next_grid[x][y] = (num,weight+new_weight,move_dir)
def move(x,y):
    num,weight,move_dir = grid[x][y]
    nx,ny,next_dir = next_pos(x,y,move_dir)
    update(nx,ny,(num,weight,next_dir))
def simulate():
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = EMPTY
    for i in range(n):
        for j in range(n):
            if grid[i][j] != EMPTY:
                move(i,j)
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
def get_marble_num():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != EMPTY:
                cnt += 1
    return cnt
def get_max_weight():
    max_weight = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] != EMPTY:
                max_weight = max(max_weight,grid[i][j][1])
    return max_weight
dir_mapper = {'U':0,'D':3,'R':1,'L':2}

for i in range(m):
    r,c,d,w = tuple(input().split())
    r,c,w = tuple(map(int,[r,c,w]))
    grid[r-1][c-1] = (i+1,w,dir_mapper[d])
for _ in range(t):
    simulate()
marble_num,max_weight = get_marble_num(),get_max_weight()
print(marble_num,max_weight)
