# class variable
class Person:
    count_instance=0
    def __init__(self,firstname,lastname,age):
        Person.count_instance+=1
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    @classmethod
    def count_instances(cls):
        return(f"The number of total instance is: {cls.count_instance}")
Aakansha=Person("Aakansha","Gautam",20)
Shasha=Person("Shasha","Gautam",21)
Sha=Person("Sha","Gautam",22)
print(Person.count_instances())