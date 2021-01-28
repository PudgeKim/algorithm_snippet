# a = (1, 2), b = (1, 2, 3)일 때 a가 b의 부분집합인지를 알고 싶을 때

a = (1, 2)
b = (1, 2, 3)

tmp_a = set(a)
tmp_b = set(b)

tmp_a.issubset(tmp_b) # return 결과는 boolean

# 그 밖의 set은 intersection, union, diffrence 등 지원
