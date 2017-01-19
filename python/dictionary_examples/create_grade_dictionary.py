grades = {}
while(True):
    print("Enter a name: (blank to quit):")
    name = raw_input()
    if name == '':
        break
    if name in grades:
        print(' {grade} is the grade of {name} ').format(grade=grades[name],name=name)
    else:
        print("we have not the grade of {name}").format(name=name)
        print("what is his/her grade?:")
        grade = input()
        grades[name]=grade
        print("Yes we updated database")
for name in grades:
    print "{name} : {grade}".format(name=name,grade=grades[name])

