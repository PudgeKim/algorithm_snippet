# 시계(원)를 직선으로 바꾸기

n = 12 # 일반적인 시계일 경우
vertexes = [1, 5, 6, 10] # 원안에 특정 점들

converted = vertexes + [v+n for v in vertexes]
# 순환시에는 vertexes만큼만 돌면됨
# 10 이후는 다시 1부터 도는 것이므로 중복됨
