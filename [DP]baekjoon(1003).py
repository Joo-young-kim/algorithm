t = int(input())
n_list = []

for i in range(t):
    n_list.append(int(input()))
    
max_n = max(n_list)
dp_zero = [0] * (max_n+1)
dp_one = [0] * (max_n+1)
dp_zero[0] = 1
dp_one[1] = 1

for d in range(2,max_n+1):
    dp_zero[d] = dp_zero[d-1]+dp_zero[d-2]
    dp_one[d] = dp_one[d-1]+dp_one[d-2]
for j in n_list:
    print(f'{dp_zero[j]} {dp_one[j]}')

