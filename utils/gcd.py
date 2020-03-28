def gcd(a, b):
    if a < b :
        a, b = b, a
    while True:
        a, b = b, a % b
        if b == 0:
            return a