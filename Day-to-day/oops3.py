# class variable
class Person:
    count_instance=0
    def __init__(self,firstname,lastname,age):
        Person.count_instance+=1
        self.firstname=firstname
        self.lastname=lastname
        self.age=age

Aakansha=Person("Aakansha","Gautam",20)
Shasha=Person("Shasha","Gautam",21)
Sha=Person("Sha","Gautam",22)
print(Person.count_instance)