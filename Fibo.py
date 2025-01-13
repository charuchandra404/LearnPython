def fibo(n):
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b

def fibo2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        print(b)
        a, b = b, a+b
    return result



