class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
    
    def display(self):
        print(f"{self.brand_name} {self.model_name} {self.price}")

    def apply_discount(self,amt):
        self.amt=amt
        print(f"The price after discount is: {self.price-self.amt}")

aakansha=Laptop("Asus","Vivobook",20)
shasha=Laptop("Dell","Dell",30)

aakansha.display()
aakansha.apply_discount(5)
shasha.display()
shasha.apply_discount(10)