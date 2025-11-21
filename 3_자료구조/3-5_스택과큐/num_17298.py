import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

answer = [-1] * n
stack = []

for i in range(n):
    while stack and num[stack[-1]] < num[i]:
        answer[stack.pop()] = num[i]
    stack.append(i)

print(*answer)
