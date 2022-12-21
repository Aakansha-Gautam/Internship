# creating the class to use it as constructor

class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age

    @classmethod
    def construct(cls,string):
        firstname,lastname,age=string.split(',')
        return cls(firstname,lastname,age)

    

Aakansha=Person.construct('Aakansha,Gautam,21')
print(Aakansha.firstname)