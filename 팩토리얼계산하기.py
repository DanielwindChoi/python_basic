# 정수 n이 주어졌을 때
# n! 구하는 프로그램을 작성해보자

n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
print(result)