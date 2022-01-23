import time, random


def evaluate_n2(A, x):
    # code for O(n^2)-time function
    ans = 0
    for i in range(len(A)):
        num = 1
        for _ in range(i):
            num = num * x
        ans += A[i] * num
    return ans


def evaluate_n(A, x):
    # code for O(n)-time function
    ret = 1
    ans = A[0]
    for i in range(1, len(A)):
        ret *= x
        ans += A[i] * ret
    return ans


random.seed()  # random 함수 초기화
# n 입력받음
n = int(input())
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = [random.randint(-1000, 1000) for _ in range(n)]
x = random.randint(-1000, 1000)

s1 = time.process_time()
# evaluate_n2 호출
evaluate_n2(A, x)
e1 = time.process_time()
print('O(n^2) 수행시간:', e1 - s1)

s2 = time.process_time()
# evaluate_n 호출
evaluate_n(A, x)
e2 = time.process_time()
print('O(n) 수행시간:', e2 - s2)
# 두 함수의 수행시간 출력
