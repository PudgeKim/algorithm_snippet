# 동전 거스르기
# 필수조건: 각 동전이 2배 이상이여야만 greedy하게 풀 수 있음

# 큰 동전부터 나눗셈 해가며 푼다.

target = 4200
coins = [5, 10, 20, 100, 1000]

coins.sort(reverse=True)
answer = 0
for coin in coins:
    if coin > target:
        continue

    quo, rem = divmod(target, coin)
    answer += quo
    target = rem

    if target == 0:
        break

print(answer)
