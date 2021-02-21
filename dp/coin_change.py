# 거슬러줄수있는 동전의 최소개수 구하기
# 15원을 [1,2,5]원으로 거슬러준다고 가정하면
import sys

coins = [1, 2, 5]
dp = [sys.maxsize] * (15+1) # dp[9]는 9원을 거슬러주는데 사용된 동전의 최소개수
dp[0] = 0
# 점화식은 dp[j-coins[i]] + 1
# 예를들어 2원짜리인경우 현재 8원이면 2를 빼서 6원의 최소개수 + 1
# 1원 -> 2원 -> 5원으로 가면서 최소값인 경우  계속 덮어쓰면됨
for i in range(n):
	for j in range(coin[i], 15+1):
		dp[j] = min(dp[j], dp[j-coins[i]]+1)

print(dp[15])

# 주어진 input을 몇가지 방법으로 만들 수 있는지
# [1,2,5]원으로 10원 만든다고 가정하자
# dp[2][10]이 의미하는건 1원과 2원을 사용해서 10원을 몇가지로 거스를 수 있는가
# 점화식은 dp[j] = dp[j] + dp[j-money[i]]

dp = [0]*(n+1)

# 첫번째는 무조건 1가지 방법만 있으므로 초기화하는것
for i in range(1, n+1):
	if i%money[0] == 0:
		dp[i] = 1
	else:
		dp[i] = 0

# 이제 두번째 동전부터 누적시작
for i in range(1, len(money)):
	for j in range(money[i], n+1):
		if j == money[i]:
			dp[j] = dp[j] + 1
		else:
			dp[j] = dp[j] + dp[j-money[i]]

print(dp[-1])
