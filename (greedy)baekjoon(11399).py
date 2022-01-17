n = int(input())
p = list(map(int,input().split()))

p.sort()
time = 0
answer = 0
for t in p:
    time+=t
    answer+=time
print(answer)
