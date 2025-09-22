import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n (수열의 개수), m (나누어떨어져야 하는 수)
A = list(map(int, input().split())) #원본 수열 저장 리스트
S = [0]*n #합 배열
C = [0]*m #같은 나머지의 인덱스를 카운트하는 리스트
answer = 0 #정답 변수

for i in range(n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i]%m
    if remainder == 0:
        answer +=1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)
print(answer)