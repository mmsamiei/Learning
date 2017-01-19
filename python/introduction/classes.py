#in the name of Allah


#for define class we get subclass from object:

class Human(object):
    species = "H. sapiens"  #this is attribute
    def __init__(self, name):   #this is a constructor
        self.name = name
        self.age = 0
    def say(self, msg):     #this is a method
        return "{self}: {msg}".format(self=self.name,msg=msg)

    #an classmethod shared between all of instances
    @classmethod
    def get_species(cls):
        return cls.species

    #property acts like getter
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    #instantiate a class
p = Human(name="parham")
print p.say("hi")

i = Human(name="iman")
print i.say("hello {friend}").format(friend=p.name)

p.age = 20


