

def decode(it):
    for x, L in it:
        for i in range(L):
            yield x

def encode(it):
    x = next(it)
    L = 1
    while True:
        try :
            n = next(it)
            if x == n:
                L += 1
            else:
                yield (x, L)
                L = 1
                x = n
        except StopIteration:
            yield (x, L)
            return
            
