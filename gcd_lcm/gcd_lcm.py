# 최대공약수 구하는 법
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b>0:
        a, b = b, a%b
    return a


# 최소공배수는 두 수의 곱을 최대공약수로 나눈 값
# 최소공배수는 두 수를 소인수분해하여 안겹치는 값, 지수가 높은 값들의 곱

# N(N>2)개의 최소공배수를 구하는 법
# 배열에서 2개씩 뽑아 최소공배수를 만들고 이걸 배열에 원소가 1개남을때까지 반복

def solution(arr):
    if len(arr) == 1:
        return arr[0]
    while arr:
        n1 = arr.pop()
        n2 = arr.pop()
        lcm = n1*n2//gcd(n1, n2)
        arr.append(lcm)
        
        if len(arr) == 1:
            break
    
    return arr[0]
