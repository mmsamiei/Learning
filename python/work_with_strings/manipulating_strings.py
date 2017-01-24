""" this is
multi line
comment! """


flag = "hello" in "i am hello"
print "flag is {flag}".format(flag=flag)


str = "Hello, I am Mahdi"
print str.upper()
print str.lower()

# they used to make case insensetive comparsion for example:

print("could you get units?")
answer = raw_input()
if answer.lower() == 'no':
    print "damn to Nick!"
else:
    print "thanks from God"


print 'hello oh'.isalpha()  #return true if consist only of letters and not blank
#print 'hell23'.isdecimal()    #return true if consist only of letters and numbers
#print '123'.isdecimal()
print '     '.isspace()     #return true if string consists only of blank spaces
print 'This Is A Title'.istitle()

#continue to Startwith() and Endwith() methods

