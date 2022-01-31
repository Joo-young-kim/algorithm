n = int(input())
grid=[list(map(int,input().split())) for _ in range(n)]

def find_num_of_coins(rows,cols):
    num = 0
    for i in range(rows,rows+3):
        for j in range(cols,cols+3):
            num+=grid[i][j]
    return num

max_num = 0
for i in range(n):
    for j in range(n):
        if i+3>n or j+3>n:
            continue
        max_num = max(max_num,find_num_of_coins(i,j))
print(max_num)
