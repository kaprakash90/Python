def checksum(n):
    s=str(n)
    while not len(s) == 16:
        try:
            s = input('please enter your 16 digit card number:')
            assert len(s)==16
        except:
            print('Hey the credit card number you entered is not having 16 digits!!! try again..')
    cs = 0
    j = 0
    ls = int(s[-1])
    for i in s[:len(s)-1]:
        if j%2 == 0:
            ms =int(i)*2
            if ms >=10:
                ms = int(str(ms)[0])+int(str(ms)[1])
            cs += ms
        else:
            cs +=int(i)
        j +=1

    cs = (9*cs)%10
    if ls == cs:
        #print(f'Valid card! as cs is {cs} and ls is {ls}!!!!')
        return 'Valid'
    else:
        #print(f'Not valid as cs is {cs} and ls is {ls}')
        return 'Not Valid'

#checksum(5497774415583614)
