# 시계에서 두 위치의 거리중 가까운 거리를 return

def get_dist_from_clock(a, b):
    a, b = max(a, b), min(a, b)
    if a-b > 6:
        result = 12 - (a-b)
    else:
        result = a - b
    return result
