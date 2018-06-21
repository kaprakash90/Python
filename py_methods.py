def addition(a , b):
    return a+b

def my_function (ip1: int, ip2: str) -> str: #setting the datatype for inputs and o/p
    return(str(ip1) + ip2)

#*args (indefinte i/ps)
#**kwargs (dictionary input
def myfunc(*args):
    mylist = []
    for i in args:
        if i%2==0:
            mylist.append(i)
    return(mylist)

def wordpros(s):
    a = ''
    for j in range(0,len(str(s))):
            if j%2 == 0:
                a += s[j].capitalize()
            else:
                a+=s[j]
    return a

def wordpros(*args):
    a = ''
    for i in args:
        for j in range(0,len(str(i))):
            if j%2 == 0:
                a += i[j].capitalize()
            else:
                a+=i[j]
    return a
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)

def animal_crackers(text):
    '''animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False'''
    x = text.split(' ')
    return x[0][0] == x[1][0]

def makes_twenty(n1,n2):
    '''makes_twenty(20,10) --> True
    makes_twenty(12,8) --> True
    makes_twenty(2,3) --> False'''
    return n1+n2 == 20 or n1==20 or n2==20

def old_macdonald(name):
    '''old_macdonald('macdonald') --> MacDonald'''
    a=''
    for i in range(0,len(name)):
        if i in [0,3]:
            a += name[i].capitalize()
        else:
            a += name[i]
    return a

def master_yoda(text):
    x = text.split(' ')
    x.reverse()
    y=x
    return " ".join(y)

def almost_there(n):
    '''almost_there(90) --> True
    almost_there(104) --> True
    almost_there(150) --> False
    almost_there(209) --> True'''
    return (abs(n-100) <= 10 ) or (abs(n-200)<=10)

def has_33(nums):
    '''has_33([1, 3, 3]) → True
    has_33([1, 3, 1, 3]) → False
    has_33([3, 1, 3]) → False'''
    a = False
    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1] ==3:
            a = True
            break
    return a

def paper_doll(text):
    '''paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'''
    op_str=''
    for i in text:
        op_str+=i*3
    return op_str

def blackjack(a,b,c):
    m = a+ b+ c
    if m <= 21:
        return m
    elif 11 in (a,b,c) and m <=31:
        return m-10
    else:
         return'BUST'

def summer_69(arr):
    a=0
    canadd = True
    for i in range(0,len(arr)):
        if arr[i] != 6 and canadd:
                a += arr[i]
        else:
            canadd = False
            if arr[i] == 9:
                canadd = True
    return a


def spy_game(nums):
    ele = ''
    for i in nums:
        if i in (0,7):
            ele += str(i)
    return ele in '007'

def count_primes(num):
    mylist = list(range(2,num+1))
    for i in range(1,num+1):
        sqr = int(i**0.5)
        for j in range(2,sqr+1):
            if i%j == 0:
                mylist.remove(i)
                break
    print(mylist)
    return len(mylist)


#for i in range(1,100):
#    if i%3==0 and i%5==0:
#        #print('FizzBuzz')
#    elif i%3==0:
#       # print('Fizz')
#    elif i%5==0:
#        #print('Buzz')
#    else:
#        #print(i)
#py generators
def simple_gen():
    for i in range(10):
        yield i**2def simple_gen():
    for i in range(10):
        yield i**2
#Create a generator that yields "n" random numbers between a low and high number (that are inputs).

import random
def rand_num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)

def fibo(N):
    l=[]
    for i in range(N):
        if i in (1,0):
            l.append(i)
        else:
            l.append(l[i-1]+l[i-2])
    return l
