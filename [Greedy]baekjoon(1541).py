minus = input().split('-')
num = []
for m in minus:
    cnt = 0
    s = m.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1,len(num)):
    n -= num[i]
print(n)
