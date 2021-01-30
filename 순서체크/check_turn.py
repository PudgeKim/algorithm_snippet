# 총 n명이 있고 내 차례가 p번째일 때 매번 내 순서 구하기

cnt = 1    # 순서를 나타냄 계속 1씩 증가
round = 1  # 모든 인원이 돌때마다 1씩 증가
dest = 10  # 10번째 까지 돈다고 가정
while cnt <= dest:
	if (round-1)*n+p == cnt:
		print('my turn')

	if cnt%n == 0:
		round += 1
	cnt += 1   # round를 증가시키고 cnt를 증가시켜야 오류X
