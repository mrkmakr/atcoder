
def factorize(n):
    ## 素因数分解
    # arr = factorize(20)
    # arr == [[2, 2], [5, 1]]
    
    result = []
    tmp = n
    for k in range(2, int(n ** 0.5) + 1):
        cnt = 0
        while tmp % k == 0:
            cnt += 1
            tmp //= k
        if cnt > 0:
            result.append([k, cnt])
    if tmp != 1:
        result.append([tmp, 1])
    return result

def divisorize(n):
    ## 約数
    # arr = factorize(20)
    # arr == [2, 4, 5, 10, 20]
    f = factorize(n)
    divisors = [1]
    for k in range(len(f)):
        num_divisors = len(divisors)
        for i in range(1, f[k][1] + 1):
            for j in range(num_divisors):
                divisors.append(divisors[j] * f[k][0] ** i)
    return sorted(divisors)