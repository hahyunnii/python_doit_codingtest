# 방법1 (그냥 정렬 + 그리디)
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
#
# answer = 0
# for i in range(n):
#     j = (n-i)
#     temp = arr[i] * (j)
#     answer += temp
#
# print(answer)

########################################
# 방법2 (삽입 정렬 + 그리디)
n = int(input())
arr = list(map(int, input()))
s = [0]*n

for i in range(1,n):
    insert_point = i
    insert_value = arr[i]
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            insert_point = j+1
            break
        if j==0:
            insert_point = 0
    for j in range(i, insert_point, -1)

