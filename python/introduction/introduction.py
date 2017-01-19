print 2/5   #print 0


print 2.0/5.0   #print 0.4


print 5.0//3.0 #print 1


print 2**3  #print 8


print True and False
print True or False


print 2 < 3 < 4     #print True
print 2 < 3 < 1     #print False


#strings can be added
"Hello"+"parham"


print "parham"[0]   #print P


print(len("parham"))


p = "parham"
i = 21
print "my name is %s and i have %d years old" %(p,i)
print "my name is {name} and i have {age} years old".format(name=p,age=i)


#we have None Object in python for compare Objects to None we must use is
p = None
print p is None     #prints True



#FOR GET STRING FROM USER
string_input = raw_input("Enter some string values:")
print string_input

#FOR GET INTEGER FROM USER
age = input("Enter your Age:")
print age


li = []
li = [1, 2, 3]
li.append(4)
print(li)   #print list 1,2,3,4
li.pop()    #now list is 1,2,3
print(li[1])    #print 2
print(li[-1])   #print last elemet 3

li = [0,1,2,3,4,5,6,7,8]
print li[0:3]   #print form 0 to 2
print li[1:]    #print from 1 to end
print li[0::2]  #prints 0,2,4,6,8
print li[1::4]  #prints 1,4,7
print li[::-1]  #prints 8,7,6,5,4,3,2,1,0

li = li + li[::-1]  #concatenate two list
print li

li.insert(1,99)     #insert at specefic index
print li    #now we have 0,99,1,2,3,4,...
print li.index(99)
li.remove(99)
print li



