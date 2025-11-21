
# 방법1
# arr = list(map(int, str(input())))
# arr.sort(reverse=True)
#
# for x in arr:
#     print(x, end='')


#방법2 (선택 정렬)
import sys
input = sys.stdin.readline

arr = list(map(int, input().strip()))


for i in range(len(arr)-1):
    max_idx = i
    for j in range(i+1, len(arr)):
        if arr[max_idx] < arr[j]:
            max_idx = j
    arr[i], arr[max_idx] = arr[max_idx], arr[i]

for x in arr:
    print(x, end='')