print('hello')
n=1+2
#print (n)

name = 'Arun'
print(f'name is {name}');
name = name[0:3]
print(f'name is {name}');
t=(1,2,3)
l=list(t)
#print(l)


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
val = d['k1'][0]['nest_key'][1][0]
#print(val)

d1 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
val1=d1['k1'][2]['k2'][1]['tough'][2][0]
#print(val1)


if (val == val1):
    #print("same values")
else:
    #print("diff values")

if not (val == val1):
    #print("same values")
elif (val == val1):
    #print("testing elif")
else:
    #print("diff values")
#enumerate
#range
#zip
for tmp in l:
    #print(tmp)
#list comprehension
result = [num if num%2==0 else num+1 for num in l]
#print(result)

result1 = [num for num in l if num%2==0]
#print(result1)

#my_list = []
#for x in [1,2,3]:
#    for y in [100,200,300]:
#        my_list.append(x*y)
#        print(my_list)
my_list1 = [x*y for x in [1,2,3] for y in [100,200,300]] #this is equivalant to lines 46 to 50
#print(my_list1)

#LEGB Rule for variables
#special methods example (__str__, __len__, __del__)
#try except(on error) else(no eorro) finally(it will always run)


#changing a string to an iterator, we can only change iterable objects to iterators
s = 'Arun Prakash'
si = iter(s)
next(si)


#Counter collection


tmd = datetime.date.today()
tmd.day # to get the day

tme = datetime.time(5,10,39,999098) # input in the order of hour, minute, second, micro second

#iterate through dates
dte1 = dte1 + datetime.timedelta(1) #ypu can pass the number of days to be added as a param in timedelta function

#Python Debugger

import pdb
#to invoke debugger use below
pdb.set_trace()

#regexp split
re.split('[0-9]',txt)
#this is pretty much same as str.split(), here we can split based on pattern


s = 'test string'
s.isalnum() #boolean to say if its alpha numeric
s.isalpha() #to check if the string is fully alpha
s.isspace()
s.title()
s.partition('s')  # ['te', 's', 't string'] split only on the first occurance and also return the seperator string

#set operators
s.disjoint(s1)#returns True if there is no common elements in the two sets
s.issubset(s1)
s.issuperset(s1)
