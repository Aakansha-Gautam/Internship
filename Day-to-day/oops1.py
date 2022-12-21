class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price

aakansha=Laptop("Asus","Vivobook","20")
shasha=Laptop("Dell","Dell",30)

print("Aakansha instance")
print(aakansha.brand_name)
print(aakansha.model_name)
print(aakansha.price)

print("Shasha Instance")
print(shasha.brand_name)
print(shasha.model_name)
print(shasha.price)
