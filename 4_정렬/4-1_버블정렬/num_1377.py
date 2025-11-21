import sys
input = sys.stdin.readline


n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))

# sorted_arr = sorted(arr)
sorted_arr = sorted(arr, key=lambda x : x[0])
answer = []
for i in range(n):
    answer.append(sorted_arr[i][1] - arr[i][1])

max = 0
for i in range(n):
    if (max < answer[i]):
        max = answer[i]

print(max+1)

