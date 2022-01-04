# 동일한 문제를 리스트를 이용하지 않고
# 변수 2개를 이용해서 구현

# 이렇게 하면 변수 3개인가요?ㅜㅜ
# 횟수를 표현할 방법을 못찾겠습니다.
n=int(input())
a = 0
b = 1
i = 1
while True :
      a, b = b, a+b
      i += 1
      if i == n:
          break

print(b)