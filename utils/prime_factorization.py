
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