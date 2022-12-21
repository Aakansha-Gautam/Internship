class Phone:
    def __init__ (self,name,year,price):
        self.name=name
        self.year=year
        self.price=price

    def info(self):
        return f"{self.name} {self.year}"
    
    def __str__(self):
        return f"{self.name}, {self.year}, {self.price}"

    def __add__(self,other):
        return self.price+other.price
phone=Phone('Iphone',2022,2000)
phone1=Phone('Apple',2022,10)
print(str(phone))
print(phone.info())
print(phone+phone1)