#inheritance

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def display(self):
        return(f"{self.fname}  {self.lname}")


class Additional(Person):
    def __init__(self,fname,lname,age,address):
        super().__init__(fname,lname)
        self.age=age
        self.address=address
    

    def display(self):
        return(f"{self.fname}  {self.lname} {self.age} {self.address}")

ha=Additional("Aakansha","Gautam",20,"Boudha")

print(ha.display())

print(help(Additional))