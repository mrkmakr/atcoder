
def power(x, y, mod):
    """
    https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
    二分累乗法でx ** yを求める
    
    2 ** n = 4 ** (n//2) = 16 ** (n//4)
    みたいなことをする
    """

    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2, mod)**2 % mod
    else            : return power(x, y//2, mod)**2 * x % mod


def mul(a, b, mod):
    """
    https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
    modを加味したかけ算を行う
    """
    return ((a % mod) * (b % mod)) % mod

def div(a, b, mod):
    """
    https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6
    modを加味した割り算を行う    
    """
    if a == b:
        return 1
    return mul(a, power(b, mod-2, mod), mod)


def factorial_part(start, last, mod):
    """
    startからlastまでのかけ算を行う
    
    factorial_part(2, 4, mod) = 2 * 3 * 4 = 24    
    """
    assert(start <= last)
    x = 1
    for k in range(start, last+1):
        x *= k
        x %= mod
    return x

mod = int(1e9) + 7
