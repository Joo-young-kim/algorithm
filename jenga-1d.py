n = int(input())
arr = [int(input()) for _ in range(n)]
end_of_arr = n

def cut_arr(start_idx,end_idx):
    global end_of_arr,arr
    temp = []
    for i in range(end_of_arr):
        if i<start_idx or i>end_idx:
            temp.append(arr[i])
    end_of_arr = len(temp)
    for i in range(end_of_arr):
        arr[i] = temp[i]

for _ in range(2):
    s, e = tuple(map(int, input().split()))
    cut_arr(s-1,e-1)

print(end_of_arr)
for i in range(end_of_arr):
    print(arr[i])
