# 동전들이 주어졌을때 2명이서 최소한의 차이로 나누기
# [1, 2, 4, 6]이 주어졌다고 가정

import sys

coins = [1, 2, 4, 6]
sum_coin = sum(coins)
length = sum_coin + 1
# dp[x]가 1이란건 주어진 동전으로 x를 만들수있음
dp = [0] * length
dp[0] = 1
tot = 0 # for문에서 탐색할때 사용

for coin in coins:
    # 중복 문제때문에 역순으로 돌림
    for i in range(tot, -1, -1):
        if dp[i] == 1 and i+coin < length:
            dp[i+coin] = 1
            tot += dp[i+coin]

# 정답은 1로 세팅된 위치*2 - 합계(sum(coins)가 최소가 되는 값
answer = sys.maxsize
for i in range(len(dp)):
    if dp[i] == 1:
        tmp = abs(i*2 - sum_coin)
        answer = min(answer, tmp)

print(answer)
