def swap(lst,position):
    e1 = lst[position]
    e2 = lst[position+1]
    lst[position] = e2
    lst[position+1] = e1
    return lst

def bubblesort(l):
    sl = l
    isswapinloop = True
    while isswapinloop:
        swpctr = 0
        for i in range(0,len(l)-1):
            if l[i] > l[i+1]:
                swpctr +=1
                sl = swap(sl,i)
            if swpctr >0:
                isswapinloop = True
            else:
                isswapinloop = False
    return sl
