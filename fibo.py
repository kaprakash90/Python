def fibo_lst(N):
    assert N>=0 # to check if its greater than 0 else throw an AssertionError
    l=[]
    for i in range(0,N+1):
        if i in (1,0):
            l.append(i)
        else:
            l.append(l[i-1]+l[i-2])
    return l

def fibo_str(N):
    assert N>=0
    l=[]
    for i in range(0,N+1):
        if i in (1,0):
            l.append(i)
        else:
            l.append(l[i-1]+l[i-2])
    l=map(str,l)
    return ', '.join(l)
