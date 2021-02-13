# 위상정렬: 일의 순서를 지키면서 전체 일의 순서를 정하기

# 일이 1번부터 6번까지 있다고 가정
# degree는 들어오는 차수를 뜻함
# ex)
# 1 4
# 5 4
# 주어지면 degree[4]를 2 늘려줌
degree = [0] * 7  # 인덱스 1번은 1번으로 활용하기 위해 리스트 개수 1개 더 늘림
                  # 만약 degree[1]이 0이라면 1번 일을 하기위해 
	          # 선행해야할 일이 없다는 뜻

q = deque()      
# 선행되어야 하는 일이 없는 것부터 queue에 넣음
for i in range(1, len(degree)):
	if degree[i] == 0:
		q.append(i)                  

while q:
	work = q.popleft()
	# work가 만약 1이라면 1이 향하는 진입차수를 1 줄여줌
	# 4번을 하기전에 1번을 해야하므로 4번을 1 줄여줌
	# 위 과정을 위해 defaultdict(list) 이용하자 (2d array는 메모리 낭비)
	# 예를들면 graph[1][4]가 1이면 1에서 4로 가고 있다는 뜻

	# 이렇게 줄이다가 0이되면 queue에 넣음 
