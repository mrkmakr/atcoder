def binary_search(l, r, hantei):
    ## hanteiはTrue or Falseを返すfunction
    while True:
        if r - l <= 1:
            break
        now = (r + l) // 2
    #     print(l, now, r)
        if hantei(now):
            r = now
        else:
            l = now
    return l
