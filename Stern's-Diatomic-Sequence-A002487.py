https://oeis.org/A002487

def Generate_A002487():
    a = [1]
    yield a[-1]
    while True:
        if len(a)%2==0:
            a.append(a[len(a)>>1]+a[len(a)>>1-1])
            yield a[-1]
        else:
            a.append(a[len(a)>>1])
            yield a[-1]
