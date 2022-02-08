n = int(input())
dists = [tuple(input().split()) for _ in range(n)]

x,y =0,0
dxs = [1,0,-1,0]
dys = [0,-1,0,1]
mapper = {'E':0,'S':1,'W':2,'N':3}

time = 0
flag = False
for direc,dist in dists:
    for _ in range(int(dist)):
        dis_num = mapper[direc]
        x,y = x+dxs[dis_num],y+dys[dis_num]
        time+=1
        if x==0 and y == 0:
            flag = True
            break
    if flag:
        print(time)
        break
if not flag:
    print(-1)
