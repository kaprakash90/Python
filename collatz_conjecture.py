def collatz_conjecture(n):
    steps = 0
    ccl = [n]
    while n!=1:
        if n%2 == 0:
            n /=2
            ccl.append(int(n))
        else:
            n = (n*3)+1
            ccl.append(int(n))
        steps +=1
    print(ccl)
    return steps
