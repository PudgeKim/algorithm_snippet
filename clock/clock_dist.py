# 시계에서 두 위치의 거리중 가까운 거리를 return

def get_dist_from_clock(a, b):
    a, b = max(a, b), min(a, b)
    if a-b > 6:
        result = 12 - (a-b)
    else:
        result = a - b
    return result

# 시계가 아닌 원인 경우 n 인자를 추가

def get_dist_from_clock(a, b, n):
    a, b = max(a, b), min(a, b)
    if a-b > n//2: # n이 자연수가 아닌 경우 n/2 고려
        result = n - (a-b)
    else:
        result = a - b
    return result
