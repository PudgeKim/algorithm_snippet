# 결과값을 도출할 때 left와 right의 범위를 잘 생각해봐야하고
# 단순히 mid값을 return 하면 안된다. 

# 1부터 100까지를 이분탐색하는 경우

answer = 0
left, right = 0, 100 # left를 1이 아닌 -1한 0으로
while left<=right:
	mid = (left+right) // 2
	if True:
		left = mid + 1
		answer = mid
	else:
		right = mid - 1

