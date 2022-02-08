commands = input()
x,y = 0,0
dxs = [1,0,-1,0]
dys = [0,-1,0,1]
dis_num = 3
time = 0
flag = False
for command in commands:
    if command == 'F':
        x,y = x+dxs[dis_num],y+dys[dis_num]
    elif command == 'L':
        dis_num = (dis_num-1+4)%4
    else:
        dis_num = (dis_num+1)%4
    time += 1
    if x == 0 and y == 0:
        flag = True
        print(time)
        break
if flag == False:
    print(-1)
