def mergefunc(l1,l2):
    mergelist = []
    while len(l1)>0 and len(l2)>0:
        if l1[0] < l2[0]:
            mergelist.append(l1.pop(0))
        else:
            mergelist.append(l2.pop(0))
    if len(l1)>0:
        mergelist.extend(l1)
    else:
        mergelist.extend(l2)
    #print (f'merged {mergelist}')
    return mergelist



def msort(l):
    if len(l) <= 1:
        return l # return a signle value list if the list contains only one value and to stop recursive call
    parkey = int(len(l)/2)

    l1 = l[:parkey]
    l2 = l[parkey:len(l)+1]
    #print (f'l1 is {l1} and l2 is {l2}')
    l1 = msort(l1)
    l2 = msort(l2)
    #print(f'going to call merge with {l1} and {l2}')
    sl = mergefunc(l1,l2)

    return sl

userinput = input('Enter the list you wanna sort:')
userlist = list(map(int,userinput.split(',')))
sortedlist = msort(userlist)
print(sortedlist)
