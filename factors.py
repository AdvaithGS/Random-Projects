def prime(n:int):
    if n in (1,2):
        return True
    l = [i for i in range(2,n+1)]
    #print(l)
    while len(l) != 1:
        x = l[0]
        y = l.copy()
        for i in y:
            if i%x == 0:
                l.remove(i)
    return l == [n]
def prime_factors(n:int):
    l = [n]
    for i in range(1,n+1):
        if n%i == 0:
            n = n//i
            if prime(i):
                l.append(i)
            else:
                l.extend(prime_factors(i))
    return list(set(l))


def factors(n:int):
    l = []
    for i in range(1,n+1):
        if n%i == 0:
            l.append(i)
    return l