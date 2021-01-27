import collections

a = collections.Counter()
b = collections.Counter()

a & b  # a와 b의 교집합 (intersection)
a | b  # a와 b의 합집합 (union)

# 집합 연산시 각 원소가 쭉 늘어지는게 아님
# 예시)
# a & b의 결과가 sheep이 2개라면 ['sheep', 'sheep']이 아닌
# {'sheep': 2} 의 형태
