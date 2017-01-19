var = input("input your Grade:")
if(var>18):
    print"You are Shakh"
elif(var>=10):
    print"You passed"
else:
    print"Fail"


li = ["iman","parham","sohrab"]
for std in li:
    print "{std_name} is shakh".format(std_name=std)


for i in range(5):
    print i     #prints 0 1 2 3 4

for i in range(5,9):
    print i     #prints 5 6 7 8

parham_grade = 12
while parham_grade < 18:
    print "the parham grade is {grade}".format(grade=parham_grade)
    parham_grade=parham_grade+1



