# 피보나치 수열: 보텀업 다이나믹 프로그래밍 소스코드
d = [0] * 46

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = int(input())

# 피보나치 함수(Fibonacci Function) 반복문으로 구현
for i in range(3, n + 1):
  d[i] = d[i - 1] + d[i - 2]

print(d[n])