# 이분탐색으로 특정값 하나를 찾는게 아니고 특정 조건에 만족할 때
# 이분탐색 이용하기

# 1 ~ 100에서 이용한다고 가정

answer = 0
left, right = 0, 100  # left를 범위의 최소값에서 -1
while left <= right:
	mid = (left+right) // 2
	if True:
		left = mid + 1
		answer = mid
	else:
		right = mid -1

return answer


# 방법2
left, right= 1, 100+1  # right값을 1늘려줌

while (left < right-1):
	mid = (left+right) // 2
	if True:
		left = mid
	else:
		right = mid

return left  # left를 return
