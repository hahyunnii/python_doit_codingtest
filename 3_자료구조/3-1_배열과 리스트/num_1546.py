n = input()
myList = list(map(int, input().split()))
mymax = max(myList)
sum = sum(myList)

print(sum*100 / mymax / int(n))