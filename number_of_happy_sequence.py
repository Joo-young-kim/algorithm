n,m = tuple(map(int,input().split()))
grid = [list(map(int,input().split())) for _ in range(n)]
ans = 0
seq = [0]*n
def find_continuous():
    consequtive_count,max_cnt = 1,1
    for i in range(1,n):
        if seq[i-1]==seq[i]:
            consequtive_count+=1
        else:
            consequtive_count=1
        max_cnt = max(max_cnt,consequtive_count)
    if max_cnt>=m:
        return True
    else:
        return False
    
for i in range(n):
    seq = grid[i][:]
    if find_continuous():
        ans += 1

for j in range(n):
    for i in range(n):
        seq[i] = grid[i][j]
    if find_continuous():
        ans += 1
print(ans)
