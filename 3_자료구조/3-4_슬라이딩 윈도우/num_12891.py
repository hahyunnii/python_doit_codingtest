checkList = [0]*4  # [needA, needC, needG, needT]
myList = [0]*4     # [cntA, cntC, cntG, cntT]
checkSecret = 0    # 조건을 충족한 문자 종류의 수 (0~4)

def myadd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
result = 0
A = list(input().strip())
checkList = list(map(int, input().split()))

# 요구 개수가 0인 항목은 이미 충족된 것으로 간주
for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

# 초기 윈도우 [0, P-1]
for i in range(P):
    myadd(A[i])
if checkSecret == 4:
    result += 1

# 슬라이딩 윈도우
for i in range(P, S):
    j=i-P
    myadd(A[i])        # 새로 들어온 문자
    myremove(A[j])   # 빠져나간 문자
    if checkSecret == 4:
        result += 1

print(result)
